# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lodging', '0004_auto_20171103_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
