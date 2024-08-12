# football/tournament_manager/manager.py
from django.db import models
from datetime import datetime
import math
import random
from ..models import (
    TournamentInfo,
    Match,
    Team,
    MatchStats,
    TeamStats,
    MatchTeamStats,
    MatchParenting,
)


class TournamentManager:
    @staticmethod
    def calculateRounds(number_of_teams):
        if number_of_teams < 2:
            raise ValueError("The number of teams must be at least 2.")
        return math.ceil(math.log2(number_of_teams))

    @staticmethod
    def createSingleEliminationTournament(tournament: TournamentInfo, teams: list[Team]) -> list[list[Match]]:
        """
        Static Method that creates a single elimination tournament from a list of teams, and
        returns a list of matches created.

        :param TournamentInfo tournament: The tournament to be associated with this elimination tournament
        :param list[Team] teams: List of teams to assign elimination tournament to
        :return: A list of matches created.
        """

        if len(teams) < 2:
            raise ValueError("Tournament must have at least two teams competing.")

        random.shuffle(teams)

        tournament.rounds = TournamentManager.calculateRounds(len(teams))
        tournament.save()

        matches: list[list[Match]] = []
        current_round_teams = teams
        prev_round_matches: list[Match] = []

        for round_number in range(1, tournament.rounds + 1):
            round_matches = []
            next_round_teams = []

            if len(current_round_teams) % 2 != 0:
                # Randomly select one team to pass to the next round
                random_team = random.choice(current_round_teams)
                next_round_teams.append(random_team)
                current_round_teams.remove(random_team)

            for i in range(0, len(current_round_teams), 2):
                match = Match(
                    date_time=datetime(year=2024, month=1, day=1),
                    team_1=current_round_teams[i],
                    team_2=current_round_teams[i + 1],
                    match_stats=TournamentManager.createMatchStats(current_round_teams[i], current_round_teams[i + 1]),
                    tournament_info=tournament,
                    round=round_number,
                )
                match.save()
                round_matches.append(match)
                print(f"Created match {match.id} between {match.team_1.name if match.team_1 else 'TBD'} "
                      f"and {match.team_2.name if match.team_2 else 'TBD'} ")

                # Placeholder for the next round
                next_round_teams.append(None)

            matches.append(round_matches)

            if round_number > 1:
                for i in range(len(round_matches)):
                    parent_match_index = 2 * i
                    if parent_match_index < len(prev_round_matches):
                        parenting = MatchParenting(child_match=round_matches[i],
                                                   parent_match=prev_round_matches[parent_match_index],
                                                   team_number=1)
                        parenting.save()
                        print(f"Created parenting for child match {round_matches[i].id} "
                              f"from parent match {prev_round_matches[parent_match_index].id} (team 1)")
                    if parent_match_index + 1 < len(prev_round_matches):
                        parenting = MatchParenting(child_match=round_matches[i],
                                                   parent_match=prev_round_matches[parent_match_index + 1],
                                                   team_number=2)
                        parenting.save()
                        print(f"Created parenting for child match {round_matches[i].id} "
                              f"from parent match {prev_round_matches[parent_match_index + 1].id} (team 2)")

            prev_round_matches = round_matches
            current_round_teams = next_round_teams

        return matches

    @staticmethod
    def getBracket(tournament: TournamentInfo) -> dict[int, list[Match]]:
        """
        From a given tournament looks for all the matches in that tournament
        and returns a dictionary of the round and list of matches.
        REMEMBER: BRACKET IS A DICTIONARY FROM ROUND 1 TO ROUND X(LOG2(NUMBEROFTEAMS))
        THE FIRST MATCH IS BRACKETS[1][0] AND THE SECOND MATCH IS BRACKETS[1][1]...

        :param TournamentInfo tournament: The tournament which bracket will be generated
        :return: A dictionary of the round and list of matches.
        """
        matches = Match.objects.filter(tournament_info=tournament).order_by('round', 'id')

        bracket = {}
        for match in matches:
            if match.round not in bracket:
                bracket[match.round] = []
            bracket[match.round].append(match)

        return bracket

    @staticmethod
    def createMatchStats(team1: Team, team2: Team) -> MatchStats:

        match_stats = MatchStats(winner=None,
                                 is_draw=False)
        match_stats.createTeamMatchStats(team1, 1)
        match_stats.createTeamMatchStats(team2, 2)

        match_stats.save()

        return match_stats

    @staticmethod
    def updateMatchWinner(match: Match, winning_team: Team):
        """
        Updates a match winner

        :param Match match: The match to update
        :param Team winning_team: The team that won the match.
        """
        if winning_team is None:
            raise ValueError("Winning team cannot be None.")

        if winning_team is not match.team_1 and winning_team is not match.team_2:
            raise ValueError("The winner team must be a team of the match")

        match.match_stats.winner = winning_team
        match.match_stats.save()
        match.save()

        # Update child matches
        parenting_relationships = MatchParenting.objects.filter(parent_match=match)
        if not parenting_relationships.exists():
            print(f"No parenting relationships found for match {match.pk}")

        for parenting in parenting_relationships:
            try:
                child_match = parenting.child_match
                if parenting.team_number == 1:
                    child_match.match_stats.team_1 = child_match.addTeam(winning_team, 1)
                elif parenting.team_number == 2:
                    child_match.match_stats.team_2 = child_match.addTeam(winning_team, 2)
                child_match.save()
            except Exception as e:
                print(f"Error updating child match {parenting.child_match.pk} for parent match {match.pk}: {str(e)}")
            else:
                print(f"Successfully updated child match {child_match.pk} with winning team {winning_team.name}. "
                      f"Now: {child_match}")

        # Force refresh the match to get the latest data from the database
        match.refresh_from_db()
        match.match_stats.refresh_from_db()
        # Refresh the child matches as well if needed
        parenting_relationships = MatchParenting.objects.filter(parent_match=match)
        for parenting in parenting_relationships:
            parenting.child_match.refresh_from_db()

        print(f"Match {match.pk} updated with winner {winning_team.name}")

    @staticmethod
    def printBracket(tournament: TournamentInfo):
        """
        Prints the bracket for the given tournament in a readable format.

        :param TournamentInfo tournament: The tournament to be printed.
        """
        bracket = TournamentManager.getBracket(tournament)

        for round_number, matches in bracket.items():
            print(f"Round {round_number}:")
            for match in matches:
                team_1_name = match.team_1.name if match.team_1 else TournamentManager.getParentMatchTeam(match, 1)
                team_2_name = match.team_2.name if match.team_2 else TournamentManager.getParentMatchTeam(match, 2)
                print(f"  Match {match.id}: {team_1_name} vs {team_2_name}")
            print()

    @staticmethod
    def getParentMatchTeam(match: Match, team_number: int) -> str:
        """
        Retrieves the team from the parent match that is supposed to occupy a position in the current match.

        :param Match match: The current match.
        :param int team_number: The team position (1 or 2).
        :return: The description of the team (either the actual team name or a placeholder).
        """
        try:
            parent_match_relationship = MatchParenting.objects.get(child_match=match, team_number=team_number)
            parent_match = parent_match_relationship.parent_match

            if parent_match.match_stats and parent_match.match_stats.winner:
                return parent_match.match_stats.winner.name
            return f"Winner of match {parent_match.id}"
        except MatchParenting.DoesNotExist:
            return "TBD"



