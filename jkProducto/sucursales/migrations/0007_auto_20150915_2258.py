# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('sucursales', '0006_auto_20150915_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='correo',
            field=models.EmailField(max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='dni',
            field=models.CharField(unique=True, max_length=8, validators=[django.core.validators.RegexValidator(regex=b'\\d{8}', message=b'DNI no tiene 8 digitos', code=b'invalido')]),
        ),
    ]
