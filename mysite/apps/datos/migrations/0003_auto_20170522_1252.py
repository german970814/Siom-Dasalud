# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mysite.apps.datos.models


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0002_auto_20170329_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='firma',
            field=models.ImageField(null=True, upload_to=mysite.apps.datos.models.url, blank=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='foto',
            field=models.ImageField(null=True, upload_to=mysite.apps.datos.models.url, blank=True),
        ),
    ]
