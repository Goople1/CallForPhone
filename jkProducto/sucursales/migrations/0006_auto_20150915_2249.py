# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucursales', '0005_auto_20150915_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='correo',
            field=models.EmailField(default=b'@gmail', max_length=254, blank=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='direccion',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='razon_social',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='ruc',
            field=models.CharField(max_length=11, blank=True),
        ),
    ]
