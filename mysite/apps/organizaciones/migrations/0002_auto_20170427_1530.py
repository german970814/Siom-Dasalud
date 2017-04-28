# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizaciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='afp',
            name='codigo',
            field=models.CharField(default='0', max_length=12),
        ),
        migrations.AlterField(
            model_name='afp',
            name='documento',
            field=models.CharField(default='NI', choices=[('NI', 'Nro de Id Tributaria'), ('CC', 'Cédula de Ciudadanía'), ('CE', 'Cédula de Extranjería'), ('PA', 'Pasaporte')], verbose_name='Documento', max_length=2),
        ),
        migrations.AlterField(
            model_name='arp',
            name='codigo',
            field=models.CharField(default='0', max_length=12),
        ),
        migrations.AlterField(
            model_name='arp',
            name='documento',
            field=models.CharField(default='NI', choices=[('NI', 'Nro de Id Tributaria'), ('CC', 'Cédula de Ciudadanía'), ('CE', 'Cédula de Extranjería'), ('PA', 'Pasaporte')], verbose_name='Documento', max_length=2),
        ),
        migrations.AlterField(
            model_name='empresas',
            name='dias',
            field=models.IntegerField(null=True, verbose_name='Días Vence Factura', blank=True),
        ),
        migrations.AlterField(
            model_name='empresas',
            name='regimen',
            field=models.CharField(default='C', choices=[('C', 'Comun'), ('S', 'Simplificado'), ('N', 'No Aplica')], verbose_name='Estado', max_length=1),
        ),
        migrations.AlterField(
            model_name='empresas',
            name='tipo_tarifa',
            field=models.CharField(default='1', choices=[('1', 'ISS 2001'), ('2', 'ISS 2004')], verbose_name='Tipo de Tarifa', max_length=1),
        ),
        migrations.AlterField(
            model_name='empresas',
            name='valor_sedacion',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name='Costo Base de Sedacion', blank=True),
        ),
        migrations.AlterField(
            model_name='eps',
            name='codigo',
            field=models.CharField(default='0', max_length=12),
        ),
        migrations.AlterField(
            model_name='eps',
            name='documento',
            field=models.CharField(default='NI', choices=[('NI', 'Nro de Id Tributaria'), ('CC', 'Cédula de Ciudadanía'), ('CE', 'Cédula de Extranjería'), ('PA', 'Pasaporte')], verbose_name='Documento', max_length=2),
        ),
        migrations.AlterField(
            model_name='instituciones',
            name='codigo',
            field=models.CharField(default='0', max_length=12),
        ),
        migrations.AlterField(
            model_name='instituciones',
            name='documento',
            field=models.CharField(choices=[('NI', 'Nro de Id Tributaria'), ('CC', 'Cédula de Ciudadanía'), ('CE', 'Cédula de Extranjería'), ('PA', 'Pasaporte')], verbose_name='Documento', max_length=2),
        ),
        migrations.AlterField(
            model_name='usuario_empresa',
            name='empresa',
            field=models.ForeignKey(to='organizaciones.empresas', verbose_name='Empresa', related_name='usuario_empresa_empresas'),
        ),
    ]
