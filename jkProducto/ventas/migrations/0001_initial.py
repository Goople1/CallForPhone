# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '__first__'),
        ('sucursales', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.PositiveIntegerField()),
                ('precio', models.FloatField()),
                ('referecia_producto', models.ForeignKey(to='productos.ProductoAlmacen')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_emision', models.DateTimeField(auto_now=True)),
                ('igv', models.FloatField()),
                ('subtotal', models.FloatField()),
                ('total', models.FloatField()),
                ('cliente', models.ForeignKey(to='sucursales.Cliente')),
                ('empleado', models.ForeignKey(to='sucursales.SucursalTrabajador')),
            ],
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='referencia_venta',
            field=models.ForeignKey(to='ventas.Venta'),
        ),
    ]
