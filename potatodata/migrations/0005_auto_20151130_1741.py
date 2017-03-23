# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('potatodata', '0004_auto_20151130_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='potatolink',
            name='description',
            field=models.CharField(blank=True, max_length=200),
            preserve_default=True,
        ),
    ]
