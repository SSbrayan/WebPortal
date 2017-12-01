# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 18:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20171128_1235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='target',
            old_name='CPHSKU',
            new_name='PCHSKU',
        ),
        migrations.RenameField(
            model_name='target',
            old_name='CPHid',
            new_name='PCHid',
        ),
        migrations.RenameField(
            model_name='target',
            old_name='CPHplatform',
            new_name='PCHplatform',
        ),
        migrations.RenameField(
            model_name='target',
            old_name='CPHstepping',
            new_name='PCHstepping',
        ),
        migrations.RemoveField(
            model_name='target',
            name='platform',
        ),
    ]