# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(null=True, blank=True, upload_to='./image'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(null=True, blank=True, upload_to='./profile'),
            preserve_default=True,
        ),
    ]
