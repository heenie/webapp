# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0024_auto_20150328_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='article',
            field=models.ForeignKey(default=None, to='sns.Article'),
            preserve_default=True,
        ),
    ]
