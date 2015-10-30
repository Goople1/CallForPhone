# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0007_auto_20151028_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalleventa',
            name='descripcion',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
