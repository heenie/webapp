# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0032_auto_20150405_2248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='memo',
        ),
        migrations.RemoveField(
            model_name='house',
            name='room_deposit',
        ),
        migrations.RemoveField(
            model_name='house',
            name='room_mon',
        ),
        migrations.RemoveField(
            model_name='house',
            name='roommate',
        ),
        migrations.RemoveField(
            model_name='house',
            name='sell_deposit',
        ),
        migrations.RemoveField(
            model_name='house',
            name='sell_mon',
        ),
        migrations.RemoveField(
            model_name='house',
            name='time',
        ),
    ]
