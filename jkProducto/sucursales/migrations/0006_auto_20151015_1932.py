# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucursales', '0005_auto_20151013_1621'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='detallesucursalalmacen',
            unique_together=set([('producto_id', 'sucursal_id')]),
        ),
    ]
