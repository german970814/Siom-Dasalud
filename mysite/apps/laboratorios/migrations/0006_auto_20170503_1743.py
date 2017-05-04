# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorios', '0005_campo_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formato',
            name='referencia',
        ),
        migrations.RemoveField(
            model_name='formato',
            name='unidades',
        ),
        migrations.AddField(
            model_name='campo',
            name='referencia',
            field=models.CharField(max_length=255, null=True, verbose_name='Referencia', blank=True),
        ),
        migrations.AddField(
            model_name='campo',
            name='unidades',
            field=models.CharField(max_length=100, null=True, verbose_name='Unidades', blank=True),
        ),
    ]
