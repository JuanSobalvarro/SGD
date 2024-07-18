from django.test import TestCase
from . import models as models


class TableTennisTestCase(TestCase):

    def setUp(self):
        self.playerInfo = models.PlayerInfo.objects.create(name="Juan", email="juan.sobalvarro@est.ulsa.edu.ni")
        self.record = models.Record.objects.create()
        self.player = models.Player.objects.create(info=self.playerInfo, record=self.record)

    def test_printPlayer(self):
        self.assertEqual(self.player.info.name, "Juan")
        self.assertEqual(self.player.info.email, "juan.sobalvarro@est.ulsa.edu.ni")
