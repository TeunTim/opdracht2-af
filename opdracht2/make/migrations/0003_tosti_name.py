# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 09:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('make', '0002_auto_20170108_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='tosti',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
