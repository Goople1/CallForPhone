# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucursales', '0007_almacen_logo'),
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
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_emision', models.DateTimeField(auto_now=True)),
                ('total', models.FloatField(blank=True)),
                ('empleado', models.ForeignKey(to='sucursales.SucursalTrabajador')),
                ('sucursal', models.ForeignKey(to='sucursales.Sucursal')),
            ],
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='venta_id',
            field=models.ForeignKey(to='ventas.Venta'),
        ),
    ]
