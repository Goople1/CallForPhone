# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucursales', '0003_historialdetallealmacen_sucursal_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallesucursalalmacen',
            name='sucursal_id',
            field=models.ForeignKey(to='sucursales.Sucursal', null=True),
        ),
    ]
