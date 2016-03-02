# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-01 23:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('url_short_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='click',
            name='access_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='click',
            name='accessed',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='click',
            name='created',
            field=models.DateField(verbose_name=datetime.datetime(2016, 3, 1, 23, 42, 55, 579998, tzinfo=utc)),
        ),
    ]
