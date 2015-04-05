# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0031_auto_20150405_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='transportation',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
