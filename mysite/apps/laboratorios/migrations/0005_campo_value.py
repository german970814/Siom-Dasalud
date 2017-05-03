# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorios', '0004_auto_20170503_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='campo',
            name='value',
            field=models.TextField(max_length=255, null=True, verbose_name='Valor', blank=True),
        ),
    ]
