# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorios', '0011_auto_20170920_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultado',
            name='comentario',
            field=models.TextField(blank=True, null=True),
        ),
    ]
