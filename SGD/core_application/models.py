from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class PlayerInfo(models.Model):
    """
    Player information model, personal information, etc
    """
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)


class Sport(models.Model):
    """
    Sport base model
    """
    name = models.CharField(max_length=50)


class TeamStats(models.Model):
    """
    Collects stats about a team
    """
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)


class Team(models.Model):
    """
    Team model that collects the base data of a team
    """
    name = models.CharField(max_length=100)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    stats = models.ForeignKey(TeamStats, on_delete=models.CASCADE)


class Record(models.Model):
    """
    Record Model saves all the stats related to a player
    """
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)


class Player(models.Model):
    """
    Player Model links the info, sport, team and record
    """
    info = models.ForeignKey(PlayerInfo, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    record = models.ForeignKey(Record, on_delete=models.CASCADE)


class Tournament(models.Model):
    """
    Tournament Model to save the data from any type of competition/tournament
    """
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    active = models.BooleanField(default=True)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)


class MatchTeamStats(models.Model):
    """
    Collects the data of the team that played a match
    """
    winner = models.BooleanField(default=False)


class MatchStats(models.Model):
    """
    Match stats model, the base collects stats of each team, then you should make an instance of this model
    """
    team_1_stats = models.ForeignKey(TeamStats, on_delete=models.CASCADE)
    team_2_stats = models.ForeignKey(TeamStats, on_delete=models.CASCADE)


class Match(models.Model):
    """
    Match model, base to date of match and check if the opponents are a team
    """
    date_time = models.DateTimeField()
    is_team = models.BooleanField(default=True)

    content_type_team_1 = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='team_1_content_type')
    object_id_team_1 = models.PositiveIntegerField()
    team_1 = GenericForeignKey('content_type_team_1', 'object_id_team_1')

    content_type_team_2 = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='team_2_content_type')
    object_id_team_2 = models.PositiveIntegerField()
    team_2 = GenericForeignKey('content_type_team_2', 'object_id_team_2')

    match_stats = models.ForeignKey(MatchStats, on_delete=models.CASCADE, null=True, blank=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
