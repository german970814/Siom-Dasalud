# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizaciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=4)),
                ('descripcion', models.CharField(max_length=350)),
            ],
        ),
        migrations.CreateModel(
            name='consultas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=7)),
                ('descripcion', models.CharField(max_length=200)),
                ('cuenta_contable', models.CharField(max_length=10, null=True, blank=True)),
                ('tarifa', models.PositiveIntegerField(default=0, verbose_name=b'Tarifa')),
            ],
        ),
        migrations.CreateModel(
            name='honorarios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ref', models.CharField(max_length=10)),
                ('codigo', models.CharField(max_length=10)),
                ('descripcion', models.CharField(max_length=350)),
                ('valor', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='procedimientos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=7)),
                ('descripcion', models.CharField(max_length=350)),
                ('cups', models.CharField(max_length=7, null=True, blank=True)),
                ('cuenta_contable', models.CharField(max_length=10, null=True, blank=True)),
                ('equipo', models.CharField(max_length=30, null=True, blank=True)),
                ('tarifa', models.PositiveIntegerField(default=0, verbose_name=b'Tarifa')),
                ('uvr', models.PositiveIntegerField(default=0, verbose_name=b'UVR')),
                ('items', models.ManyToManyField(to='parametros.items', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='rango_consulta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=50)),
                ('cuota', models.PositiveIntegerField(default=0, verbose_name=b'Cuota Moderadora')),
            ],
        ),
        migrations.CreateModel(
            name='rango_procedimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=50)),
                ('porcentaje', models.DecimalField(max_digits=3, decimal_places=3)),
            ],
        ),
        migrations.CreateModel(
            name='sala',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=10)),
                ('lim_1', models.PositiveIntegerField(default=0)),
                ('lim_2', models.PositiveIntegerField(default=0)),
                ('valor', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='servicios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('tipo', models.CharField(default=b'S', max_length=1, verbose_name=b'Tipo', choices=[(b'S', b'Servicio'), (b'L', b'Laboratorio')])),
                ('costo', models.DecimalField(verbose_name=b'Valor Unitario', max_digits=10, decimal_places=2)),
                ('historia', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='serviciosEmpresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('costo', models.DecimalField(verbose_name=b'Valor Unitario', max_digits=10, decimal_places=2)),
                ('empresa', models.ForeignKey(related_name='serviciosEmpresa_empresa', verbose_name='Empresa', to='organizaciones.empresas')),
                ('nombre', models.ForeignKey(related_name='serviciosEmpresa_servicios', verbose_name='Servicio', to='parametros.servicios')),
            ],
        ),
        migrations.CreateModel(
            name='sutura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ref', models.CharField(max_length=10)),
                ('codigo', models.CharField(max_length=10)),
                ('descripcion', models.CharField(max_length=350)),
                ('valor', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
