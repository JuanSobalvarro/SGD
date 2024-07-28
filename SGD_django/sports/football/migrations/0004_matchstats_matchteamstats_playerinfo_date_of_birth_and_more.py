# Generated by Django 5.0.6 on 2024-07-28 01:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0003_rename_tournament_tournamentinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MatchTeamStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goals', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='playerinfo',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tournamentinfo',
            name='rounds',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('round', models.IntegerField(default=0)),
                ('parent_match_team1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_matches_team1', to='football.match')),
                ('parent_match_team2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_matches_team2', to='football.match')),
                ('team_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches_as_team1', to='football.team')),
                ('team_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches_as_team2', to='football.team')),
                ('tournament_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.tournamentinfo')),
                ('winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.team')),
                ('match_stats', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football.matchstats')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='matchstats',
            name='team_1_stats',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stats_team1', to='football.matchteamstats'),
        ),
        migrations.AddField(
            model_name='matchstats',
            name='team_2_stats',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stats_team2', to='football.matchteamstats'),
        ),
    ]
