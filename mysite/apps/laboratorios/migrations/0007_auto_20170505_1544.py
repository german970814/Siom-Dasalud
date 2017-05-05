# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorios', '0006_auto_20170503_1743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formato',
            name='campos',
        ),
        migrations.RemoveField(
            model_name='formato',
            name='observacion',
        ),
        migrations.AddField(
            model_name='formato',
            name='formato',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Campo',
        ),
    ]
