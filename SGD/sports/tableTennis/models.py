from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from ...core_application import models as core_models


class TableTennisPlayerInfo(core_models.PlayerInfo):
    # attributes to override
    class Meta:
        app_label = 'tableTennis'
        verbose_name = 'Table Tennis Player Info'

    def __str__(self):
        return self.name
