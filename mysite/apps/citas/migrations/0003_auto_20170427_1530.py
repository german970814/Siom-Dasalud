# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citas', '0002_auto_20170329_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citas_consulta',
            name='documento',
            field=models.CharField(choices=[('CC', 'Cédula Ciudadanía'), ('CE', 'Cédula de Extranjería'), ('PA', 'Pasaporte'), ('RC', 'Registro Civil'), ('TI', 'Tarjeta de Identidad'), ('AS', 'Adulto sin Identificar'), ('MS', 'Menor sin Identificar'), ('UN', 'Numero Unico de Identificación')], verbose_name='Documento', max_length=2),
        ),
        migrations.AlterField(
            model_name='citas_procedimiento',
            name='documento',
            field=models.CharField(choices=[('CC', 'Cédula Ciudadanía'), ('CE', 'Cédula de Extranjería'), ('PA', 'Pasaporte'), ('RC', 'Registro Civil'), ('TI', 'Tarjeta de Identidad'), ('AS', 'Adulto sin Identificar'), ('MS', 'Menor sin Identificar'), ('UN', 'Numero Unico de Identificación')], verbose_name='Documento', max_length=2),
        ),
    ]
