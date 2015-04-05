# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0010_car_trade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='fee',
        ),
        migrations.RemoveField(
            model_name='car',
            name='memo',
        ),
        migrations.RemoveField(
            model_name='car',
            name='now_num',
        ),
        migrations.RemoveField(
            model_name='car',
            name='time',
        ),
        migrations.RemoveField(
            model_name='car',
            name='total_num',
        ),
    ]
