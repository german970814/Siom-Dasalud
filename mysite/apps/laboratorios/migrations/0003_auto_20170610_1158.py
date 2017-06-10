# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historias', '0002_auto_20170329_1809'),
        ('laboratorios', '0002_auto_20170522_1252'),
    ]

    operations = [
        migrations.CreateModel(
            name='HojaGasto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField(default=1, verbose_name='Cantidad')),
                ('orden', models.ForeignKey(related_name='hojas_gasto', verbose_name='Orden', to='historias.orden')),
            ],
        ),
        migrations.CreateModel(
            name='PlantillaArea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField(default=1, verbose_name='Cantidad')),
                ('area', models.ForeignKey(related_name='plantillas', verbose_name='Area', to='laboratorios.SeccionTrabajo')),
            ],
        ),
        migrations.CreateModel(
            name='PlantillaLaboratorio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField(default=1, verbose_name='Cantidad')),
                ('laboratorio', models.ForeignKey(related_name='plantillas', verbose_name='Laboratorio', to='laboratorios.Laboratorio')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=50, verbose_name='C\xf3digo')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('alarma_inferior', models.IntegerField(null=True, verbose_name='Alarma inferior', blank=True)),
                ('alarma_media', models.IntegerField(null=True, verbose_name='Alarma media', blank=True)),
                ('tipo', models.CharField(max_length=1, verbose_name='Tipo', choices=[('R', 'REACTIVO'), ('I', 'INSUMO')])),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
            ],
        ),
        migrations.RemoveField(
            model_name='bancoreactivo',
            name='reactivo',
        ),
        migrations.RemoveField(
            model_name='reactivo',
            name='laboratorio',
        ),
        migrations.RemoveField(
            model_name='recarga',
            name='reactivo',
        ),
        migrations.AddField(
            model_name='recarga',
            name='distribuidor',
            field=models.CharField(max_length=100, verbose_name='Distribuidor', blank=True),
        ),
        migrations.AddField(
            model_name='recarga',
            name='fabricante',
            field=models.CharField(max_length=100, verbose_name='Fabricante', blank=True),
        ),
        migrations.AddField(
            model_name='recarga',
            name='fecha_distribucion',
            field=models.DateField(null=True, verbose_name='Fecha de distribuci\xf3n', blank=True),
        ),
        migrations.AddField(
            model_name='recarga',
            name='fecha_vencimiento',
            field=models.DateField(null=True, verbose_name='Fecha de vencimiento', blank=True),
        ),
        migrations.AddField(
            model_name='recarga',
            name='invima',
            field=models.CharField(max_length=100, verbose_name='Invima', blank=True),
        ),
        migrations.AddField(
            model_name='recarga',
            name='lote',
            field=models.CharField(max_length=100, verbose_name='Lote', blank=True),
        ),
        migrations.AddField(
            model_name='recarga',
            name='marca',
            field=models.CharField(max_length=100, verbose_name='Marca', blank=True),
        ),
        migrations.AddField(
            model_name='recarga',
            name='presentacion',
            field=models.CharField(max_length=100, verbose_name='Presentaci\xf3n', blank=True),
        ),
        migrations.DeleteModel(
            name='BancoReactivo',
        ),
        migrations.DeleteModel(
            name='Reactivo',
        ),
        migrations.AddField(
            model_name='plantillalaboratorio',
            name='producto',
            field=models.ForeignKey(related_name='plantillas_laboratorio', verbose_name='Producto', to='laboratorios.Producto'),
        ),
        migrations.AddField(
            model_name='plantillaarea',
            name='producto',
            field=models.ForeignKey(related_name='plantillas_area', verbose_name='Producto', to='laboratorios.Producto'),
        ),
        migrations.AddField(
            model_name='hojagasto',
            name='producto',
            field=models.ForeignKey(verbose_name='Producto', to='laboratorios.Producto'),
        ),
        migrations.AddField(
            model_name='recarga',
            name='producto',
            field=models.ForeignKey(related_name='recargas', default=1, verbose_name='Producto', to='laboratorios.Producto'),
            preserve_default=False,
        ),
    ]
