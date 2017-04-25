# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import mysite.apps.laboratorios.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('historias', '__first__'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bacteriologo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50, verbose_name='Código')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('registro', models.IntegerField(verbose_name='Registro')),
                ('otros', models.CharField(max_length=255, null=True, blank=True, verbose_name='Otros')),
                ('firma', models.FileField(null=True, upload_to=mysite.apps.laboratorios.models.ruta_imagen_bacteriologo, blank=True)),
                ('usuario', models.OneToOneField(verbose_name='Usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BancoReactivo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
            ],
        ),
        migrations.CreateModel(
            name='Caracteristica',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50, verbose_name='Código')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50, verbose_name='Código')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='EspecificacionCaracteristica',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('caracteristica', models.ForeignKey(verbose_name='Caracteristica', to='laboratorios.Caracteristica', related_name='especificaciones')),
            ],
        ),
        migrations.CreateModel(
            name='Formato',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('observacion', models.TextField(null=True, blank=True, verbose_name='Observación')),
                ('referencia', models.CharField(max_length=255, null=True, blank=True, verbose_name='Referencia')),
                ('unidades', models.CharField(max_length=100, null=True, blank=True, verbose_name='Unidades')),
            ],
        ),
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('label', models.CharField(max_length=150, verbose_name='Label')),
                ('help_text', models.CharField(max_length=255, null=True, blank=True, verbose_name='Ayuda')),
                ('value', models.CharField(max_length=255, verbose_name='Valor')),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50, verbose_name='Código')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('codigo_internacional', models.CharField(max_length=50, null=True, blank=True, verbose_name='Código Internacional')),
                ('equipo', models.ForeignKey(verbose_name='Equipo', to='laboratorios.Equipo', related_name='laboratorios')),
            ],
        ),
        migrations.CreateModel(
            name='Reactivo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50, verbose_name='Código')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('alarma_inferior', models.IntegerField(null=True, blank=True, verbose_name='Alarma inferior')),
                ('alarma_media', models.IntegerField(null=True, blank=True, verbose_name='Alarma media')),
                ('costos', models.IntegerField(verbose_name='Costo')),
                ('laboratorio', models.ForeignKey(verbose_name='Laboratorio', to='laboratorios.Laboratorio', related_name='reactivos')),
            ],
        ),
        migrations.CreateModel(
            name='Recarga',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('reactivo', models.ForeignKey(verbose_name='Reactivo', to='laboratorios.Reactivo', related_name='recargas')),
            ],
        ),
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('bacteriologo', models.ForeignKey(verbose_name='Bacterioogo', to='laboratorios.Bacteriologo', related_name='resultados')),
                ('laboratorio', models.ForeignKey(verbose_name='Laboratorio', to='laboratorios.Laboratorio', related_name='resultados')),
                ('orden', models.ForeignKey(verbose_name='Orden', to='historias.orden', related_name='resultados_laboratorio')),
            ],
        ),
        migrations.CreateModel(
            name='SeccionTrabajo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50, verbose_name='Código')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
            ],
            options={
                'verbose_name_plural': 'Secciones de Trabajo',
                'verbose_name': 'Sección de Trabajo',
            },
        ),
        migrations.CreateModel(
            name='Select',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('label', models.CharField(max_length=150, verbose_name='Label')),
                ('help_text', models.CharField(max_length=255, null=True, blank=True, verbose_name='Ayuda')),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('value', models.ForeignKey(verbose_name='Valor', to='laboratorios.Caracteristica')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tecnica',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50, verbose_name='Código')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='TextArea',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('label', models.CharField(max_length=150, verbose_name='Label')),
                ('help_text', models.CharField(max_length=255, null=True, blank=True, verbose_name='Ayuda')),
                ('value', models.TextField(verbose_name='Valor')),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='laboratorio',
            name='seccion_trabajo',
            field=models.ForeignKey(verbose_name='Seccion de Trabajo', to='laboratorios.SeccionTrabajo', related_name='laboratorios'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='tecnica',
            field=models.ForeignKey(verbose_name='Tecnica', to='laboratorios.Tecnica', related_name='equipos'),
        ),
        migrations.AddField(
            model_name='bancoreactivo',
            name='reactivo',
            field=models.OneToOneField(verbose_name='Reactivo', to='laboratorios.Reactivo', related_name='banco_reactivo'),
        ),
    ]
