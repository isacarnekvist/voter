# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 07:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deck', '0003_alternative_correct'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='deck',
            unique_together=set([('name', 'created_by')]),
        ),
    ]
