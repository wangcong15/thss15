# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-15 06:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thss', '0004_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='sterms',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
