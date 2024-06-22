# Generated by Django 5.0.6 on 2024-06-22 22:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableTennisDuoStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wins', models.IntegerField(default=0)),
                ('losses', models.IntegerField(default=0)),
                ('draws', models.IntegerField(default=0)),
                ('average_points_per_game', models.FloatField(default=0)),
                ('games_played', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TableTennisMatchDuoStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winner', models.BooleanField(default=False)),
                ('player1_average_points_per_game', models.FloatField(default=0)),
                ('player2_average_points_per_game', models.FloatField(default=0)),
                ('games_played', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TableTennisMatchSingleStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winner', models.BooleanField(default=False)),
                ('average_points_per_game', models.FloatField(default=0)),
                ('games_played', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TableTennisPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TableTennisPlayerInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TableTennisRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wins', models.IntegerField(default=0)),
                ('losses', models.IntegerField(default=0)),
                ('draws', models.IntegerField(default=0)),
                ('attack_efficiency', models.FloatField(default=0)),
                ('serving_efficiency', models.FloatField(default=0)),
                ('defense_efficiency', models.FloatField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TableTennisTournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('active', models.BooleanField(default=True)),
                ('type', models.CharField(choices=[('S', 'Singles'), ('D', 'Doubles')], default='S', max_length=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TableTennisMatchStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id_team_1', models.PositiveIntegerField()),
                ('object_id_team_2', models.PositiveIntegerField()),
                ('content_type_team_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_1_stats_content_type', to='contenttypes.contenttype')),
                ('content_type_team_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_2_stats_content_type', to='contenttypes.contenttype')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TableTennisDuo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('stats', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tableTennis.tabletennisduostats')),
                ('player1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player1', to='tableTennis.tabletennisplayer')),
                ('player2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player2', to='tableTennis.tabletennisplayer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='tabletennisplayer',
            name='info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tableTennis.tabletennisplayerinfo'),
        ),
        migrations.AddField(
            model_name='tabletennisplayer',
            name='record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tableTennis.tabletennisrecord'),
        ),
        migrations.CreateModel(
            name='TableTennisMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('is_team', models.BooleanField(default=True)),
                ('object_id_team_1', models.PositiveIntegerField()),
                ('object_id_team_2', models.PositiveIntegerField()),
                ('content_type_team_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_1_content_type', to='contenttypes.contenttype')),
                ('content_type_team_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_2_content_type', to='contenttypes.contenttype')),
                ('match_stats', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tableTennis.tabletennismatchstats')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tableTennis.tabletennistournament')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
