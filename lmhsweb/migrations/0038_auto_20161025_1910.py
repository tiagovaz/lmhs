# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-25 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmhsweb', '0037_auto_20161025_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coteauteur',
            name='cote',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='coteprefixe',
            name='cote',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
    ]