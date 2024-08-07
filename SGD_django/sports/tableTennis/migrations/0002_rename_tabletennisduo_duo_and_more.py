# Generated by Django 5.0.6 on 2024-06-22 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('tableTennis', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TableTennisDuo',
            new_name='Duo',
        ),
        migrations.RenameModel(
            old_name='TableTennisDuoStats',
            new_name='DuoStats',
        ),
        migrations.RenameModel(
            old_name='TableTennisMatch',
            new_name='Match',
        ),
        migrations.RenameModel(
            old_name='TableTennisMatchDuoStats',
            new_name='MatchDuoStats',
        ),
        migrations.RenameModel(
            old_name='TableTennisMatchSingleStats',
            new_name='MatchSingleStats',
        ),
        migrations.RenameModel(
            old_name='TableTennisMatchStats',
            new_name='MatchStats',
        ),
        migrations.RenameModel(
            old_name='TableTennisPlayer',
            new_name='Player',
        ),
        migrations.RenameModel(
            old_name='TableTennisPlayerInfo',
            new_name='PlayerInfo',
        ),
        migrations.RenameModel(
            old_name='TableTennisRecord',
            new_name='Record',
        ),
        migrations.RenameModel(
            old_name='TableTennisTournament',
            new_name='Tournament',
        ),
    ]
