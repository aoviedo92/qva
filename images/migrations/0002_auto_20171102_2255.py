# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 02:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='original_resized',
            new_name='original',
        ),
    ]
