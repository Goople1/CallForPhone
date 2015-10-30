# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleventa',
            name='venta_id',
            field=models.OneToOneField(to='ventas.Venta'),
        ),
    ]
