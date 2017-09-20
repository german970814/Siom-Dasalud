# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorios', '0009_auto_20170718_1636'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bacteriologo',
            options={'permissions': (('es_administrador', 'Administrador'),)},
        ),
    ]
