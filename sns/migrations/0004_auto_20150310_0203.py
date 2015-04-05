# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0003_auto_20150301_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(to='sns.Category', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='car',
            name='transportation',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Transportation',
        ),
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile'),
            preserve_default=True,
        ),
    ]
