# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametros', '0001_initial'),
        ('laboratorios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='input',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='select',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='select',
            name='value',
        ),
        migrations.RemoveField(
            model_name='textarea',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='formato',
            name='observacion',
        ),
        migrations.RemoveField(
            model_name='formato',
            name='referencia',
        ),
        migrations.RemoveField(
            model_name='formato',
            name='unidades',
        ),
        migrations.AddField(
            model_name='bacteriologo',
            name='areas',
            field=models.ManyToManyField(related_name='bacteriologos', verbose_name='\xc1reas', to='laboratorios.SeccionTrabajo'),
        ),
        migrations.AddField(
            model_name='formato',
            name='formato',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formato',
            name='laboratorio',
            field=models.OneToOneField(related_name='formato', default=1, verbose_name='Laboratorio', to='laboratorios.Laboratorio'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='laboratorio',
            name='servicio',
            field=models.OneToOneField(related_name='laboratorio', default=1, to='parametros.servicios'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resultado',
            name='resultado',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='resultado',
            name='bacteriologo',
            field=models.ForeignKey(related_name='resultados', verbose_name='Bacteri\xf3logo', to='laboratorios.Bacteriologo'),
        ),
        migrations.DeleteModel(
            name='Input',
        ),
        migrations.DeleteModel(
            name='Select',
        ),
        migrations.DeleteModel(
            name='TextArea',
        ),
    ]
