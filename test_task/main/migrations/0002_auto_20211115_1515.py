# Generated by Django 2.2.10 on 2021-11-15 15:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 15, 15, 15, 11, 115692, tzinfo=utc)),
        ),
    ]
