# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('laboratorios', '0005_resultado_cerrado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=255, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=255, verbose_name='Apellidos')),
                ('documento', models.CharField(max_length=100, verbose_name='Documento')),
                ('usuario', models.OneToOneField(verbose_name='Usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='recepcion',
            name='empleado',
            field=models.ForeignKey(related_name='recepciones', default=1, verbose_name='Empleado', to='laboratorios.Empleado'),
            preserve_default=False,
        ),
    ]
