# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 13:25
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20160523_1258'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='event',
            managers=[
                ('geo_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]