# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucursales', '0007_auto_20150915_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sucursaltrabajador',
            name='cargo',
            field=models.CharField(default=b'empl', max_length=20, choices=[(b'admi', b'Administrador'), (b'empl', b'Empleado')]),
        ),
    ]
