# Generated by Django 3.2.3 on 2021-06-09 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0002_rename_scores_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='Score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
