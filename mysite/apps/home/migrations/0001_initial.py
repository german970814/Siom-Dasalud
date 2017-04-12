# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='departamentos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=2)),
                ('codigo_municipio', models.CharField(max_length=4)),
                ('codigo_poblado', models.CharField(max_length=10)),
                ('nombre_depto', models.CharField(max_length=50)),
                ('nombre_municipio', models.CharField(max_length=50)),
                ('nombre_poblado', models.CharField(max_length=50)),
                ('tipo_poblado', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='userProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'permissions': (('es_administrador', 'Administrador'), ('es_coordinador_general', 'Coordinador General'), ('es_coordinador_plataforma', 'Coordinador Plataforma'), ('es_coordinador_endoscopia', 'Coordinador Endoscopia'), ('es_auxiliar_plataforma', 'Auxiliar Plataforma'), ('es_auxiliar_endoscopia', 'Auxiliar Endoscopia'), ('es_auxiliar_contabilidad', 'Auxiliar Contabilidad'), ('es_auxiliar_enfermeria', 'Auxiliar Enfermeria'), ('es_doctor', 'Doctor')),
            },
        ),
    ]
