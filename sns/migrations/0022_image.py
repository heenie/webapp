# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0021_auto_20150327_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('image', models.ImageField(upload_to='img', blank=True, null=True)),
                ('article', models.ForeignKey(to='sns.Article')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
