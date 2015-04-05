# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0029_remove_car_transportation'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='transportation',
            field=models.CharField(max_length=50, default='기타'),
            preserve_default=True,
        ),
    ]
