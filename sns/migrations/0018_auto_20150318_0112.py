# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0017_auto_20150318_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='trade',
            field=models.OneToOneField(to='sns.Trade'),
            preserve_default=True,
        ),
    ]
