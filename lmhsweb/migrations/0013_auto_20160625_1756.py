# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-25 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmhsweb', '0012_auto_20160624_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='main',
            name='date_fin',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
