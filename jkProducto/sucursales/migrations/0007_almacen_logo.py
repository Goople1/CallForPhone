# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucursales', '0006_auto_20151015_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='almacen',
            name='logo',
            field=models.ImageField(null=True, upload_to=b'empresa/', blank=True),
        ),
    ]
