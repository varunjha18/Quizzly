# Generated by Django 3.2.3 on 2021-06-09 14:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0016_auto_20210609_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 9, 20, 17, 9, 265524)),
        ),
    ]