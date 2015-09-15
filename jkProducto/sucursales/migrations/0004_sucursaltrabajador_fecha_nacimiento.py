# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucursales', '0003_auto_20150915_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='sucursaltrabajador',
            name='fecha_nacimiento',
            field=models.DateField(null=True, blank=True),
        ),
    ]
