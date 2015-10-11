# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=20)),
                ('color', models.CharField(default=b'Ot', max_length=2, choices=[(b'Sc', b''), (b'Az', b'Azul'), (b'Bl', b'Blanco'), (b'Ne', b'Negro'), (b'Ot', b'Otro'), (b'Pl', b'Plomo')])),
                ('precio_x_mayor', models.PositiveIntegerField()),
                ('precio_x_menor', models.PositiveIntegerField()),
                ('marca', models.ForeignKey(to='productos.Marca')),
            ],
            options={
                'verbose_name_plural': 'Mantenimiento de Productos',
            },
        ),
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=60)),
            ],
            options={
                'verbose_name_plural': 'Tipos de Productos',
            },
        ),
        migrations.AddField(
            model_name='producto',
            name='tipo_producto',
            field=models.ForeignKey(to='productos.TipoProducto'),
        ),
        migrations.AlterUniqueTogether(
            name='producto',
            unique_together=set([('codigo', 'color', 'marca', 'tipo_producto')]),
        ),
    ]
