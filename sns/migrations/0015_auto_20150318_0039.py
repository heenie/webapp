# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0014_auto_20150318_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='time',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
