
class MatchTeamFootballStats(MatchTeamStats):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.home_team = kwargs['home_team']
        self.away_team = kwargs['away_team']

        self.home_score = kwargs['home_score']

        self.away_score = kwargs['away_score']

        self.home_goals = kwargs['home_goals']

        self.away_goals = kwargs['away_goals']