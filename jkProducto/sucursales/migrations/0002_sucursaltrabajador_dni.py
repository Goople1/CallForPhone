# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucursales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sucursaltrabajador',
            name='dni',
            field=models.CharField(default=b'00000000', unique=True, max_length=8),
        ),
    ]
