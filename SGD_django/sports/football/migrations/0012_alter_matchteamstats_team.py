# Generated by Django 5.0.6 on 2024-07-30 22:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0011_matchstats_is_draw_matchstats_winner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchteamstats',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='football.team'),
        ),
    ]