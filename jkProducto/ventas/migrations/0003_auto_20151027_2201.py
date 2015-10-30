# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0002_auto_20151027_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleventa',
            name='venta_id',
            field=models.ForeignKey(to='ventas.Venta'),
        ),
    ]
