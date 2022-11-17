# Generated by Django 2.2.8 on 2022-11-16 05:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0020_auto_20221116_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchmodel',
            name='end_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 16, 10, 35, 14, 506816), max_length=30),
        ),
        migrations.AlterField(
            model_name='matchmodel',
            name='start_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 16, 10, 35, 14, 506794), max_length=30),
        ),
        migrations.AlterField(
            model_name='requestmodel',
            name='end_time',
            field=models.TimeField(blank=True, default='10:35:14'),
        ),
        migrations.AlterField(
            model_name='requestmodel',
            name='start_time',
            field=models.TimeField(blank=True, default='10:35:14'),
        ),
        migrations.AlterField(
            model_name='tournamentmodel',
            name='end_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 16, 10, 35, 14, 507761), max_length=30),
        ),
        migrations.AlterField(
            model_name='tournamentmodel',
            name='start_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 16, 10, 35, 14, 507748), max_length=30),
        ),
        migrations.AlterField(
            model_name='tournamentrequestmodel',
            name='end_time',
            field=models.TimeField(blank=True, default='10:35:14'),
        ),
        migrations.AlterField(
            model_name='tournamentrequestmodel',
            name='start_time',
            field=models.TimeField(blank=True, default='10:35:14'),
        ),
    ]
