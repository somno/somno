# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-08-02 12:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("somno", "0011_monitorpatientpairing_user")]

    operations = [
        migrations.RemoveField(model_name="monitorpatientpairing", name="user")
    ]
