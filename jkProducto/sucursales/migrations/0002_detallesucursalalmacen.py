# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
        ('sucursales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleSucursalAlmacen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('adicional_stock', models.PositiveSmallIntegerField(default=0)),
                ('fecha_ingreso', models.DateTimeField(auto_now=True)),
                ('producto_id', models.ForeignKey(to='productos.Producto')),
            ],
        ),
    ]
