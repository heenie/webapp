# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0011_auto_20150317_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='article',
            field=models.OneToOneField(to='sns.Article'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='car',
            name='trade',
            field=models.OneToOneField(to='sns.Trade'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trade',
            name='fee',
            field=models.CharField(max_length=70),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trade',
            name='time',
            field=models.CharField(max_length=70),
            preserve_default=True,
        ),
    ]
