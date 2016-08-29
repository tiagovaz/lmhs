# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-10 18:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lmhsweb', '0027_auto_20160710_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='cote_annee',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='main',
            name='cote_numero',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='main',
            name='editeur',
            field=models.ManyToManyField(blank=True, null=True, to='lmhsweb.Editeur', verbose_name='\xc9diteur'),
        ),
        migrations.AlterField(
            model_name='main',
            name='fonds',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lmhsweb.Fonds', verbose_name='Fonds'),
        ),
        migrations.AlterField(
            model_name='main',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lmhsweb.Genre', verbose_name='Genre'),
        ),
    ]
