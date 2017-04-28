# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametros', '0002_auto_20170427_1530'),
        ('laboratorios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='laboratorio',
            name='servicio',
            field=models.OneToOneField(to='parametros.servicios', related_name='laboratorio', default=1),
            preserve_default=False,
        ),
    ]
