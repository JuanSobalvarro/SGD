# Generated by Django 5.0.6 on 2024-07-24 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tableTennis', '0005_remove_duostats_matches_played'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duo',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
