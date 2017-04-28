# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0002_auto_20170329_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle',
            name='cantidad',
            field=models.PositiveIntegerField(default=0, verbose_name='Cantidad'),
        ),
        migrations.AlterField(
            model_name='detalle',
            name='precio',
            field=models.PositiveIntegerField(default=0, verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='fecha_atencion',
            field=models.DateField(default=datetime.date.today, verbose_name='Fecha Atención'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='fecha_emision',
            field=models.DateField(default=datetime.date.today, verbose_name='Fecha Emision'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='fecha_vencimiento',
            field=models.DateField(default=datetime.date.today, verbose_name='Fecha Vencimiento'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='valor_anestesia',
            field=models.DecimalField(default=0, max_digits=10, verbose_name='Anestesia y Sedacion', decimal_places=2),
        ),
        migrations.AlterField(
            model_name='factura',
            name='valor_consulta',
            field=models.DecimalField(default=0, max_digits=10, verbose_name='Valor Consulta', decimal_places=2),
        ),
        migrations.AlterField(
            model_name='factura',
            name='valor_honorarios',
            field=models.DecimalField(default=0, max_digits=10, verbose_name='Honorarios Medico', decimal_places=2),
        ),
        migrations.AlterField(
            model_name='factura',
            name='valor_sala',
            field=models.DecimalField(default=0, max_digits=10, verbose_name='Derechos de Sala', decimal_places=2),
        ),
        migrations.AlterField(
            model_name='factura',
            name='valor_sutura',
            field=models.DecimalField(default=0, max_digits=10, verbose_name='Materiales de Sutura', decimal_places=2),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.PositiveIntegerField(default=0, verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='stock',
            field=models.PositiveIntegerField(default=0, verbose_name='Cantidad'),
        ),
    ]
