# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 05:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lodging', '0020_auto_20171108_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='description_de',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='description_es',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='description_fr',
            field=models.TextField(null=True),
        ),
    ]
