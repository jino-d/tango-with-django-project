# Generated by Django 2.1.5 on 2021-08-30 09:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0009_auto_20210829_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='last_visit',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 30, 9, 11, 24, 248228, tzinfo=utc)),
        ),
    ]