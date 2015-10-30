# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0006_detalleventa_importe'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='venta',
            name='total',
            field=models.FloatField(default=0.0, blank=True),
        ),
    ]
