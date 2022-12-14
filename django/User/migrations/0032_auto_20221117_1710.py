# Generated by Django 2.2.8 on 2022-11-17 11:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0031_auto_20221117_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchmodel',
            name='end_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 17, 17, 10, 27, 208202), max_length=30),
        ),
        migrations.AlterField(
            model_name='matchmodel',
            name='start_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 17, 17, 10, 27, 208183), max_length=30),
        ),
        migrations.AlterField(
            model_name='requestmodel',
            name='end_time',
            field=models.TimeField(blank=True, default='17:10:27'),
        ),
        migrations.AlterField(
            model_name='requestmodel',
            name='start_time',
            field=models.TimeField(blank=True, default='17:10:27'),
        ),
        migrations.AlterField(
            model_name='tournamentmodel',
            name='end_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 17, 17, 10, 27, 209130), max_length=30),
        ),
        migrations.AlterField(
            model_name='tournamentmodel',
            name='start_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 17, 17, 10, 27, 209117), max_length=30),
        ),
        migrations.AlterField(
            model_name='tournamentmodel',
            name='team_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='User.CreateTeamModel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tournamentrequestmodel',
            name='end_time',
            field=models.TimeField(blank=True, default='17:10:27'),
        ),
        migrations.AlterField(
            model_name='tournamentrequestmodel',
            name='start_time',
            field=models.TimeField(blank=True, default='17:10:27'),
        ),
        migrations.AlterField(
            model_name='turfcommentsmodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 17, 17, 10, 27, 210387), max_length=30),
        ),
    ]
