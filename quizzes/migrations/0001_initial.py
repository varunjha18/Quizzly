# Generated by Django 3.2.2 on 2021-05-26 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_id', models.IntegerField()),
                ('question_no', models.IntegerField()),
                ('problem', models.TextField()),
                ('option_1', models.CharField(max_length=200)),
                ('option_2', models.CharField(max_length=200)),
                ('option_3', models.CharField(max_length=200)),
                ('option_4', models.CharField(default='None of these', max_length=200)),
                ('option_5', models.CharField(blank=True, max_length=200)),
                ('option_6', models.CharField(blank=True, max_length=200)),
                ('option_7', models.CharField(blank=True, max_length=200)),
                ('prob_img_1', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('prob_img_2', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('prob_img_3', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
            ],
        ),
    ]
