# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citas', '0003_auto_20170427_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citas_consulta',
            name='documento',
            field=models.CharField(max_length=2, verbose_name='Documento', choices=[(b'CC', b'C\xc3\xa9dula Ciudadan\xc3\xada'), (b'CE', b'C\xc3\xa9dula de Extranjer\xc3\xada'), (b'PA', b'Pasaporte'), (b'RC', b'Registro Civil'), (b'TI', b'Tarjeta de Identidad'), (b'AS', b'Adulto sin Identificar'), (b'MS', b'Menor sin Identificar'), (b'UN', b'Numero Unico de Identificaci\xc3\xb3n')]),
        ),
        migrations.AlterField(
            model_name='citas_procedimiento',
            name='documento',
            field=models.CharField(max_length=2, verbose_name='Documento', choices=[(b'CC', b'C\xc3\xa9dula Ciudadan\xc3\xada'), (b'CE', b'C\xc3\xa9dula de Extranjer\xc3\xada'), (b'PA', b'Pasaporte'), (b'RC', b'Registro Civil'), (b'TI', b'Tarjeta de Identidad'), (b'AS', b'Adulto sin Identificar'), (b'MS', b'Menor sin Identificar'), (b'UN', b'Numero Unico de Identificaci\xc3\xb3n')]),
        ),
    ]
