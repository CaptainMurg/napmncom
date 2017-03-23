# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FreightDestination',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('usda_name', models.CharField(unique=True, max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FWA',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('date', models.DateField()),
                ('fwa', models.DecimalField(decimal_places=3, max_digits=6)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('usda_name', models.CharField(unique=True, max_length=30)),
                ('napmn_name', models.CharField(blank=True, max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GRI',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('date', models.DateField()),
                ('gri', models.DecimalField(decimal_places=3, max_digits=6)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('week_ending', models.DateField()),
                ('season', models.PositiveSmallIntegerField()),
                ('organic', models.IntegerField()),
                ('import_export', models.CharField(max_length=8)),
                ('transport_mode', models.CharField(max_length=9)),
                ('total_weight', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MovementDistrict',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('usda_name', models.CharField(unique=True, max_length=60)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='napmnRegion',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('napmn_name', models.CharField(max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Origin',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('usda_name', models.CharField(unique=True, max_length=60)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('usda_name', models.CharField(unique=True, max_length=50)),
                ('napmn_name', models.CharField(blank=True, max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShippingDistrict',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('usda_name', models.CharField(unique=True, max_length=100)),
                ('napmn_name', models.ForeignKey(to='potatodata.napmnRegion', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShippingPointPrice',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('report_date', models.DateField()),
                ('season', models.PositiveSmallIntegerField()),
                ('low', models.DecimalField(decimal_places=2, max_digits=6)),
                ('high', models.DecimalField(null=True, decimal_places=2, max_digits=6)),
                ('mostly_low', models.DecimalField(null=True, decimal_places=2, max_digits=6)),
                ('mostly_high', models.DecimalField(null=True, decimal_places=2, max_digits=6)),
                ('price_weight', models.IntegerField()),
                ('grade', models.ForeignKey(to='potatodata.Grade')),
                ('package', models.ForeignKey(to='potatodata.Package')),
                ('shipping_district', models.ForeignKey(to='potatodata.ShippingDistrict')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('usda_name', models.CharField(unique=True, max_length=50)),
                ('napmn_name', models.CharField(blank=True, max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subvariety',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('usda_name', models.CharField(unique=True, max_length=30)),
                ('napmn_name', models.CharField(blank=True, max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TruckRate',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('week_ending', models.DateField()),
                ('week_low', models.IntegerField()),
                ('week_high', models.IntegerField(null=True)),
                ('day_low', models.IntegerField(null=True)),
                ('day_high', models.IntegerField(null=True)),
                ('price_weight', models.IntegerField()),
                ('freight_destination', models.ForeignKey(to='potatodata.FreightDestination')),
                ('shipping_district', models.ForeignKey(to='potatodata.ShippingDistrict')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Variety',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('usda_name', models.CharField(unique=True, max_length=30)),
                ('napmn_name', models.CharField(blank=True, max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='truckrate',
            unique_together=set([('week_ending', 'shipping_district', 'freight_destination')]),
        ),
        migrations.AddField(
            model_name='shippingpointprice',
            name='size',
            field=models.ForeignKey(to='potatodata.Size'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shippingpointprice',
            name='subvariety',
            field=models.ForeignKey(to='potatodata.Subvariety'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shippingpointprice',
            name='variety',
            field=models.ForeignKey(to='potatodata.Variety'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='shippingpointprice',
            unique_together=set([('report_date', 'shipping_district', 'variety', 'subvariety', 'grade', 'package', 'size')]),
        ),
        migrations.AddField(
            model_name='movement',
            name='movement_district',
            field=models.ForeignKey(to='potatodata.MovementDistrict'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movement',
            name='origin',
            field=models.ForeignKey(to='potatodata.Origin'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movement',
            name='variety',
            field=models.ForeignKey(to='potatodata.Variety'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='movement',
            unique_together=set([('week_ending', 'origin', 'movement_district', 'season', 'variety', 'organic', 'import_export', 'transport_mode')]),
        ),
        migrations.AddField(
            model_name='gri',
            name='napmn_region',
            field=models.ForeignKey(to='potatodata.napmnRegion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gri',
            name='subvariety',
            field=models.ForeignKey(to='potatodata.Subvariety'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='gri',
            unique_together=set([('date', 'napmn_region', 'subvariety')]),
        ),
        migrations.AddField(
            model_name='fwa',
            name='napmn_region',
            field=models.ForeignKey(to='potatodata.napmnRegion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fwa',
            name='subvariety',
            field=models.ForeignKey(to='potatodata.Subvariety'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='fwa',
            unique_together=set([('date', 'napmn_region', 'subvariety')]),
        ),
    ]
