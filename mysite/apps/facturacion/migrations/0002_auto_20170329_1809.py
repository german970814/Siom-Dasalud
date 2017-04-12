# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0001_initial'),
        ('historias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='orden',
            field=models.OneToOneField(related_name='factura_orden', to='historias.orden'),
        ),
        migrations.AddField(
            model_name='detalle',
            name='factura',
            field=models.ForeignKey(related_name='detalle_factura', to='facturacion.factura'),
        ),
        migrations.AddField(
            model_name='detalle',
            name='producto',
            field=models.ForeignKey(related_name='detalle_producto', to='facturacion.producto'),
        ),
    ]
