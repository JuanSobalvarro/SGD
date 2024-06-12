from typing import Any
from django.db import models
from core_application import models as core_models


class TableTennisRecord(core_models.Record):
    """
    Record for the player    
    """
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class TableTennisTeamStats(core_models.TeamStats):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)        


class TableTennisTeam(core_models.Team):
    """
    Model for table tennis team
    """
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.stats = models.ForeignKey(TableTennisTeamStats, on_delete=models.CASCADE)


class TableTennisPlayer(core_models.Player):
    """
    Instance for table tennis player
    """
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.record = models.ForeignKey(TableTennisRecord, on_delete=models.CASCADE)