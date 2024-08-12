# sports/football/models.py
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db import models

try:
    from core_application import models as core_models
except ImportError:
    from ...core_application import models as core_models


class PlayerInfo(core_models.PlayerInfo):
    """
    Football player info model
    Fields:
    - name: CharField
    - email: EmailField
    - date_of_birth: DateField
    """
    pass


class Record(core_models.Record):
    """
    Football record model
    Fields
    - wins: Number of wins
    - losses: Number of losses
    - draws: Number of draws
    - goals: Number of goals
    """
    goals = models.IntegerField(default=0)


class TeamStats(core_models.TeamStats):
    """
    Football team stats model
    Fields:
    - wins: int
    - losses: int
    - draws: int
    - average_goals_per_game: float
    """
    average_goals_per_game = models.FloatField(default=0)

    def clean(self):
        if self.average_goals_per_game < 0:
            raise ValidationError("Average goals per game must be greater than 0")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class Team(core_models.Team):
    """
    Football team model
    Fields:
    - name: CharField
    - stats: TeamStats
    """
    stats = models.ForeignKey(TeamStats, on_delete=models.CASCADE)


class Player(core_models.Player):
    """
    Football player model
    Fields:
    - info: PlayerInfo
    - record: Record
    - team: Team
    """
    info = models.ForeignKey(PlayerInfo, on_delete=models.CASCADE)
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)


class TournamentInfo(core_models.TournamentInfo):
    """
    Football tournament model
    Fields:
    - name: CharField
    - date: DateField
    - active: BooleanField
    - type: TOURNAMENT_TYPE_CHOICES[LEAGUE, CHAMPIONSHIP, DEFAULT_EVENT](L,C,E)
    """

    class TournamentType(models.TextChoices):
        LEAGUE = 'L', _("Liga")  # another way to write tuples and gettextlazy is _
        CHAMPIONSHIP = 'C', _("Campeonato")
        DEFAULT_EVENT = 'E', _("Evento")

    type = models.CharField(max_length=1,
                            choices=TournamentType,
                            default=TournamentType.DEFAULT_EVENT)
    rounds = models.IntegerField(default=0)


class MatchTeamStats(core_models.MatchTeamStats):
    """
    Football match team stats model
    Fields:
    - team: FK Team
    - goals: IntegerField
    """
    team = models.ForeignKey(Team, null=True, on_delete=models.CASCADE)
    goals = models.IntegerField(default=0)


class MatchStats(core_models.MatchStats):
    """
    Football match stats model
    Fields:
    - team_1_stats: MatchTeamStats
    - team_2_stats: MatchTeamStats
    - winner: Team
    - is_draw: BooleanField
    - is_finished: BooleanField
    """
    team_1_stats = models.ForeignKey(MatchTeamStats, null=True, related_name="stats_team1", on_delete=models.CASCADE)
    team_2_stats = models.ForeignKey(MatchTeamStats, null=True, related_name="stats_team2", on_delete=models.CASCADE)
    winner = models.ForeignKey(Team, null=True, default=None, on_delete=models.CASCADE)
    is_draw = models.BooleanField(default=False)
    is_finished = models.BooleanField(default=False)

    def createTeamMatchStats(self, team: Team, number: int):

        if number < 1 or number > 2:
            raise ValidationError("Number of team must be 1 or 2")

        if number == 1:
            self.team_1_stats = MatchTeamStats(team=team, goals=0)
            self.team_1_stats.save()
        elif number == 2:
            self.team_2_stats = MatchTeamStats(team=team, goals=0)
            self.team_2_stats.save()

        self.save()

    def finishMatch(self, winner: Team, is_draw: bool):
        """
        Finishes the match
        :param winner: Team
        :param is_draw: BooleanField
        """
        if is_draw:
            self.is_draw = True
            self.save()
            return

        if winner is None:
            raise ValidationError("Winner cannot be None")

        if winner != self.team_1_stats.team or winner != self.team_2_stats.team:
            raise ValidationError("Winner MUST be one of the teams in the match")

        self.winner = winner
        self.is_finished = True
        self.is_draw = False
        self.save()

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)


class Match(core_models.Match):
    """
    Football match model
    Fields:
    - date_time: DateTimeField
    - team_1: Team
    - team_2: Team
    - match_stats: MatchStats
    - tournament_info: TournamentInfo
    - round: int
    """
    # a team is null when the match is not determined yet
    team_1 = models.ForeignKey(Team, null=True, related_name="matches_as_team1", on_delete=models.CASCADE)
    team_2 = models.ForeignKey(Team, null=True, related_name="matches_as_team2", on_delete=models.CASCADE)

    match_stats = models.ForeignKey(MatchStats, null=True, on_delete=models.CASCADE)
    tournament_info = models.ForeignKey(TournamentInfo, on_delete=models.CASCADE)
    round = models.IntegerField(default=0)

    def addTeam(self, team: Team, team_number: int) -> TeamStats:
        """
        Adds a team to the match, creating and returning its stats that should be added to the match_stats
        :param team: Team
        :param team_number: int (1 or 2)
        :return: TeamStats
        """
        if team is None:
            raise ValidationError("Team cannot be None")

        if team_number == 1:
            self.team_1 = team
            self.save()
            return self.match_stats.createTeamMatchStats(team=team, number=team_number)
        elif team_number == 2:
            self.team_2 = team
            self.save()
            return self.match_stats.createTeamMatchStats(team=team, number=team_number)

        raise ValidationError("Team number must be 1 or 2")

    @property
    def winner(self) -> Team:
        return self.match_stats.winner

    def save(self, *args, **kwargs):

        if self.match_stats is None:
            Exception("Trying to save a match with an empty match_stats object")

        super().save(*args, **kwargs)

    def __str__(self):

        return f"ID {self.id} {self.team_1} vs {self.team_2}. Date: {self.date_time}. Tournament: {self.tournament_info}. Winner: {self.match_stats.winner}"


class MatchParenting(models.Model):
    """
    Football match parenting model
    Fields:
    - match: Match
    - parent_match: Match
    - team_number: Number of team SmallIntegerField
    """
    child_match = models.ForeignKey(Match, related_name="match_parenting", on_delete=models.CASCADE)
    parent_match = models.ForeignKey(Match, null=False, related_name="parent_of_match", on_delete=models.CASCADE)
    team_number = models.SmallIntegerField(null=False, default=1)

    def __str__(self):
        return f"Parent: {self.parent_match}. Child: {self.child_match}. Inheriting Team: {self.team_number}"
