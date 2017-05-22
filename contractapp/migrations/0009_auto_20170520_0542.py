# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-20 05:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contractapp', '0008_employee_tenantid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='ismanager',
        ),
        migrations.AlterField(
            model_name='employee',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='staff status'),
        ),
    ]
