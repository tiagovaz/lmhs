# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-11-08 20:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lmhsweb', '0056_auto_20171108_1309'),
    ]

    operations = [
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='State',
        ),
    ]
