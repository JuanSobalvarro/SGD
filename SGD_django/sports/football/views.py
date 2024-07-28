# sports/football/views.py
from rest_framework import viewsets
from .models import PlayerInfo, Record, TeamStats, Team, Player, TournamentInfo, MatchTeamStats, MatchStats, Match
from .serializers import PlayerInfoSerializer, RecordSerializer, TeamStatsSerializer, TeamSerializer, PlayerSerializer, \
    TournamentInfoSerializer, MatchTeamStatsSerializer, MatchStatsSerializer, MatchSerializer


class PlayerInfoViewSet(viewsets.ModelViewSet):
    queryset = PlayerInfo.objects.all()
    serializer_class = PlayerInfoSerializer


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class TeamStatsViewSet(viewsets.ModelViewSet):
    queryset = TeamStats.objects.all()
    serializer_class = TeamStatsSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class TournamentInfoViewSet(viewsets.ModelViewSet):
    queryset = TournamentInfo.objects.all()
    serializer_class = TournamentInfoSerializer


class MatchTeamStatsViewSet(viewsets.ModelViewSet):
    queryset = MatchTeamStats.objects.all()
    serializer_class = MatchTeamStatsSerializer


class MatchStatsViewSet(viewsets.ModelViewSet):
    queryset = MatchStats.objects.all()
    serializer_class = MatchStatsSerializer


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
