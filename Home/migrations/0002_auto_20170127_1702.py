# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-27 11:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='blood_group',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='division',
        ),
    ]