# Generated by Django 5.0.6 on 2024-07-31 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0013_alter_matchstats_team_1_stats_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matchparenting',
            old_name='match',
            new_name='child_match',
        ),
    ]