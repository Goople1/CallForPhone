# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_empresa', models.CharField(max_length=80)),
                ('ruc', models.CharField(unique=True, max_length=11, validators=[django.core.validators.RegexValidator(regex=b'\\d{11}', message=b'Ruc no tiene 11 digitos', code=b'invalido')])),
                ('departamento', models.CharField(default=b'Lim', max_length=20, choices=[(b'Ama', b'Amazonas'), (b'Anc', b'Ancash'), (b'Apu', b'Apurimac'), (b'Are', b'Arequipa'), (b'Aya', b'Ayacucho'), (b'Caj', b'Cajamarca'), (b'Cal', b'Callao'), (b'Cuz', b'Cuzco'), (b'Hua', b'Huancavelica'), (b'Hun', b'Huanuco'), (b'Ica', b'Ica'), (b'Jun', b'Junin'), (b'Lal', b'La Libertad'), (b'Lam', b'Lambayeque'), (b'Lim', b'Lima'), (b'Lor', b'Loreto'), (b'Mad', b'Madre de Dios'), (b'Moq', b'Moquegua'), (b'Pas', b'Pasco'), (b'Piu', b'Piura'), (b'Pun', b'Puno'), (b'San', b'San Martin'), (b'Piu', b'Piura'), (b'Tac', b'Tacna'), (b'Tum', b'Tumbes'), (b'Uca', b'Ucayali')])),
                ('direccion', models.CharField(max_length=80)),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
                ('telefono', models.CharField(max_length=20)),
                ('celular', models.CharField(max_length=20)),
                ('descripcion', models.TextField(max_length=400)),
            ],
            options={
                'verbose_name': 'Empresa',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('razon_social', models.CharField(max_length=50, blank=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=10)),
                ('dni', models.CharField(unique=True, max_length=8, validators=[django.core.validators.RegexValidator(regex=b'\\d{8}', message=b'DNI no tiene 8 digitos', code=b'invalido')])),
                ('direccion', models.CharField(max_length=50, blank=True)),
                ('ruc', models.CharField(max_length=11, blank=True)),
                ('correo', models.EmailField(max_length=254, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleAlmacen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('adicional_stock', models.PositiveSmallIntegerField(default=0)),
                ('descripcion', models.TextField(max_length=400)),
                ('fecha_ingreso', models.DateTimeField(auto_now=True)),
                ('id_almacen', models.ForeignKey(to='sucursales.Almacen')),
                ('producto_id', models.ForeignKey(to='productos.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='EstadoSucursal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_estado', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name_plural': 'Registro de Estados de Sucursales',
            },
        ),
        migrations.CreateModel(
            name='HistorialDetalleAlmacen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('adicional_producto', models.PositiveIntegerField()),
                ('fecha_ingreso', models.DateTimeField(auto_now=True)),
                ('stock_actual', models.PositiveIntegerField()),
                ('detalle_almacen_id', models.ForeignKey(to='sucursales.DetalleAlmacen')),
            ],
        ),
        migrations.CreateModel(
            name='HistorialSucursal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo_puesto', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=60)),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
                ('departamento', models.CharField(default=b'Lim', max_length=20, choices=[(b'Ama', b'Amazonas'), (b'Anc', b'Ancash'), (b'Apu', b'Apurimac'), (b'Are', b'Arequipa'), (b'Aya', b'Ayacucho'), (b'Caj', b'Cajamarca'), (b'Cal', b'Callao'), (b'Cuz', b'Cuzco'), (b'Hua', b'Huancavelica'), (b'Hun', b'Huanuco'), (b'Ica', b'Ica'), (b'Jun', b'Junin'), (b'Lal', b'La Libertad'), (b'Lam', b'Lambayeque'), (b'Lim', b'Lima'), (b'Lor', b'Loreto'), (b'Mad', b'Madre de Dios'), (b'Moq', b'Moquegua'), (b'Pas', b'Pasco'), (b'Piu', b'Piura'), (b'Pun', b'Puno'), (b'San', b'San Martin'), (b'Piu', b'Piura'), (b'Tac', b'Tacna'), (b'Tum', b'Tumbes'), (b'Uca', b'Ucayali')])),
                ('direccion', models.CharField(max_length=80)),
                ('telefono', models.CharField(max_length=20)),
                ('celular', models.CharField(max_length=20)),
                ('descripcion', models.TextField(max_length=400)),
                ('id_almacen', models.ForeignKey(to='sucursales.Almacen')),
                ('id_estadoSucursal', models.ForeignKey(to='sucursales.EstadoSucursal')),
            ],
            options={
                'verbose_name_plural': 'Mantenimiento de Sucursales',
            },
        ),
        migrations.CreateModel(
            name='SucursalTrabajador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_ingreso', models.DateTimeField(auto_now=True)),
                ('cargo', models.CharField(default=b'empl', max_length=20, choices=[(b'admi', b'Administrador'), (b'empl', b'Empleado')])),
                ('dni', models.CharField(unique=True, max_length=8)),
                ('fecha_nacimiento', models.DateField(default=datetime.date(1990, 1, 1), null=True, blank=True)),
                ('sexo', models.CharField(default=b'm', max_length=1, choices=[(b'm', b'Masculino'), (b'f', b'Femenino')])),
                ('sucursal', models.ForeignKey(to='sucursales.Sucursal')),
                ('trabajador', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='historialsucursal',
            name='id_sucursal',
            field=models.ForeignKey(to='sucursales.Sucursal'),
        ),
        migrations.AlterUniqueTogether(
            name='sucursal',
            unique_together=set([('codigo_puesto', 'departamento')]),
        ),
        migrations.AlterUniqueTogether(
            name='detallealmacen',
            unique_together=set([('producto_id',)]),
        ),
    ]
