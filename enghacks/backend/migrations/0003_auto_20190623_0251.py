# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-23 02:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_directionthread'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
