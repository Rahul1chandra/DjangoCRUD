# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-20 09:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('databasetest', '0004_auto_20170820_0905'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ('name',)},
        ),
    ]