# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20171128_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='target',
            name='ports_dic',
            field=models.CharField(default=b'No Data', max_length=1000),
        ),
        migrations.AddField(
            model_name='target',
            name='ports_limits_dic',
            field=models.CharField(default=b'No Data', max_length=1000),
        ),
        migrations.AddField(
            model_name='target',
            name='system_information_dic',
            field=models.CharField(default=b'No Data', max_length=1000),
        ),
    ]