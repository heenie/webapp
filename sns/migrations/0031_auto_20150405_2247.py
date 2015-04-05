# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0030_car_transportation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trade',
            name='now_num',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='total_num',
        ),
    ]
