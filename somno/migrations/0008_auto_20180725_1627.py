# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-07-25 16:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('somno', '0007_auto_20180725_1610'),
    ]

    operations = [
        migrations.RenameField(
            model_name='infusion',
            old_name='end_date',
            new_name='stopped_time',
        ),
    ]