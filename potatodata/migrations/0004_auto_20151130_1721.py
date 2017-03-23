# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('potatodata', '0003_auto_20151130_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='potatolink',
            name='subcategory',
            field=models.ForeignKey(null=True, blank=True, to='potatodata.LinkSubcategory'),
            preserve_default=True,
        ),
    ]
