# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def eliminar_usuarios_sin_uso(apps, schema_editor):
    """
    Elimina los usuarios que no están siendo usados actualmente en la aplicación.
    """
    User = apps.get_model('auth', 'User')
    # EmpleadoExamenes = apps.get_model('mysite.examenes', 'Empleado')
    # Empleado = apps.get_model('mysite.laboratorios', 'Empleado')
    # Paciente = apps.get_model('datos', 'Paciente')

    for user in User.objects.exclude(groups__isnull=False).exclude(
        is_superuser=True).exclude(empleado_examenes__isnull=False).exclude(
        empleado__isnull=False).exclude(userprofile__isnull=False).distinct():
        user.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0004_auto_20170911_0929'),
        ('examenes', '0003_auto_20170830_1208'),
        ('laboratorios', '0009_auto_20170718_1636'),
        ('home', '0002_auto_20170329_1809'),
    ]

    operations = [
        migrations.RunPython(eliminar_usuarios_sin_uso, reverse_code=migrations.RunPython.noop)
    ]
