# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('potatodata', '0005_auto_20151130_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='potatolink',
            name='text',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
