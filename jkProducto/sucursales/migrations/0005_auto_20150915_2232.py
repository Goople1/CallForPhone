# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('sucursales', '0004_sucursaltrabajador_fecha_nacimiento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=10)),
                ('dni', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(regex=b'\\d{8}', message=b'DNI no tiene 8 digitos', code=b'invalido')])),
            ],
        ),
        migrations.AddField(
            model_name='sucursaltrabajador',
            name='sexo',
            field=models.CharField(default=b'm', max_length=1, choices=[(b'm', b'M'), (b'f', b'F')]),
        ),
    ]
