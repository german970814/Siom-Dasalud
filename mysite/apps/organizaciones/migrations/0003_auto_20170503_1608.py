# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizaciones', '0002_auto_20170427_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='afp',
            name='documento',
            field=models.CharField(default=b'NI', max_length=2, verbose_name='Documento', choices=[(b'NI', b'Nro de Id Tributaria'), (b'CC', b'C\xc3\xa9dula de Ciudadan\xc3\xada'), (b'CE', b'C\xc3\xa9dula de Extranjer\xc3\xada'), (b'PA', b'Pasaporte')]),
        ),
        migrations.AlterField(
            model_name='arp',
            name='documento',
            field=models.CharField(default=b'NI', max_length=2, verbose_name='Documento', choices=[(b'NI', b'Nro de Id Tributaria'), (b'CC', b'C\xc3\xa9dula de Ciudadan\xc3\xada'), (b'CE', b'C\xc3\xa9dula de Extranjer\xc3\xada'), (b'PA', b'Pasaporte')]),
        ),
        migrations.AlterField(
            model_name='empresas',
            name='dias',
            field=models.IntegerField(null=True, verbose_name=b'D\xc3\xadas Vence Factura', blank=True),
        ),
        migrations.AlterField(
            model_name='eps',
            name='documento',
            field=models.CharField(default=b'NI', max_length=2, verbose_name='Documento', choices=[(b'NI', b'Nro de Id Tributaria'), (b'CC', b'C\xc3\xa9dula de Ciudadan\xc3\xada'), (b'CE', b'C\xc3\xa9dula de Extranjer\xc3\xada'), (b'PA', b'Pasaporte')]),
        ),
        migrations.AlterField(
            model_name='instituciones',
            name='documento',
            field=models.CharField(max_length=2, verbose_name='Documento', choices=[(b'NI', b'Nro de Id Tributaria'), (b'CC', b'C\xc3\xa9dula de Ciudadan\xc3\xada'), (b'CE', b'C\xc3\xa9dula de Extranjer\xc3\xada'), (b'PA', b'Pasaporte')]),
        ),
    ]
