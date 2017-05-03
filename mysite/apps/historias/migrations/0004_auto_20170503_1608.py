# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historias', '0003_auto_20170427_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historia_clinica',
            name='a_erg1',
            field=models.CharField(default=b'4', max_length=1, choices=[(b'1', b'Posturas'), (b'2', b'Reubicaci\xc3\xb3n de Puesto'), (b'3', b'Otros'), (b'4', b'Ninguno')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='a_erg2',
            field=models.CharField(default=b'4', max_length=1, choices=[(b'1', b'Posturas'), (b'2', b'Reubicaci\xc3\xb3n de Puesto'), (b'3', b'Otros'), (b'4', b'Ninguno')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='a_fis1',
            field=models.CharField(default=b'B', max_length=1, choices=[(b'1', b'Quemaduras por Electricidad 1er grado'), (b'2', b'Quemaduras por Electricidad  2do grado'), (b'3', b'Quemaduras por Electricidad  3er grado'), (b'4', b'Altas temperaturas'), (b'5', b'Bajas temperaturas'), (b'6', b'Iluminaci\xc3\xb3n'), (b'7', b'Radiaciones'), (b'8', b'Vibraciones'), (b'9', b'Ruido'), (b'A', b'Otros'), (b'B', b'Ninguno')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='a_fis2',
            field=models.CharField(default=b'B', max_length=1, choices=[(b'1', b'Quemaduras por Electricidad 1er grado'), (b'2', b'Quemaduras por Electricidad  2do grado'), (b'3', b'Quemaduras por Electricidad  3er grado'), (b'4', b'Altas temperaturas'), (b'5', b'Bajas temperaturas'), (b'6', b'Iluminaci\xc3\xb3n'), (b'7', b'Radiaciones'), (b'8', b'Vibraciones'), (b'9', b'Ruido'), (b'A', b'Otros'), (b'B', b'Ninguno')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='a_mec1',
            field=models.CharField(default=b'5', max_length=1, choices=[(b'1', b'Ca\xc3\xaddas'), (b'2', b'Contusiones'), (b'3', b'Torceduras'), (b'4', b'Otros'), (b'5', b'Ninguno')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='a_mec2',
            field=models.CharField(default=b'5', max_length=1, choices=[(b'1', b'Ca\xc3\xaddas'), (b'2', b'Contusiones'), (b'3', b'Torceduras'), (b'4', b'Otros'), (b'5', b'Ninguno')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='a_psi1',
            field=models.CharField(default=b'4', max_length=1, choices=[(b'1', b'Estr\xc3\xa9s laboral'), (b'2', b'Acoso laboral'), (b'3', b'Otros'), (b'4', b'Ninguno')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='a_psi2',
            field=models.CharField(default=b'4', max_length=1, choices=[(b'1', b'Estr\xc3\xa9s laboral'), (b'2', b'Acoso laboral'), (b'3', b'Otros'), (b'4', b'Ninguno')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='planificacion',
            field=models.CharField(default=b'9', max_length=1, choices=[(b'1', b'Preservativo'), (b'2', b'Implante Subdermico'), (b'3', b'DIU'), (b'4', b'Pomeroy'), (b'5', b'Inyecci\xc3\xb3n'), (b'6', b'P\xc3\xadldora'), (b'7', b'Ritmo'), (b'8', b'Otros'), (b'9', b'Ninguno')]),
        ),
        migrations.AlterField(
            model_name='historia_procedimientos',
            name='forma',
            field=models.CharField(default=b'1', max_length=1, verbose_name='Forma de realizacion del acto quirurgico', choices=[(b'1', b'\xc3\x9anico o unilateral'), (b'2', b'Multiple o Bilateral misma via, diferente especialidad'), (b'3', b'Multiple o Bilateral misma via, igual especialidad'), (b'4', b'Multiple o Bilateral diferente via, diferente especialidad'), (b'5', b'Multiple o Bilateral diferente via, igual especialidad')]),
        ),
        migrations.AlterField(
            model_name='historia_procedimientos',
            name='personal',
            field=models.CharField(default=b'1', max_length=1, verbose_name='Personal que atiende', choices=[(b'1', b'M\xc3\xa9dico (a) especialista'), (b'2', b'M\xc3\xa9dico (a) general'), (b'3', b'Enfermera (o)'), (b'4', b'Auxiliar de enfermer\xc3\xada'), (b'5', b'Otro')]),
        ),
    ]
