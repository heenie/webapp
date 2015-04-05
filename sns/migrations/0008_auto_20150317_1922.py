# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0007_auto_20150317_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='trade',
            field=models.OneToOneField(to='sns.Trade'),
            preserve_default=True,
        ),
    ]
