# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0025_image_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='article',
            field=models.ForeignKey(to='sns.Article'),
            preserve_default=True,
        ),
    ]
