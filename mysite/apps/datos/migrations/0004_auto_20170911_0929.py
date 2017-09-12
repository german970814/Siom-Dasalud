# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mysite.apps.datos.models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0003_auto_20170522_1252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='usuario',
        ),
        migrations.AlterField(
            model_name='medico',
            name='estado',
            field=models.CharField(verbose_name='Estado', max_length=1, default='A', choices=[('A', 'Activo'), ('I', 'Inactivo')]),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='afiliado',
            field=models.CharField(verbose_name='Tipo Afiliado', max_length=1, default='N', choices=[('C', 'Cotizante'), ('B', 'Beneficiario'), ('A', 'Adicional'), ('N', 'Ninguno')]),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='documento',
            field=models.CharField(verbose_name='Documento', max_length=2, choices=[('CC', 'Cédula Ciudadanía'), ('CE', 'Cédula de Extranjería'), ('PA', 'Pasaporte'), ('RC', 'Registro Civil'), ('TI', 'Tarjeta de Identidad'), ('AS', 'Adulto sin Identificar'), ('MS', 'Menor sin Identificar'), ('UN', 'Numero Unico de Identificación')]),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='escolaridad',
            field=models.CharField(verbose_name='Escalonaridad', max_length=1, default='U', choices=[('P', 'Primaria'), ('S', 'Secundaria'), ('T', 'Tecnico'), ('R', 'Tecnologo'), ('U', 'Universitaria')]),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='estadoCivil',
            field=models.CharField(verbose_name='Estado Civil', max_length=1, choices=[('C', 'Casado'), ('U', 'Union Libre'), ('S', 'Soltero'), ('V', 'Viudo'), ('D', 'Divorciado')]),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='fecha_nacimiento',
            field=models.DateField(verbose_name='Fecha de Nacimiento'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='firma',
            field=models.ImageField(blank=True, null=True, upload_to=mysite.apps.datos.models.paciente.url),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to=mysite.apps.datos.models.paciente.url),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='genero',
            field=models.CharField(verbose_name='Genero', max_length=1, choices=[('M', 'Masculino'), ('F', 'Femenino')]),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='tipo',
            field=models.CharField(verbose_name='Tipo Usuario', max_length=1, default='4', choices=[('1', 'Contributivo'), ('2', 'Subsidiado'), ('3', 'Vinculado'), ('4', 'Particular'), ('5', 'Otro')]),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='unidad',
            field=models.CharField(verbose_name='Unidad Edad', max_length=1, default='A', choices=[('1', 'Años'), ('2', 'Meses'), ('3', 'Días')]),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='visita',
            field=models.DateField(verbose_name='Ultima Visita', default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='zona',
            field=models.CharField(verbose_name='Zona Residencia', max_length=1, default='U', choices=[('U', 'Urbano'), ('R', 'Rural')]),
        ),
    ]
