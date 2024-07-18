from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
try:
    from core_application import models as core_models
except ImportError:
    from ...core_application import models as core_models


class PlayerInfo(core_models.PlayerInfo):
    """
    Table Tennis Player Info
    """
    pass


class Record(core_models.Record):
    """
    Table Tennis Record
    """
    attack_efficiency = models.FloatField(default=0)
    serving_efficiency = models.FloatField(default=0)
    defense_efficiency = models.FloatField(default=0)


class Player(core_models.Player):
    """
    Table Tennis Player model

    :param info: PlayerInfo
    :param record: Record
    """
    info = models.ForeignKey(PlayerInfo, on_delete=models.CASCADE)
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    team = None


class DuoStats(core_models.TeamStats):
    """
    Since table tennis Team is Duo
    """
    average_points_per_game = models.FloatField(default=0)
    games_played = models.IntegerField(default=0)


class Duo(core_models.Team):
    """
    Table Tennis Duo
    """
    player1 = models.ForeignKey(Player, related_name='player1', on_delete=models.CASCADE)
    player2 = models.ForeignKey(Player, related_name='player2', on_delete=models.CASCADE)
    stats = models.ForeignKey(DuoStats, on_delete=models.CASCADE)


class Tournament(core_models.Tournament):
    """
    Table Tennis Tournament
    """
    SINGLE = 'S'
    DUO = 'D'
    TOURNAMENT_TYPE_CHOICES = [
        (SINGLE, 'Singles'),
        (DUO, 'Doubles'),
    ]
    type = models.CharField(max_length=1, choices=TOURNAMENT_TYPE_CHOICES, default=SINGLE)

    def get_tournament_type(self):
        return self.type

    def __str__(self):
        return f"{self.name} {self.get_tournament_type()}"


class MatchDuoStats(core_models.MatchTeamStats):
    """
    Table Tennis Match Duo Stats
    """
    player1_average_points_per_game = models.FloatField(default=0)
    player2_average_points_per_game = models.FloatField(default=0)
    games_played = models.IntegerField(default=0)


class MatchSingleStats(core_models.MatchTeamStats):
    """
    Table Tennis Match Single Stats
    """
    average_points_per_game = models.FloatField(default=0)
    games_played = models.IntegerField(default=0)


class MatchStats(core_models.MatchStats):
    """
    Table Tennis Match Stats. Not necessarily for Duo, it also works for a single player
    """
    content_type_team_1 = models.ForeignKey(ContentType, on_delete=models.CASCADE,
                                            related_name='team_1_stats_content_type')
    object_id_team_1 = models.PositiveIntegerField()
    team_1_stats = GenericForeignKey('content_type_team_1', 'object_id_team_1')

    content_type_team_2 = models.ForeignKey(ContentType, on_delete=models.CASCADE,
                                            related_name='team_2_stats_content_type')
    object_id_team_2 = models.PositiveIntegerField()
    team_2_stats = GenericForeignKey('content_type_team_2', 'object_id_team_2')

    def clean(self):
        valid_models = ['MatchDuoStats', 'MatchSingleStats']
        team_1_model = self.content_type_team_1
        team_2_model = self.content_type_team_2

        if team_1_model not in valid_models or team_2_model not in valid_models:
            raise ValidationError(
                "Both team stats must be either MatchSingleStats or MatchDuoStats")

        if team_1_model != team_2_model:
            raise ValidationError(
                "Both team stats must be of the same type (either single player stats or duo stats)")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Team 1 Stats: {self.team_1_stats}, Team 2 Stats: {self.team_2_stats}"


class Match(core_models.Match):
    """
    Table Tennis Match
    """

    match_stats = models.ForeignKey(MatchStats, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)

    def clean(self):
        # Ensure that content types match is_team flag
        if self.is_team:
            if (self.content_type_team_1.model != 'Duo' or
                    self.content_type_team_2.model != 'Duo'):
                raise ValidationError("Both opponents must be Duo if is_team flag is true")
        else:
            if (self.content_type_team_1.model != 'Player' or
                    self.content_type_team_2.model != 'Player'):
                raise ValidationError("Both opponents must be Players if is_team is False")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
