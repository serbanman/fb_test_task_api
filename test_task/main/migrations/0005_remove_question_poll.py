# Generated by Django 2.2.10 on 2021-11-15 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_question_poll'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='poll',
        ),
    ]
