# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0003_auto_20170427_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='fecha_atencion',
            field=models.DateField(default=datetime.date.today, verbose_name=b'Fecha Atenci\xc3\xb3n'),
        ),
    ]
