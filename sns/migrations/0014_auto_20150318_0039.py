# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0013_remove_house_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='time',
            field=models.CharField(max_length=100, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='area',
            name='name',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='car',
            name='depart',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='store',
            name='fee',
            field=models.CharField(max_length=100, default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='store',
            name='time',
            field=models.CharField(max_length=100, default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trade',
            name='fee',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trade',
            name='time',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
