# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sncfdata_rt', '0002_auto_20150114_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='info',
            field=models.URLField(verbose_name='Additional information', blank=True, default='http://www.infolignes.com/'),
            preserve_default=True,
        ),
    ]
