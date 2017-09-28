# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 07:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataVisualizer', '0007_auto_20170928_1002'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aluhyper',
            options={'verbose_name_plural': 'AluHyper'},
        ),
        migrations.AlterField(
            model_name='aluhyper',
            name='AVG_Norm',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=100),
        ),
        migrations.AlterField(
            model_name='aluhyper',
            name='SampleType',
            field=models.TextField(default='NA', max_length=100),
        ),
        migrations.AlterField(
            model_name='aluhyper',
            name='contIndex',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=100),
        ),
        migrations.AlterField(
            model_name='aluhyper',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
