# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import mysite.apps.datos.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='especialidades',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=3)),
                ('nombre', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='medico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombres Medico')),
                ('papellido', models.CharField(max_length=30, verbose_name='Primer Apellido')),
                ('sapellido', models.CharField(max_length=30, verbose_name='Segundo Apellido')),
                ('cedula', models.CharField(unique=True, max_length=15, verbose_name='Cedula')),
                ('estado', models.CharField(default=b'A', max_length=1, verbose_name='Estado', choices=[(b'A', b'Activo'), (b'I', b'Inactivo')])),
                ('registro', models.CharField(max_length=20, verbose_name='Registro Medico')),
                ('imagen', models.ImageField(null=True, upload_to=mysite.apps.datos.models.url, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='paciente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pnombre', models.CharField(max_length=30, verbose_name='Primer Nombre')),
                ('snombre', models.CharField(max_length=30, null=True, verbose_name='Segundo Nombre', blank=True)),
                ('papellido', models.CharField(max_length=30, verbose_name='Primer Apellido')),
                ('sapellido', models.CharField(max_length=30, verbose_name='Segundo Apellido')),
                ('genero', models.CharField(max_length=1, verbose_name='Genero', choices=[(b'M', b'Masculino'), (b'F', b'Femenino')])),
                ('fecha_nacimiento', models.DateField(verbose_name=b'Fecha de Nacimiento')),
                ('unidad', models.CharField(default=b'A', max_length=1, verbose_name='Unidad Edad', choices=[(b'1', b'A\xc3\xb1os'), (b'2', b'Meses'), (b'3', b'D\xc3\xadas')])),
                ('edad', models.CharField(max_length=2)),
                ('documento', models.CharField(max_length=2, verbose_name='Documento', choices=[(b'CC', b'C\xc3\xa9dula Ciudadan\xc3\xada'), (b'CE', b'C\xc3\xa9dula de Extranjer\xc3\xada'), (b'PA', b'Pasaporte'), (b'RC', b'Registro Civil'), (b'TI', b'Tarjeta de Identidad'), (b'AS', b'Adulto sin Identificar'), (b'MS', b'Menor sin Identificar'), (b'UN', b'Numero Unico de Identificaci\xc3\xb3n')])),
                ('cedula', models.CharField(unique=True, max_length=20)),
                ('estadoCivil', models.CharField(max_length=1, verbose_name=b'Estado Civil', choices=[(b'C', b'Casado'), (b'U', b'Union Libre'), (b'S', b'Soltero'), (b'V', b'Viudo'), (b'D', b'Divorciado')])),
                ('tipo', models.CharField(default=b'4', max_length=1, verbose_name='Tipo Usuario', choices=[(b'1', b'Contributivo'), (b'2', b'Subsidiado'), (b'3', b'Vinculado'), (b'4', b'Particular'), (b'5', b'Otro')])),
                ('afiliado', models.CharField(default=b'N', max_length=1, verbose_name='Tipo Afiliado', choices=[(b'C', b'Cotizante'), (b'B', b'Beneficiario'), (b'A', b'Adicional'), (b'N', b'Ninguno')])),
                ('zona', models.CharField(default=b'U', max_length=1, verbose_name='Zona Residencia', choices=[(b'U', b'Urbano'), (b'R', b'Rural')])),
                ('escolaridad', models.CharField(default=b'U', max_length=1, verbose_name='Escalonaridad', choices=[(b'P', b'Primaria'), (b'S', b'Secundaria'), (b'T', b'Tecnico'), (b'R', b'Tecnologo'), (b'U', b'Universitaria')])),
                ('direccion', models.CharField(max_length=100)),
                ('barrio', models.CharField(max_length=80)),
                ('Estrato', models.CharField(max_length=1)),
                ('telefono', models.CharField(max_length=20)),
                ('celular', models.CharField(max_length=20, null=True, blank=True)),
                ('status', models.BooleanField(default=True)),
                ('email', models.EmailField(max_length=30, null=True, blank=True)),
                ('visita', models.DateField(default=datetime.date.today, verbose_name=b'Ultima Visita')),
                ('foto', models.ImageField(null=True, upload_to=mysite.apps.datos.models.url, blank=True)),
                ('firma', models.ImageField(null=True, upload_to=mysite.apps.datos.models.url, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='profesiones',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=3)),
                ('profesion', models.CharField(max_length=250)),
            ],
        ),
    ]
