# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0028_auto_20150403_0027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='transportation',
        ),
    ]
