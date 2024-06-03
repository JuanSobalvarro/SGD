from django.db import models

class PlayerInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class Sport(models.Model):
    name = models.CharField(max_length=50)

class Team(models.Model):
    name = models.CharField(max_length=100)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)

class Record(models.Model):
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)

class Player(models.Model):
    info = models.ForeignKey(PlayerInfo, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    record = models.ForeignKey(Record, on_delete=models.CASCADE)

class Match(models.Model):
    date_time = models.DateTimeField()
    team_1 = models.ForeignKey(Team, related_name='home_team', on_delete=models.CASCADE)
    team_2 = models.ForeignKey(Team, related_name='away_team', on_delete=models.CASCADE)
    is_team = models.BooleanField(default=True)
    tournament = models.ForeignKey('Tournament', on_delete=models.CASCADE)

class Tournament(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    active = models.BooleanField(default=True)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
