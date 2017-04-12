# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='agenda_consulta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, null=True, blank=True)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('editable', models.BooleanField(default=False)),
                ('overlap', models.BooleanField(default=False)),
                ('color', models.CharField(max_length=10, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='agenda_procedimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, null=True, blank=True)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('editable', models.BooleanField(default=False)),
                ('overlap', models.BooleanField(default=False)),
                ('color', models.CharField(max_length=10, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='citas_consulta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pnombre', models.CharField(max_length=30, verbose_name='Primer Nombre')),
                ('snombre', models.CharField(max_length=30, null=True, verbose_name='Segundo Nombre', blank=True)),
                ('papellido', models.CharField(max_length=30, verbose_name='Primer Apellido')),
                ('sapellido', models.CharField(max_length=30, null=True, verbose_name='Segundo Apellido', blank=True)),
                ('documento', models.CharField(max_length=2, verbose_name='Documento', choices=[(b'CC', b'C\xc3\xa9dula Ciudadan\xc3\xada'), (b'CE', b'C\xc3\xa9dula de Extranjer\xc3\xada'), (b'PA', b'Pasaporte'), (b'RC', b'Registro Civil'), (b'TI', b'Tarjeta de Identidad'), (b'AS', b'Adulto sin Identificar'), (b'MS', b'Menor sin Identificar'), (b'UN', b'Numero Unico de Identificaci\xc3\xb3n')])),
                ('cedula', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=20, null=True, blank=True)),
                ('celular', models.CharField(max_length=20, null=True, blank=True)),
                ('llego', models.BooleanField(default=False, verbose_name='Paciente Llego')),
                ('confirmo', models.BooleanField(default=False, verbose_name='Confirmo')),
                ('cumplida', models.BooleanField(default=False, verbose_name='Cumplida')),
                ('anestesiologo', models.BooleanField(default=False, verbose_name='Anestesiologo')),
                ('observacion', models.TextField(max_length=250, null=True, blank=True)),
                ('hora_llegada', models.TimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='citas_procedimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pnombre', models.CharField(max_length=30, verbose_name='Primer Nombre')),
                ('snombre', models.CharField(max_length=30, verbose_name='Segundo Nombre')),
                ('papellido', models.CharField(max_length=30, verbose_name='Primer Apellido')),
                ('sapellido', models.CharField(max_length=30, null=True, verbose_name='Segundo Apellido', blank=True)),
                ('documento', models.CharField(max_length=2, verbose_name='Documento', choices=[(b'CC', b'C\xc3\xa9dula Ciudadan\xc3\xada'), (b'CE', b'C\xc3\xa9dula de Extranjer\xc3\xada'), (b'PA', b'Pasaporte'), (b'RC', b'Registro Civil'), (b'TI', b'Tarjeta de Identidad'), (b'AS', b'Adulto sin Identificar'), (b'MS', b'Menor sin Identificar'), (b'UN', b'Numero Unico de Identificaci\xc3\xb3n')])),
                ('cedula', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=20, null=True, blank=True)),
                ('celular', models.CharField(max_length=20, null=True, blank=True)),
                ('llego', models.BooleanField(default=False, verbose_name='Paciente Llego')),
                ('confirmo', models.BooleanField(default=False, verbose_name='Confirmo')),
                ('cumplida', models.BooleanField(default=False, verbose_name='Cumplida')),
                ('anestesiologo', models.BooleanField(default=False, verbose_name='Anestesiologo')),
                ('observacion', models.TextField(max_length=250, null=True, blank=True)),
                ('hora_llegada', models.TimeField(null=True, blank=True)),
                ('agenda', models.OneToOneField(related_name='citas_procedimiento_agenda', to='citas.agenda_procedimiento')),
            ],
        ),
    ]
