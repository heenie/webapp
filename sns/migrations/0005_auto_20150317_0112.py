# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0004_auto_20150310_0203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='car',
        ),
        migrations.RemoveField(
            model_name='article',
            name='house',
        ),
        migrations.RemoveField(
            model_name='article',
            name='store',
        ),
        migrations.RemoveField(
            model_name='car',
            name='trade',
        ),
        migrations.RemoveField(
            model_name='store',
            name='trade',
        ),
        migrations.DeleteModel(
            name='Trade',
        ),
        migrations.AddField(
            model_name='car',
            name='article',
            field=models.OneToOneField(to='sns.Article', default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='car',
            name='fee',
            field=models.CharField(default=None, max_length=70),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='car',
            name='memo',
            field=models.TextField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='car',
            name='now_num',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='car',
            name='time',
            field=models.CharField(default=None, max_length=70),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='car',
            name='total_num',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='house',
            name='article',
            field=models.OneToOneField(to='sns.Article', default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='store',
            name='article',
            field=models.OneToOneField(to='sns.Article', default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='store',
            name='fee',
            field=models.CharField(default=None, max_length=70),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='store',
            name='memo',
            field=models.TextField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='store',
            name='now_num',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='store',
            name='time',
            field=models.CharField(default=None, max_length=70),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='store',
            name='total_num',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='car',
            name='depart',
            field=models.CharField(max_length=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='store',
            name='link',
            field=models.URLField(null=True),
            preserve_default=True,
        ),
    ]
