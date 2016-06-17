# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-17 03:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lmhsweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Collection',
            },
        ),
        migrations.AlterField(
            model_name='auteur',
            name='cote_auteur',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='auteur',
            name='nom_auteur',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='main',
            name='collection',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lmhsweb.Collection'),
        ),
    ]
