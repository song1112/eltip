# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-25 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eltip_user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='user',
            name='identity',
        ),
        migrations.RemoveField(
            model_name='user',
            name='sex',
        ),
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.IntegerField(blank=0),
        ),
    ]
