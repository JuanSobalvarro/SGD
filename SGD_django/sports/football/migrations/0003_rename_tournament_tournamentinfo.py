# Generated by Django 5.0.6 on 2024-07-25 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0002_team_teamstats_tournament_player_team_stats'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tournament',
            new_name='TournamentInfo',
        ),
    ]