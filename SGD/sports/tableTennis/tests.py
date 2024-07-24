from django.test import TestCase
from . import models as models
from .serializers import (
    PlayerInfoSerializer,
    RecordSerializer,
    PlayerSerializer,
    DuoStatsSerializer,
    DuoSerializer,
    TournamentSerializer,
    MatchSingleStatsSerializer,
    MatchStatsSerializer,
    MatchSerializer
)


class TableTennisTestCase(TestCase):

    def setUp(self):
        # player1 setup
        self.playerInfo1 = models.PlayerInfo(name="Juan",
                                             email="juan.sobalvarro@est.ulsa.edu.ni")
        self.playerInfo1.save()

        self.record1 = models.Record(attack_efficiency=75,
                                   serving_efficiency=80,
                                   defense_efficiency=85)
        self.record1.save()

        self.player1 = models.Player(info=self.playerInfo1,
                                   record=self.record1)
        self.player1.save()

        # player2 setup
        self.playerInfo2 = models.PlayerInfo(name="KK",
                                            email="kk.sobalvarro@est.ulsa.edu.ni")
        self.playerInfo2.save()

        self.record2 = models.Record(attack_efficiency=23,
                                    serving_efficiency=90,
                                    defense_efficiency=54)
        self.record2.save()

        self.player2 = models.Player(info=self.playerInfo2,
                                    record=self.record2)
        self.player2.save()

        # duo setup
        self.duoStats = models.DuoStats(wins=10,
                                        losses=10,
                                        draws=10,
                                        average_points_per_game=8.9)
        self.duoStats.save()

        self.duo = models.Duo(name="Los Kks",
                              player1=self.player1,
                              player2=self.player2,
                              stats=self.duoStats)
        self.duo.save()

    def test_player_info_serializer(self):
        serializer = PlayerInfoSerializer(self.playerInfo1)
        data = serializer.data
        self.assertEqual(data['name'], "Juan")
        self.assertEqual(data['email'], "juan.sobalvarro@est.ulsa.edu.ni")

    def test_record_serializer(self):
        serializer = RecordSerializer(self.record1)
        data = serializer.data
        self.assertEqual(data['attack_efficiency'], 75)
        self.assertEqual(data['serving_efficiency'], 80)
        self.assertEqual(data['defense_efficiency'], 85)

    def test_player_serializer(self):
        serializer = PlayerSerializer(self.player1)
        data = serializer.data
        self.assertEqual(data['info']['name'], "Juan")
        self.assertEqual(data['info']['email'], "juan.sobalvarro@est.ulsa.edu.ni")
        self.assertEqual(data['record']['attack_efficiency'], 75)
        self.assertEqual(data['record']['serving_efficiency'], 80)
        self.assertEqual(data['record']['defense_efficiency'], 85)

    def test_duo_stats_serializer(self):
        serializer = DuoStatsSerializer(self.duoStats)
        data = serializer.data
        self.assertEqual(data['wins'], 10)
        self.assertEqual(data['losses'], 10)
        self.assertEqual(data['draws'], 10)
        self.assertEqual(data['average_points_per_game'], 8.9)

    def test_duo_serializer(self):
        serializer = DuoSerializer(self.duo)
        data = serializer.data
        self.assertEqual(data['name'], "Los Kks")
        self.assertEqual(data['player1']['info']['name'], "Juan")
        self.assertEqual(data['player2']['info']['name'], "KK")
