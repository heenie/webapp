# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0009_remove_car_trade'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='trade',
            field=models.OneToOneField(to='sns.Trade', default=None),
            preserve_default=True,
        ),
    ]
