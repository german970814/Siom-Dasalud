# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categorias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='detalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.PositiveIntegerField(default=0, verbose_name=b'Cantidad')),
                ('precio', models.PositiveIntegerField(default=0, verbose_name=b'Precio')),
            ],
        ),
        migrations.CreateModel(
            name='factura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.PositiveIntegerField()),
                ('letra_factura', models.CharField(max_length=3, null=True, blank=True)),
                ('fecha_emision', models.DateField(default=datetime.date.today, verbose_name=b'Fecha Emision')),
                ('fecha_vencimiento', models.DateField(default=datetime.date.today, verbose_name=b'Fecha Vencimiento')),
                ('fecha_atencion', models.DateField(default=datetime.date.today, verbose_name=b'Fecha Atenci\xc3\xb3n')),
                ('valor_consulta', models.DecimalField(default=0, verbose_name=b'Valor Consulta', max_digits=10, decimal_places=2)),
                ('valor_honorarios', models.DecimalField(default=0, verbose_name=b'Honorarios Medico', max_digits=10, decimal_places=2)),
                ('valor_sala', models.DecimalField(default=0, verbose_name=b'Derechos de Sala', max_digits=10, decimal_places=2)),
                ('valor_sutura', models.DecimalField(default=0, verbose_name=b'Materiales de Sutura', max_digits=10, decimal_places=2)),
                ('valor_anestesia', models.DecimalField(default=0, verbose_name=b'Anestesia y Sedacion', max_digits=10, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.PositiveIntegerField(default=0, verbose_name=b'Precio')),
                ('stock', models.PositiveIntegerField(default=0, verbose_name=b'Cantidad')),
                ('categorias', models.ManyToManyField(to='facturacion.categorias', null=True, blank=True)),
            ],
        ),
    ]
