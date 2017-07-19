# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorios', '0008_resultado_archivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboratorio',
            name='equipo',
            field=models.ForeignKey(verbose_name='Equipo', blank=True, null=True, related_name='laboratorios', to='laboratorios.Equipo'),
        ),
    ]
