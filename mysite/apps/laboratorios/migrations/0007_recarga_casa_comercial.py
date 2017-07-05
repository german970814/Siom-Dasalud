# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorios', '0006_auto_20170624_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='recarga',
            name='casa_comercial',
            field=models.CharField(verbose_name='Casa comercial', max_length=100, blank=True),
        ),
    ]
