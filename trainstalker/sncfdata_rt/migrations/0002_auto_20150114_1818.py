# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sncfdata_rt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='info',
            field=models.URLField(verbose_name='Additional information', blank=True),
            preserve_default=True,
        ),
    ]
