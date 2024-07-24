from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class PlayerInfo(models.Model):
    """
    Player information model, personal information, etc
    Fields:
    - name: CharField
    - email: EmailField
    """
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f"{self.name} {self.email}"


class TeamStats(models.Model):
    """
    Collects stats about a team
    """
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)

    class Meta:
        abstract = True


class Team(models.Model):
    """
    Team model that collects the base data of a team
    """
    name = models.CharField(max_length=20, unique=True, null=False)
    stats = models.ForeignKey(TeamStats, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f"{self.name}"


class Record(models.Model):
    """
    Record Model saves all the stats related to a player
    """
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)

    class Meta:
        abstract = True


class Player(models.Model):
    """
    Player Model links the info, sport, team and record
    """
    info = models.ForeignKey(PlayerInfo, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    record = models.ForeignKey(Record, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f"{self.info.name}"


class Tournament(models.Model):
    """
    Tournament Model to save the data from any type of competition/tournament
    """
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f"{self.name}"


class MatchTeamStats(models.Model):
    """
    Collects the data of the team that played a match
    """
    winner = models.BooleanField(default=False)

    class Meta:
        abstract = True


class MatchStats(models.Model):
    """
    Match stats model, the base collects stats of each team
    """
    team_1_stats = models.ForeignKey(MatchTeamStats, on_delete=models.CASCADE)
    team_2_stats = models.ForeignKey(MatchTeamStats, on_delete=models.CASCADE)

    class Meta:
        abstract = True


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

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f"{self.tournament.name} {self.team_1.name} {self.team_2.name} {self.date_time}"


class News(models.Model):
    """
    News model so the Gestor of our site could create News
    """
    image_route = models.ImageField(upload_to="static/images/")
    title = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        abstract = True
