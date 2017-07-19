# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historias', '0002_auto_20170329_1809'),
        ('laboratorios', '0003_auto_20170610_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recepcion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado', models.CharField(default='TO', max_length=2, verbose_name='Estado', choices=[('TO', 'TOMA DE MUESTRA'), ('EC', 'EN CURSO'), ('RE', 'RESULTADO EMITIDO')])),
                ('orden', models.OneToOneField(related_name='recepcion', verbose_name='Orden', to='historias.orden')),
            ],
        ),
    ]
