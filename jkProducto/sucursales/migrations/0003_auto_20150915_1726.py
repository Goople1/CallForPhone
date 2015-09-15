# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucursales', '0002_sucursaltrabajador_dni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sucursaltrabajador',
            name='dni',
            field=models.CharField(default=b'0', unique=True, max_length=8),
        ),
    ]
