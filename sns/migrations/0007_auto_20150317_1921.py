# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0006_category_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('fee', models.CharField(default=None, max_length=70)),
                ('time', models.CharField(default=None, max_length=70)),
                ('now_num', models.IntegerField(null=True, blank=True)),
                ('total_num', models.IntegerField(null=True, blank=True)),
                ('memo', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='car',
            name='trade',
            field=models.OneToOneField(to='sns.Trade', default=None),
            preserve_default=True,
        ),
    ]
