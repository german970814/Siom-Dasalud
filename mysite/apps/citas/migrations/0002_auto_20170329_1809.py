# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('parametros', '0001_initial'),
        ('datos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organizaciones', '0001_initial'),
        ('citas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='citas_procedimiento',
            name='empresa',
            field=models.ForeignKey(related_name='citas_procedimiento_empresa', verbose_name='Empresa a la que Pertenece', to='organizaciones.empresas'),
        ),
        migrations.AddField(
            model_name='citas_procedimiento',
            name='generadapor',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='citas_procedimiento',
            name='paciente',
            field=models.ForeignKey(related_name='citas_procedimiento_paciente', blank=True, to='datos.paciente', null=True),
        ),
        migrations.AddField(
            model_name='citas_procedimiento',
            name='procedimiento',
            field=models.ForeignKey(related_name='citas_procedimiento_procedimientos', to='parametros.procedimientos'),
        ),
        migrations.AddField(
            model_name='citas_consulta',
            name='agenda',
            field=models.OneToOneField(related_name='citas_consulta_agenda', to='citas.agenda_consulta'),
        ),
        migrations.AddField(
            model_name='citas_consulta',
            name='consulta',
            field=models.ForeignKey(related_name='citas_consulta_consultas', to='parametros.consultas'),
        ),
        migrations.AddField(
            model_name='citas_consulta',
            name='empresa',
            field=models.ForeignKey(related_name='citas_consulta_empresa', verbose_name='Empresa a la que Pertenece', to='organizaciones.empresas'),
        ),
        migrations.AddField(
            model_name='citas_consulta',
            name='generadapor',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='citas_consulta',
            name='paciente',
            field=models.ForeignKey(related_name='citas_consulta_paciente', blank=True, to='datos.paciente', null=True),
        ),
        migrations.AddField(
            model_name='agenda_procedimiento',
            name='medico',
            field=models.ForeignKey(related_name='agenda_procedimiento_medico', to='datos.medico'),
        ),
        migrations.AddField(
            model_name='agenda_consulta',
            name='medico',
            field=models.ForeignKey(related_name='agenda_consulta_medico', to='datos.medico'),
        ),
    ]
