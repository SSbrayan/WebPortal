# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 18:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_interface_port'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='target',
            name='ports',
        ),
    ]
