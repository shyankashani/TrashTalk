# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cleanups', '0002_auto_20171113_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cleanup',
            name='image',
            field=models.CharField(default='images/defaults/bow_rake.jpg', max_length=300),
        ),
        migrations.AlterField(
            model_name='location',
            name='country',
            field=models.CharField(default='United States', max_length=100),
        ),
        migrations.AlterField(
            model_name='location',
            name='county',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='location',
            name='cross_street',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='location',
            name='district',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='location',
            name='zipcode',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
