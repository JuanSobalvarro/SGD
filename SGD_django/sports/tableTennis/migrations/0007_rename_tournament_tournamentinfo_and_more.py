# Generated by Django 5.0.6 on 2024-07-25 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tableTennis', '0006_alter_duo_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tournament',
            new_name='TournamentInfo',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='tournament',
            new_name='tournament_info',
        ),
    ]