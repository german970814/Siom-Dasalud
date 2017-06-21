# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorios', '0004_recepcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultado',
            name='cerrado',
            field=models.NullBooleanField(default=False, verbose_name='Cerrado'),
        ),
    ]
