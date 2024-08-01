# sports/football/tests.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import (
    PlayerInfo,
    Record,
    TeamStats,
    Team,
    Player,
    TournamentInfo,
    MatchTeamStats,
    MatchStats,
    Match,
    MatchParenting,
)
from .tournament_manager.manager import TournamentManager
from datetime import datetime
import faker


class TeamTestCase(TestCase):
    def setUp(self):
        self.fake = faker.Faker()

    @staticmethod
    def createTeam(name: str, team_stats: TeamStats) -> Team:
        team = Team(name=name, stats=team_stats)
        team.save()

        return team

    @staticmethod
    def createTeamStats(wins: int, losses: int, draws: int, average_goals: float) -> TeamStats:
        team_stats = TeamStats(wins=wins, losses=losses, draws=draws, average_goals_per_game=average_goals)
        team_stats.save()

        return team_stats


class PlayerTestCase(TestCase):
    def setUp(self):
        self.player = self.createPlayer(info=self.createInfo(name="uwu", email="uwu@kkck.com", date=datetime.now()),
                                        record=self.createRecord(wins=10, losses=10, draws=10, goals=10),
                                        team=TeamTestCase.createTeam(name="los kks",
                                                                     team_stats=TeamTestCase.createTeamStats(wins=10,
                                                                                                             losses=10,
                                                                                                             draws=10,
                                                                                                             average_goals=1.5)))

    @staticmethod
    def createPlayer(info: PlayerInfo, record: Record, team: Team) -> Player:
        player = Player(info=info, record=record, team=team)
        player.save()

        return player

    @staticmethod
    def createInfo(name: str, email: str, date: datetime) -> PlayerInfo:
        info = PlayerInfo(name=name, email=email, date_of_birth=date)
        info.save()

        return info

    @staticmethod
    def createRecord(wins: int, losses: int, draws: int, goals: int) -> Record:
        record = Record(wins=wins, losses=losses, draws=draws, goals=goals)
        record.save()

        return record

    def test_player_creation(self):
        player = Player.objects.get(pk=self.player.pk)
        self.assertEqual(player.info.name, "uwu")
        self.assertEqual(player.info.email, "uwu@kkck.com")
        self.assertEqual(player.record.wins, 10)
        self.assertEqual(player.team.name, "los kks")
        self.assertEqual(player.team.stats.wins, 10)
        self.assertEqual(player.team.stats.average_goals_per_game, 1.5)


class TournamentManagerTestCase(TestCase):
    def setUp(self):
        number_of_teams = 10
        self.teams = [self.createTeam(f"Team {i}") for i in range(number_of_teams)]
        self.tournament = TournamentInfo(name="Test Tournament", date=datetime.now(), active=True)
        self.tournament.save()

    @staticmethod
    def createTeam(name: str):
        team_stats = TeamStats(wins=0, losses=0, draws=0, average_goals_per_game=0.0)
        team_stats.save()
        team = Team(name=name, stats=team_stats)
        team.save()
        return team

    def test_create_single_elimination_tournament(self):
        matches = TournamentManager.createSingleEliminationTournament(self.tournament, self.teams)
        self.assertEqual(len(matches), self.tournament.rounds)
        self.assertEqual(self.tournament.rounds, 4)  # 10 teams require 4 rounds

        # # Verify the match creation
        # for round_matches in matches:
        #     print(round_matches)

    def test_tournamentBracket_view(self):
        matches = TournamentManager.createSingleEliminationTournament(self.tournament, self.teams)
        bracket = TournamentManager.getBracket(self.tournament)

        # TournamentManager.printBracket(self.tournament)

        # 10 teams
        self.assertTrue(len(bracket) > 0)

        # check if there is 1, 2 and 3 rounds values in bracket
        self.assertIn(1, bracket)
        self.assertIn(2, bracket)
        self.assertIn(3, bracket)

        # Verify structure of the bracket
        self.assertEqual(len(bracket[1]), 5)
        self.assertEqual(len(bracket[2]), 2)
        self.assertEqual(len(bracket[3]), 1)

    def test_match_winners(self):
        matches = TournamentManager.createSingleEliminationTournament(self.tournament, self.teams)
        bracket = TournamentManager.getBracket(self.tournament)

        # tournament bracket should be empty
        self.assertEqual(bracket[2][0].team_1, None)
        self.assertEqual(bracket[2][0].team_2, None)
        self.assertEqual(bracket[2][1].team_1, None)
        self.assertEqual(bracket[2][1].team_2, None)

        self.assertEqual(bracket[3][0].team_1, None)
        self.assertEqual(bracket[3][0].team_2, None)

        self.assertEqual(bracket[4][0].team_1, None)
        self.assertEqual(bracket[4][0].team_2, None)

        print("First bracket")
        TournamentManager.printBracket(self.tournament)

        # Set winners for the first round
        TournamentManager.updateMatchWinner(bracket[1][0], bracket[1][0].team_1)
        TournamentManager.updateMatchWinner(bracket[1][1], bracket[1][1].team_2)
        TournamentManager.updateMatchWinner(bracket[1][2], bracket[1][2].team_1)
        TournamentManager.updateMatchWinner(bracket[1][3], bracket[1][3].team_1)
        TournamentManager.updateMatchWinner(bracket[1][4], bracket[1][4].team_2)

        # Re-fetch the bracket to ensure the latest data is available
        bracket = TournamentManager.getBracket(self.tournament)
        print(bracket)

        print("Second bracket")
        TournamentManager.printBracket(self.tournament)

        parenting1 = MatchParenting.objects.get(child_match=bracket[2][0], team_number=1)
        parenting2 = MatchParenting.objects.get(child_match=bracket[2][0], team_number=2)
        print(f"Match Ah: {bracket[2][0]}")
        self.assertEqual(bracket[2][0].team_1, parenting1.parent_match.match_stats.winner)
        self.assertEqual(bracket[2][0].team_2, parenting2.parent_match.match_stats.winner)

        self.assertEqual(bracket[3][0].team_1, None)
        self.assertEqual(bracket[3][0].team_2, None)

        # Set winners for the second round
        TournamentManager.updateMatchWinner(bracket[2][0], bracket[2][0].team_1)
        TournamentManager.updateMatchWinner(bracket[2][1], bracket[2][1].team_2)

        # Re-fetch the bracket to ensure the latest data is available
        bracket = TournamentManager.getBracket(self.tournament)

        print("Third bracket")
        TournamentManager.printBracket(self.tournament)

        # Set winner for the third round
        TournamentManager.updateMatchWinner(bracket[3][0], bracket[3][0].team_1)

        # Re-fetch the bracket to ensure the latest data is available
        bracket = TournamentManager.getBracket(self.tournament)

        # Final match should not have "TBD" and should have the winning team from the previous round
        final_match = bracket[4][0]
        self.assertIsNotNone(final_match.team_1)
        self.assertNotEqual(final_match.team_1, "TBD")
        print(f"Final match: {final_match}")

