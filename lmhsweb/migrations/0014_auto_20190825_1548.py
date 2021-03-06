# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2019-08-25 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmhsweb', '0013_utilisateur_etat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Corpus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Corpus',
            },
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='etat',
            field=models.CharField(default='En attente', max_length=20, verbose_name='\xc9tat de la demande'),
        ),
        migrations.AddField(
            model_name='main',
            name='corpus',
            field=models.ManyToManyField(blank=True, null=True, to='lmhsweb.Corpus'),
        ),
    ]
