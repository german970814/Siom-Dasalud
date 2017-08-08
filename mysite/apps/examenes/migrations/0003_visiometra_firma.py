# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mysite.apps.examenes.models


class Migration(migrations.Migration):

    dependencies = [
        ('examenes', '0002_auto_20170802_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='visiometra',
            name='firma',
            field=models.FileField(blank=True, null=True, upload_to=mysite.apps.examenes.models.ruta_imagen_visiometra),
        ),
    ]
