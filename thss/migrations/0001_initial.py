# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-12 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20)),
                ('upass', models.CharField(max_length=50)),
                ('urank', models.IntegerField(max_length=1)),
            ],
        ),
    ]
