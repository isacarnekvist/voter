# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deck', '0002_auto_20160528_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='alternative',
            name='correct',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
