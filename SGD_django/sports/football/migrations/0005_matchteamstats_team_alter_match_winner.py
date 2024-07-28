# Generated by Django 5.0.6 on 2024-07-28 06:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0004_matchstats_matchteamstats_playerinfo_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchteamstats',
            name='team',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='football.team'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='football.team'),
        ),
    ]
