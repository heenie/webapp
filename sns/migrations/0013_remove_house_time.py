# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0012_auto_20150317_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='time',
        ),
    ]
