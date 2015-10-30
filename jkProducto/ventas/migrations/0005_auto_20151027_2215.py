# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucursales', '0007_almacen_logo'),
        ('ventas', '0004_auto_20151027_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_precio', models.CharField(max_length=20)),
                ('cantidad', models.PositiveIntegerField()),
                ('precio', models.FloatField()),
                ('detalle_Sucursal_almacen_id', models.ForeignKey(to='sucursales.DetalleSucursalAlmacen')),
                ('venta_id', models.ForeignKey(to='ventas.Venta')),
            ],
        ),
        migrations.RemoveField(
            model_name='detalle_venta',
            name='detalle_Sucursal_almacen_id',
        ),
        migrations.RemoveField(
            model_name='detalle_venta',
            name='venta_id',
        ),
        migrations.DeleteModel(
            name='Detalle_Venta',
        ),
    ]
