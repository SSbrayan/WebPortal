# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20171128_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='target',
            name='ports_dic',
            field=models.CharField(default=b'No Data', max_length=10000),
        ),
        migrations.AlterField(
            model_name='target',
            name='ports_limits_dic',
            field=models.CharField(default=b'No Data', max_length=10000),
        ),
        migrations.AlterField(
            model_name='target',
            name='system_information_dic',
            field=models.CharField(default=b'No Data', max_length=10000),
        ),
        migrations.AlterField(
            model_name='target',
            name='system_information_js',
            field=models.CharField(default=b'No Data', max_length=10000),
        ),
    ]
