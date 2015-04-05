# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0015_auto_20150318_0039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='fee',
        ),
        migrations.RemoveField(
            model_name='store',
            name='memo',
        ),
        migrations.RemoveField(
            model_name='store',
            name='now_num',
        ),
        migrations.RemoveField(
            model_name='store',
            name='time',
        ),
        migrations.RemoveField(
            model_name='store',
            name='total_num',
        ),
        migrations.AlterField(
            model_name='house',
            name='roommate',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
