# sports/football/serializers.py
from rest_framework import serializers
from .models import PlayerInfo, Record, TeamStats, Team, Player, TournamentInfo, MatchTeamStats, MatchStats, Match


class PlayerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerInfo
        fields = '__all__'


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'


class TeamStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamStats
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    stats = TeamStatsSerializer()

    class Meta:
        model = Team
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    info = PlayerInfoSerializer()
    record = RecordSerializer()

    class Meta:
        model = Player
        fields = '__all__'


class TournamentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentInfo
        fields = '__all__'


class MatchTeamStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchTeamStats
        fields = '__all__'


class MatchStatsSerializer(serializers.ModelSerializer):
    team_1_stats = MatchTeamStatsSerializer()
    team_2_stats = MatchTeamStatsSerializer()

    class Meta:
        model = MatchStats
        fields = '__all__'


class MatchSerializer(serializers.ModelSerializer):
    team_1 = TeamSerializer()
    team_2 = TeamSerializer()
    match_stats = MatchStatsSerializer()
    tournament_info = TournamentInfoSerializer()

    class Meta:
        model = Match
        fields = '__all__'
