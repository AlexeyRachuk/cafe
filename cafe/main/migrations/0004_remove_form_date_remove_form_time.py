# Generated by Django 4.1 on 2022-08-17 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_form'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='date',
        ),
        migrations.RemoveField(
            model_name='form',
            name='time',
        ),
    ]
