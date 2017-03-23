# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('potatodata', '0002_linkcategory_linksubcategory_potatolink'),
    ]

    operations = [
        migrations.AddField(
            model_name='potatolink',
            name='subcategory',
            field=models.ForeignKey(null=True, to='potatodata.LinkSubcategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='potatolink',
            name='text',
            field=models.CharField(default='Nothing', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='potatolink',
            name='category',
            field=models.ForeignKey(default=1, to='potatodata.LinkCategory'),
            preserve_default=False,
        ),
    ]
