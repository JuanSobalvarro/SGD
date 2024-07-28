# football/tournament_manager/manager.py
from django.db import models
from datetime import datetime
import math
import random
from ..models import TournamentInfo, Match, Team


class TournamentManager:
    @staticmethod
    def calculateRounds(number_of_teams):
        if number_of_teams < 2:
            raise ValueError("The number of teams must be at least 2.")
        return math.ceil(math.log2(number_of_teams))

    @staticmethod
    def createSingleEliminationTournament(tournament: TournamentInfo, teams: list[Team]):
        teams = list(teams)
        random.shuffle(teams)

        tournament.rounds = TournamentManager.calculateRounds(len(teams))
        tournament.save()

        matches = []
        current_round_teams = teams
        for round_number in range(1, tournament.rounds + 1):
            round_matches = []
            next_round_teams = []
            for i in range(0, len(current_round_teams), 2):
                if i + 1 < len(current_round_teams):
                    match = Match.objects.create(
                        tournament=tournament,
                        round=round_number,
                        team1=current_round_teams[i],
                        team2=current_round_teams[i + 1],
                        date=datetime.now()
                    )
                    round_matches.append(match)
                    next_round_teams.append(match)
                else:
                    next_round_teams.append(current_round_teams[i])  # Odd team out gets a bye
            matches.append(round_matches)
            current_round_teams = next_round_teams

        # Link parent matches for rounds greater than 1
        for round_number in range(2, tournament.rounds + 1):
            prev_round_matches = matches[round_number - 2]
            current_round_matches = matches[round_number - 1]
            for i in range(0, len(current_round_matches)):
                current_round_matches[i].parent_match1 = prev_round_matches[2 * i]
                if 2 * i + 1 < len(prev_round_matches):
                    current_round_matches[i].parent_match2 = prev_round_matches[2 * i + 1]
                current_round_matches[i].save()

        return matches

    @staticmethod
    def getBracket(tournament: TournamentInfo):
        matches = Match.objects.filter(tournament=tournament).order_by('round', 'id')

        bracket = {}
        for match in matches:
            if match.round not in bracket:
                bracket[match.round] = []
            bracket[match.round].append(match)

        return bracket
