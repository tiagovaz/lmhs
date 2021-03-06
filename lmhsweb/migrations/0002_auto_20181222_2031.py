# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-12-22 20:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lmhsweb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='main',
            name='auteur',
        ),
        migrations.AddField(
            model_name='main',
            name='auteur',
            field=models.ManyToManyField(blank=True, to='lmhsweb.Auteur'),
        ),
        migrations.RemoveField(
            model_name='main',
            name='cote_auteur',
        ),
        migrations.AddField(
            model_name='main',
            name='cote_auteur',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Cote_Auteur', to='lmhsweb.Auteur'),
        ),
        migrations.AlterField(
            model_name='main',
            name='date_ajout',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
