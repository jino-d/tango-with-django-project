# Generated by Django 2.1.5 on 2021-08-29 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0007_auto_20210829_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='last_visit',
            field=models.DateTimeField(),
        ),
    ]
