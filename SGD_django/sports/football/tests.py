# sports/football/tests.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import PlayerInfo, Record, TeamStats, Team, Player, TournamentInfo, MatchTeamStats, MatchStats, Match
from .tournament_manager.manager import TournamentManager
from datetime import datetime


class TournamentManagerTestCase(TestCase):
    def setUp(self):
        self.team1 = Team.objects.create(name="Team 1")
        self.team2 = Team.objects.create(name="Team 2")
        self.team3 = Team.objects.create(name="Team 3")
        self.team4 = Team.objects.create(name="Team 4")
        self.tournament = TournamentInfo.objects.create(name="Test Tournament", date=datetime.now())

    def test_calculateRounds(self):
        self.assertEqual(TournamentManager.calculateRounds(2), 1)
        self.assertEqual(TournamentManager.calculateRounds(4), 2)
        self.assertEqual(TournamentManager.calculateRounds(8), 3)

    def test_singleEliminationTournament_creation(self):
        teams = [self.team1, self.team2, self.team3, self.team4]
        matches = TournamentManager.createSingleEliminationTournament(self.tournament, teams)

        self.assertEqual(len(matches), 3)  # 3 rounds (1st round: 2 matches, 2nd round: 1 match, 3rd round: final match)
        self.assertEqual(self.tournament.rounds, 2)  # 4 teams -> log2(4) = 2 rounds

        # Check the matches
        first_round = matches[0]
        second_round = matches[1]

        self.assertEqual(len(first_round), 2)  # 2 matches in the first round
        self.assertEqual(len(second_round), 1)  # 1 match in the second round

        # Check teams in the first round
        self.assertIn(first_round[0].team1, teams)
        self.assertIn(first_round[0].team2, teams)
        self.assertIn(first_round[1].team1, teams)
        self.assertIn(first_round[1].team2, teams)

    def test_tournamentBracket_view(self):
        teams = [self.team1, self.team2, self.team3, self.team4]
        TournamentManager.createSingleEliminationTournament(self.tournament, teams)
        bracket = TournamentManager.getBracket(self.tournament)

        self.assertTrue(len(bracket) > 0)
        self.assertIn(1, bracket)
        self.assertIn(2, bracket)

        # Verify structure of the bracket
        self.assertEqual(len(bracket[1]), 2)  # 2 matches in the first round
        self.assertEqual(len(bracket[2]), 1)  # 1 match in the second round


class MatchModelTestCase(TestCase):
    def setUp(self):
        self.team1 = Team.objects.create(name="Team 1")
        self.team2 = Team.objects.create(name="Team 2")
        self.team3 = Team.objects.create(name="Team 3")
        self.team4 = Team.objects.create(name="Team 4")
        self.tournament = TournamentInfo.objects.create(name="Test Tournament", date=datetime.now(), rounds=2)
        self.match_stats1 = MatchStats.objects.create()
        self.match_stats2 = MatchStats.objects.create()

    def test_match_self_referential_relationship(self):
        match1 = Match.objects.create(
            date_time=datetime.now(),
            team_1=self.team1,
            team_2=self.team2,
            match_stats=self.match_stats1,
            tournament_info=self.tournament,
            round=1
        )

        match2 = Match.objects.create(
            date_time=datetime.now(),
            team_1=self.team3,
            team_2=self.team4,
            match_stats=self.match_stats2,
            tournament_info=self.tournament,
            round=1
        )

        final_match = Match.objects.create(
            date_time=datetime.now(),
            team_1=self.team1,
            team_2=self.team3,
            match_stats=self.match_stats1,
            tournament_info=self.tournament,
            round=2,
            parent_match_team1=match1,
            parent_match_team2=match2
        )

        self.assertEqual(final_match.parent_match_team1, match1)
        self.assertEqual(final_match.parent_match_team2, match2)
        self.assertEqual(match1.child_matches_team1.first(), final_match)
        self.assertEqual(match2.child_matches_team2.first(), final_match)


class FootballAPITestCase(APITestCase):
    def setUp(self):
        self.player_info = PlayerInfo.objects.create(name="John Doe", email="john@example.com", date_of_birth="1990-01-01")
        self.record = Record.objects.create(wins=10, losses=5, draws=2, goals=20)
        self.team_stats = TeamStats.objects.create(wins=10, losses=5, draws=2, average_goals_per_game=2.5)
        self.team = Team.objects.create(name="Team A", stats=self.team_stats)
        self.player = Player.objects.create(info=self.player_info, record=self.record, team=self.team)
        self.tournament = TournamentInfo.objects.create(name="Tournament 1", date="2023-07-23", type=TournamentInfo.LEAGUE, rounds=3)
        self.match_team_stats1 = MatchTeamStats.objects.create(winner=True, goals=3)
        self.match_team_stats2 = MatchTeamStats.objects.create(winner=False, goals=1)
        self.match_stats = MatchStats.objects.create(team_1_stats=self.match_team_stats1, team_2_stats=self.match_team_stats2)
        self.match = Match.objects.create(date_time="2023-07-23T10:00:00Z", team_1=self.team, team_2=self.team, match_stats=self.match_stats, tournament_info=self.tournament, round=1, winner=self.team)

    def test_create_player_info(self):
        url = reverse('playerinfo-list')
        data = {"name": "Jane Doe", "email": "jane@example.com", "date_of_birth": "1995-05-15"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_record(self):
        url = reverse('record-list')
        data = {"wins": 8, "losses": 2, "draws": 1, "goals": 15}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_team_stats(self):
        url = reverse('teamstats-list')
        data = {"wins": 5, "losses": 3, "draws": 2, "average_goals_per_game": 1.8}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_team(self):
        url = reverse('team-list')
        data = {"name": "Team B", "stats": self.team_stats.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_player(self):
        url = reverse('player-list')
        data = {"info": self.player_info.id, "record": self.record.id, "team": self.team.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_tournament(self):
        url = reverse('tournamentinfo-list')
        data = {"name": "Tournament 2", "date": "2024-07-23", "type": TournamentInfo.CHAMPIONSHIP, "rounds": 4}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_match_team_stats(self):
        url = reverse('matchteamstats-list')
        data = {"winner": True, "goals": 2}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_match_stats(self):
        url = reverse('matchstats-list')
        data = {"team_1_stats": self.match_team_stats1.id, "team_2_stats": self.match_team_stats2.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_match(self):
        url = reverse('match-list')
        data = {
            "date_time": "2024-07-23T10:00:00Z",
            "team_1": self.team.id,
            "team_2": self.team.id,
            "match_stats": self.match_stats.id,
            "tournament_info": self.tournament.id,
            "round": 1,
            "winner": self.team.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)