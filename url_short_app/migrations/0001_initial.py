# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-01 18:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=15)),
                ('description', models.TextField(blank=True)),
                ('shortened', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(verbose_name=datetime.datetime(2016, 3, 1, 18, 20, 7, 774611, tzinfo=utc))),
                ('accessed', models.DateField()),
                ('bookmark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='url_short_app.Bookmark')),
            ],
        ),
    ]