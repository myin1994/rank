# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2020-05-18 05:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myrank', '0002_auto_20200518_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topscore',
            name='personal_high_score',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
