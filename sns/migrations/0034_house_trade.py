# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0033_auto_20150405_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='trade',
            field=models.OneToOneField(to='sns.Trade', default=None),
            preserve_default=True,
        ),
    ]
