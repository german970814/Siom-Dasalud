# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorios', '0003_auto_20170503_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='input',
            name='campo_ptr',
        ),
        migrations.RemoveField(
            model_name='select',
            name='campo_ptr',
        ),
        migrations.RemoveField(
            model_name='select',
            name='value',
        ),
        migrations.RemoveField(
            model_name='textarea',
            name='campo_ptr',
        ),
        migrations.RemoveField(
            model_name='campo',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='campo',
            name='object_id',
        ),
        migrations.AddField(
            model_name='campo',
            name='tipo',
            field=models.CharField(default='text', max_length=10, choices=[('text', 'Texto'), ('checkbox', 'Muchas Opciones'), ('radio', '\xdanica Opci\xf3n'), ('select', 'Selecci\xf3n'), ('textarea', 'Texto Libre')]),
        ),
        migrations.AddField(
            model_name='formato',
            name='campos',
            field=models.ManyToManyField(related_name='formatos', to='laboratorios.Campo'),
        ),
        migrations.AddField(
            model_name='formato',
            name='laboratorio',
            field=models.OneToOneField(related_name='formato', default=1, verbose_name='Laboratorio', to='laboratorios.Laboratorio'),
            preserve_default=False,
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
