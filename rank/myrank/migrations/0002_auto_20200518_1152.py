# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2020-05-18 03:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myrank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]