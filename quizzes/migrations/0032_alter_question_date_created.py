# Generated by Django 3.2.3 on 2021-06-11 17:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0031_alter_question_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 11, 23, 23, 38, 807820)),
        ),
    ]
