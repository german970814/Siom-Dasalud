# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mysite.apps.laboratorios.models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorios', '0007_recarga_casa_comercial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultado',
            name='archivo',
            field=models.FileField(verbose_name='Archivo', blank=True, null=True, upload_to=mysite.apps.laboratorios.models.ruta_archivo_resultado),
        ),
    ]
