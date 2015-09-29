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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('usda_name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='FWA',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('date', models.DateField()),
                ('fwa', models.DecimalField(max_digits=6, decimal_places=3)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('usda_name', models.CharField(max_length=30, unique=True)),
                ('napmn_name', models.CharField(max_length=30, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='GRI',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('date', models.DateField()),
                ('gri', models.DecimalField(max_digits=6, decimal_places=3)),
            ],
        ),
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('week_ending', models.DateField()),
                ('season', models.PositiveSmallIntegerField()),
                ('organic', models.IntegerField()),
                ('import_export', models.CharField(max_length=8)),
                ('transport_mode', models.CharField(max_length=9)),
                ('total_weight', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MovementDistrict',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('usda_name', models.CharField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='napmnRegion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('napmn_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Origin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('usda_name', models.CharField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('usda_name', models.CharField(max_length=50, unique=True)),
                ('napmn_name', models.CharField(max_length=30, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingDistrict',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('usda_name', models.CharField(max_length=100, unique=True)),
                ('napmn_name', models.ForeignKey(null=True, to='potatodata.napmnRegion')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingPointPrice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('report_date', models.DateField()),
                ('season', models.PositiveSmallIntegerField()),
                ('low', models.DecimalField(max_digits=6, decimal_places=2)),
                ('high', models.DecimalField(null=True, max_digits=6, decimal_places=2)),
                ('mostly_low', models.DecimalField(null=True, max_digits=6, decimal_places=2)),
                ('mostly_high', models.DecimalField(null=True, max_digits=6, decimal_places=2)),
                ('price_weight', models.IntegerField()),
                ('grade', models.ForeignKey(to='potatodata.Grade')),
                ('package', models.ForeignKey(to='potatodata.Package')),
                ('shipping_district', models.ForeignKey(to='potatodata.ShippingDistrict')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('usda_name', models.CharField(max_length=50, unique=True)),
                ('napmn_name', models.CharField(max_length=30, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subvariety',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('usda_name', models.CharField(max_length=30, unique=True)),
                ('napmn_name', models.CharField(max_length=30, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TruckRate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('week_ending', models.DateField()),
                ('week_low', models.IntegerField()),
                ('week_high', models.IntegerField(null=True)),
                ('day_low', models.IntegerField(null=True)),
                ('day_high', models.IntegerField(null=True)),
                ('price_weight', models.IntegerField()),
                ('freight_destination', models.ForeignKey(to='potatodata.FreightDestination')),
                ('shipping_district', models.ForeignKey(to='potatodata.ShippingDistrict')),
            ],
        ),
        migrations.CreateModel(
            name='Variety',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('usda_name', models.CharField(max_length=30, unique=True)),
                ('napmn_name', models.CharField(max_length=30, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='shippingpointprice',
            name='size',
            field=models.ForeignKey(to='potatodata.Size'),
        ),
        migrations.AddField(
            model_name='shippingpointprice',
            name='subvariety',
            field=models.ForeignKey(to='potatodata.Subvariety'),
        ),
        migrations.AddField(
            model_name='shippingpointprice',
            name='variety',
            field=models.ForeignKey(to='potatodata.Variety'),
        ),
        migrations.AddField(
            model_name='movement',
            name='movement_district',
            field=models.ForeignKey(to='potatodata.MovementDistrict'),
        ),
        migrations.AddField(
            model_name='movement',
            name='origin',
            field=models.ForeignKey(to='potatodata.Origin'),
        ),
        migrations.AddField(
            model_name='movement',
            name='variety',
            field=models.ForeignKey(to='potatodata.Variety'),
        ),
        migrations.AddField(
            model_name='gri',
            name='napmn_region',
            field=models.ForeignKey(to='potatodata.napmnRegion'),
        ),
        migrations.AddField(
            model_name='gri',
            name='subvariety',
            field=models.ForeignKey(to='potatodata.Subvariety'),
        ),
        migrations.AddField(
            model_name='fwa',
            name='napmn_region',
            field=models.ForeignKey(to='potatodata.napmnRegion'),
        ),
        migrations.AddField(
            model_name='fwa',
            name='subvariety',
            field=models.ForeignKey(to='potatodata.Subvariety'),
        ),
        migrations.AlterUniqueTogether(
            name='truckrate',
            unique_together=set([('week_ending', 'shipping_district', 'freight_destination')]),
        ),
        migrations.AlterUniqueTogether(
            name='shippingpointprice',
            unique_together=set([('report_date', 'shipping_district', 'variety', 'subvariety', 'grade', 'package', 'size')]),
        ),
        migrations.AlterUniqueTogether(
            name='movement',
            unique_together=set([('week_ending', 'origin', 'movement_district', 'season', 'variety', 'organic', 'import_export', 'transport_mode')]),
        ),
        migrations.AlterUniqueTogether(
            name='gri',
            unique_together=set([('date', 'napmn_region', 'subvariety')]),
        ),
        migrations.AlterUniqueTogether(
            name='fwa',
            unique_together=set([('date', 'napmn_region', 'subvariety')]),
        ),
    ]
