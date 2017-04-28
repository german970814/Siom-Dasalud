# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import mysite.apps.datos.models


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0002_auto_20170329_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='estado',
            field=models.CharField(default='A', choices=[('A', 'Activo'), ('I', 'Inactivo')], verbose_name='Estado', max_length=1),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='afiliado',
            field=models.CharField(default='N', choices=[('C', 'Cotizante'), ('B', 'Beneficiario'), ('A', 'Adicional'), ('N', 'Ninguno')], verbose_name='Tipo Afiliado', max_length=1),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='documento',
            field=models.CharField(choices=[('CC', 'Cédula Ciudadanía'), ('CE', 'Cédula de Extranjería'), ('PA', 'Pasaporte'), ('RC', 'Registro Civil'), ('TI', 'Tarjeta de Identidad'), ('AS', 'Adulto sin Identificar'), ('MS', 'Menor sin Identificar'), ('UN', 'Numero Unico de Identificación')], verbose_name='Documento', max_length=2),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='escolaridad',
            field=models.CharField(default='U', choices=[('P', 'Primaria'), ('S', 'Secundaria'), ('T', 'Tecnico'), ('R', 'Tecnologo'), ('U', 'Universitaria')], verbose_name='Escalonaridad', max_length=1),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='estadoCivil',
            field=models.CharField(choices=[('C', 'Casado'), ('U', 'Union Libre'), ('S', 'Soltero'), ('V', 'Viudo'), ('D', 'Divorciado')], verbose_name='Estado Civil', max_length=1),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='fecha_nacimiento',
            field=models.DateField(verbose_name='Fecha de Nacimiento'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='firma',
            field=models.ImageField(null=True, upload_to=mysite.apps.datos.models.paciente.url, blank=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='foto',
            field=models.ImageField(null=True, upload_to=mysite.apps.datos.models.paciente.url, blank=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='genero',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], verbose_name='Genero', max_length=1),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='tipo',
            field=models.CharField(default='4', choices=[('1', 'Contributivo'), ('2', 'Subsidiado'), ('3', 'Vinculado'), ('4', 'Particular'), ('5', 'Otro')], verbose_name='Tipo Usuario', max_length=1),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='unidad',
            field=models.CharField(default='A', choices=[('1', 'Años'), ('2', 'Meses'), ('3', 'Días')], verbose_name='Unidad Edad', max_length=1),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='visita',
            field=models.DateField(default=datetime.date.today, verbose_name='Ultima Visita'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='zona',
            field=models.CharField(default='U', choices=[('U', 'Urbano'), ('R', 'Rural')], verbose_name='Zona Residencia', max_length=1),
        ),
    ]
