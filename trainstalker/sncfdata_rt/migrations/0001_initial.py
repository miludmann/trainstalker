# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DepartureTime',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('departure_time', models.DateTimeField(verbose_name='departure time')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('station_name', models.CharField(max_length=100)),
                ('station_code', models.CharField(max_length=11)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('destination', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('model_type', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('info', models.URLField(verbose_name='additional information')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='departuretime',
            name='station',
            field=models.ForeignKey(to='sncfdata_rt.Station'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='departuretime',
            name='train',
            field=models.ForeignKey(to='sncfdata_rt.Train'),
            preserve_default=True,
        ),
    ]
