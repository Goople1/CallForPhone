# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo_puesto', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=60)),
                ('direccion', models.CharField(max_length=120)),
                ('departamento', models.CharField(default=b'Lim', max_length=20, choices=[(b'Ama', b'Amazonas'), (b'Anc', b'Ancash'), (b'Apu', b'Apurimac'), (b'Are', b'Arequipa'), (b'Aya', b'Ayacucho'), (b'Caj', b'Cajamarca'), (b'Cal', b'Callao'), (b'Cuz', b'Cuzco'), (b'Hua', b'Huancavelica'), (b'Hun', b'Huanuco'), (b'Ica', b'Ica'), (b'Jun', b'Junin'), (b'Lal', b'La Libertad'), (b'Lam', b'Lambayeque'), (b'Lim', b'Lima'), (b'Lor', b'Loreto'), (b'Mad', b'Madre de Dios'), (b'Moq', b'Moquegua'), (b'Pas', b'Pasco'), (b'Piu', b'Piura'), (b'Pun', b'Puno'), (b'San', b'San Martin'), (b'Piu', b'Piura'), (b'Tac', b'Tacna'), (b'Tum', b'Tumbes'), (b'Uca', b'Ucayali')])),
            ],
        ),
        migrations.CreateModel(
            name='SucursalTrabajador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_ingreso', models.DateTimeField(auto_now=True)),
                ('cargo', models.CharField(default=b'vend', max_length=20, choices=[(b'admi', b'Administrador'), (b'empl', b'Empleado')])),
                ('sucursal', models.ForeignKey(to='sucursales.Sucursal')),
                ('trabajador', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='sucursal',
            unique_together=set([('codigo_puesto', 'departamento')]),
        ),
    ]
