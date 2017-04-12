# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('parametros', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organizaciones', '0001_initial'),
        ('datos', '0002_auto_20170329_1809'),
        ('historias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordenesproducto',
            name='servicio',
            field=models.ForeignKey(related_name='ordenProducto_servicio', verbose_name='Servicio', to='parametros.serviciosEmpresa'),
        ),
        migrations.AddField(
            model_name='orden',
            name='empresa',
            field=models.ForeignKey(related_name='orden_empresa', verbose_name='Empresa que ordena', to='organizaciones.empresas'),
        ),
        migrations.AddField(
            model_name='orden',
            name='generadapor',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='orden',
            name='institucion',
            field=models.ForeignKey(related_name='ordeninstitucion_empresa', verbose_name='Institucion a la que Pertenece', to='organizaciones.instituciones'),
        ),
        migrations.AddField(
            model_name='orden',
            name='medico',
            field=models.ForeignKey(related_name='orden_medico', to='datos.medico'),
        ),
        migrations.AddField(
            model_name='orden',
            name='paciente',
            field=models.ForeignKey(related_name='orden_paciente', to='datos.paciente'),
        ),
        migrations.AddField(
            model_name='laboratorios',
            name='orden',
            field=models.ForeignKey(related_name='laboratorios_orden', to='historias.orden'),
        ),
        migrations.AddField(
            model_name='historia_procedimientos',
            name='complicacion',
            field=models.ForeignKey(related_name='procedimiento_complicacion_cie', verbose_name='Complicacion', blank=True, to='parametros.cie', null=True),
        ),
        migrations.AddField(
            model_name='historia_procedimientos',
            name='diagnostico',
            field=models.ForeignKey(related_name='procedimiento_diagnostico_cie', verbose_name='Diagnostico', blank=True, to='parametros.cie', null=True),
        ),
        migrations.AddField(
            model_name='historia_procedimientos',
            name='diagnostico1',
            field=models.ForeignKey(related_name='procedimiento_diagnostico1_cie', verbose_name='Diagnostico 1', blank=True, to='parametros.cie', null=True),
        ),
        migrations.AddField(
            model_name='historia_procedimientos',
            name='orden',
            field=models.ForeignKey(related_name='procedimiento_orden', to='historias.orden'),
        ),
        migrations.AddField(
            model_name='historia_procedimientos',
            name='paciente',
            field=models.ForeignKey(related_name='historia_procedimientos_paciente', to='datos.paciente'),
        ),
        migrations.AddField(
            model_name='historia_procedimientos',
            name='procedimiento',
            field=models.ForeignKey(related_name='procedimiento_empresa', to='parametros.procedimientos'),
        ),
        migrations.AddField(
            model_name='historia_clinica',
            name='afp',
            field=models.ForeignKey(related_name='historia_afp', to='organizaciones.arp'),
        ),
        migrations.AddField(
            model_name='historia_clinica',
            name='arl',
            field=models.ForeignKey(related_name='historia_arl', to='organizaciones.arp'),
        ),
        migrations.AddField(
            model_name='historia_clinica',
            name='eps',
            field=models.ForeignKey(related_name='historia_eps', to='organizaciones.eps'),
        ),
        migrations.AddField(
            model_name='historia_clinica',
            name='orden',
            field=models.ForeignKey(related_name='historia_orden', to='historias.orden'),
        ),
        migrations.AddField(
            model_name='historia_clinica',
            name='paciente',
            field=models.ForeignKey(related_name='historia_paciente', to='datos.paciente'),
        ),
    ]
