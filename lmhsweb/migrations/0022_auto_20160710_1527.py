# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-10 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmhsweb', '0021_auto_20160710_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='directeur_collection',
            field=models.ManyToManyField(blank=True, null=True, to='lmhsweb.DirecteurCollection'),
        ),
    ]
