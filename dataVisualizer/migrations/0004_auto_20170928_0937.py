# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 06:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataVisualizer', '0003_auto_20170927_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluhyper',
            name='SampleCode',
            field=models.IntegerField(max_length=30),
        ),
    ]
