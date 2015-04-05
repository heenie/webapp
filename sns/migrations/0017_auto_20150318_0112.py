# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0016_auto_20150318_0111'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='trade',
            field=models.OneToOneField(to='sns.Trade', default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='store',
            name='article',
            field=models.OneToOneField(to='sns.Article'),
            preserve_default=True,
        ),
    ]
