# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultas',
            name='tarifa',
            field=models.PositiveIntegerField(default=0, verbose_name='Tarifa'),
        ),
        migrations.AlterField(
            model_name='procedimientos',
            name='tarifa',
            field=models.PositiveIntegerField(default=0, verbose_name='Tarifa'),
        ),
        migrations.AlterField(
            model_name='procedimientos',
            name='uvr',
            field=models.PositiveIntegerField(default=0, verbose_name='UVR'),
        ),
        migrations.AlterField(
            model_name='rango_consulta',
            name='cuota',
            field=models.PositiveIntegerField(default=0, verbose_name='Cuota Moderadora'),
        ),
        migrations.AlterField(
            model_name='servicios',
            name='costo',
            field=models.DecimalField(max_digits=10, verbose_name='Valor Unitario', decimal_places=2),
        ),
        migrations.AlterField(
            model_name='servicios',
            name='tipo',
            field=models.CharField(default='S', choices=[('S', 'Servicio'), ('L', 'Laboratorio')], verbose_name='Tipo', max_length=1),
        ),
        migrations.AlterField(
            model_name='serviciosempresa',
            name='costo',
            field=models.DecimalField(max_digits=10, verbose_name='Valor Unitario', decimal_places=2),
        ),
    ]
