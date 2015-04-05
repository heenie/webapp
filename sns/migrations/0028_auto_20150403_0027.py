# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0027_auto_20150328_2217'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.FileField(null=True, blank=True, upload_to='documents/%Y/%m/%d'),
            preserve_default=True,
        ),
    ]
