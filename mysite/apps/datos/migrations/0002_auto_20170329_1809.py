# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organizaciones', '0001_initial'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='ciudad',
            field=models.ForeignKey(related_name='pacientes_departamento_ciudad', verbose_name='Ciudad', to='home.departamentos'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='institucion',
            field=models.ForeignKey(related_name='paciente_institucion', verbose_name='Institucion que lo atendio', to='organizaciones.instituciones'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='nacioen',
            field=models.ForeignKey(related_name='pacientes_departamento_nacimiento', verbose_name='Nacio en', to='home.departamentos'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='procede',
            field=models.ForeignKey(related_name='paciente_empresa', verbose_name='Procede de', to='organizaciones.empresas'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='profesion',
            field=models.ForeignKey(verbose_name='Profesion', to='datos.profesiones'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='medico',
            name='especialidad',
            field=models.ForeignKey(verbose_name='Especialista en', to='datos.especialidades'),
        ),
        migrations.AddField(
            model_name='medico',
            name='institucion',
            field=models.ForeignKey(related_name='medico_institucion', verbose_name='Institucion a la que pertenece', to='organizaciones.instituciones'),
        ),
        migrations.AddField(
            model_name='medico',
            name='usuario',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
