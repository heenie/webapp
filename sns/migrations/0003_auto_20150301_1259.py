# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0002_auto_20150214_2354'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('depart', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('sell_mon', models.IntegerField(null=True, blank=True)),
                ('sell_deposit', models.IntegerField(null=True, blank=True)),
                ('roommate', models.BooleanField(default=False)),
                ('room_mon', models.IntegerField(null=True, blank=True)),
                ('room_deposit', models.IntegerField(null=True, blank=True)),
                ('time', models.DateTimeField()),
                ('memo', models.TextField()),
                ('area', models.ForeignKey(to='sns.Area')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('total_fee', models.IntegerField(null=True, blank=True)),
                ('per_fee', models.IntegerField(null=True, blank=True)),
                ('time', models.DateTimeField()),
                ('now_num', models.IntegerField(null=True, blank=True)),
                ('total_num', models.IntegerField(null=True, blank=True)),
                ('memo', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transportation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=70)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='store',
            name='trade',
            field=models.ForeignKey(to='sns.Trade'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='car',
            name='trade',
            field=models.ForeignKey(to='sns.Trade'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='car',
            name='transportation',
            field=models.ForeignKey(to='sns.Transportation'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='car',
            field=models.ForeignKey(to='sns.Car', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='house',
            field=models.ForeignKey(to='sns.House', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='store',
            field=models.ForeignKey(to='sns.Store', null=True),
            preserve_default=True,
        ),
    ]
