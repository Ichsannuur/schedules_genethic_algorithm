# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-01 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
