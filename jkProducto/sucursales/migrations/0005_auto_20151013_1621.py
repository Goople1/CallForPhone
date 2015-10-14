# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucursales', '0004_detallesucursalalmacen_sucursal_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallesucursalalmacen',
            name='sucursal_id',
            field=models.ForeignKey(to='sucursales.Sucursal'),
        ),
    ]
