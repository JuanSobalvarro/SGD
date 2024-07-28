"""
Table tennis Serializer module for the api rest framework
"""
from rest_framework import serializers
from .models import PlayerInfo, Record, Player, DuoStats, Duo, Tournament, MatchDuoStats, MatchSingleStats, MatchStats, Match


class PlayerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerInfo
        fields = '__all__'


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    info = PlayerInfoSerializer()
    record = RecordSerializer()

    class Meta:
        model = Player
        fields = '__all__'


class DuoStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DuoStats
        fields = '__all__'


class DuoSerializer(serializers.ModelSerializer):
    player1 = PlayerSerializer()
    player2 = PlayerSerializer()
    stats = DuoStatsSerializer()

    class Meta:
        model = Duo
        fields = '__all__'


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = '__all__'


class MatchDuoStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchDuoStats
        fields = '__all__'


class MatchSingleStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchSingleStats
        fields = '__all__'


class MatchStatsSerializer(serializers.ModelSerializer):
    team_1_stats = serializers.SerializerMethodField()
    team_2_stats = serializers.SerializerMethodField()

    class Meta:
        model = MatchStats
        fields = '__all__'

    def get_team_1_stats(self, obj):
        if isinstance(obj.team_1_stats, MatchDuoStats):
            return MatchDuoStatsSerializer(obj.team_1_stats).data
        elif isinstance(obj.team_1_stats, MatchSingleStats):
            return MatchSingleStatsSerializer(obj.team_1_stats).data

    def get_team_2_stats(self, obj):
        if isinstance(obj.team_2_stats, MatchDuoStats):
            return MatchDuoStatsSerializer(obj.team_2_stats).data
        elif isinstance(obj.team_2_stats, MatchSingleStats):
            return MatchSingleStatsSerializer(obj.team_2_stats).data


class MatchSerializer(serializers.ModelSerializer):
    match_stats = MatchStatsSerializer()
    tournament = TournamentSerializer()

    class Meta:
        model = Match
        fields = '__all__'
