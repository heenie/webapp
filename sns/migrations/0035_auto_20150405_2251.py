# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0034_house_trade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(to='sns.Category'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='house',
            name='article',
            field=models.OneToOneField(to='sns.Article'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='house',
            name='trade',
            field=models.OneToOneField(to='sns.Trade'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='article',
            field=models.ForeignKey(to='sns.Article'),
            preserve_default=True,
        ),
    ]
