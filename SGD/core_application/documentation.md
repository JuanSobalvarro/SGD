# Core Application Models Documentation

## Introduction

This documentation provides an overview of how to implement and extend the core application models to create sport-specific models. The core application defines abstract base classes, which can be inherited to create concrete models for specific sports.

## Abstract Base Models

The core application provides the following abstract base models:

- PlayerInfo
- TeamStats
- Team
- Record
- Player
- Tournament
- MatchTeamStats
- MatchStats
- Match
- News

These abstract models are defined with `abstract = True` in their Meta class and do not create tables in the database. Instead, they provide common fields and methods that can be reused by concrete models.

## Creating Sport-Specific Models

To create sport-specific models, follow these steps:

1. **Create a New App**: Create a new Django app for the specific sport (e.g., `table_tennis`).

2. **Define Concrete Models**: In the new app's `models.py` file, define concrete models that inherit from the abstract base models. Do not set `abstract = True` in the Meta class of these concrete models.

### Example: Table Tennis Models

python
from django.db import models
from core_application.models import PlayerInfo, TeamStats, Team, Record, Player, Tournament, MatchTeamStats, MatchStats, Match, News

class TableTennisPlayerInfo(PlayerInfo):
    """
    Table Tennis player information.
    """
    pass

class TableTennisDuoStats(TeamStats):
    """
    Table Tennis team stats.
    """
    pass

...

This documentation file provides clear instructions on how to implement and use the models from the core application. You can expand it further based on your project's specific needs.

For more details, refer to the Django documentation on abstract base classes.