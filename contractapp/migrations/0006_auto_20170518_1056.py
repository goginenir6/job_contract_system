# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-18 10:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contractapp', '0005_auto_20170518_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
