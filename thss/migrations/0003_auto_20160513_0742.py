# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-13 07:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thss', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pclass',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='users',
            name='urank',
            field=models.IntegerField(),
        ),
    ]
