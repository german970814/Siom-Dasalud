# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorios', '0010_auto_20170920_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hojagasto',
            name='orden',
            field=models.ForeignKey(verbose_name='Orden', blank=True, null=True, related_name='hojas_gasto', to='historias.orden'),
        ),
    ]
