# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-27 10:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0002_auto_20160523_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='first_name',
            field=models.CharField(default='Jacob', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myuser',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to='/profilepictures/'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='surname',
            field=models.CharField(max_length=30, null=True),
        ),
    ]