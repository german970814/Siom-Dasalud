# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('laboratorios', '0002_laboratorio_servicio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('label', models.CharField(max_length=150, verbose_name='Label')),
                ('help_text', models.CharField(max_length=255, null=True, verbose_name='Ayuda', blank=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
        ),
        migrations.RemoveField(
            model_name='input',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='input',
            name='help_text',
        ),
        migrations.RemoveField(
            model_name='input',
            name='id',
        ),
        migrations.RemoveField(
            model_name='input',
            name='label',
        ),
        migrations.RemoveField(
            model_name='input',
            name='name',
        ),
        migrations.RemoveField(
            model_name='input',
            name='object_id',
        ),
        migrations.RemoveField(
            model_name='select',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='select',
            name='help_text',
        ),
        migrations.RemoveField(
            model_name='select',
            name='id',
        ),
        migrations.RemoveField(
            model_name='select',
            name='label',
        ),
        migrations.RemoveField(
            model_name='select',
            name='name',
        ),
        migrations.RemoveField(
            model_name='select',
            name='object_id',
        ),
        migrations.RemoveField(
            model_name='textarea',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='textarea',
            name='help_text',
        ),
        migrations.RemoveField(
            model_name='textarea',
            name='id',
        ),
        migrations.RemoveField(
            model_name='textarea',
            name='label',
        ),
        migrations.RemoveField(
            model_name='textarea',
            name='name',
        ),
        migrations.RemoveField(
            model_name='textarea',
            name='object_id',
        ),
        migrations.AddField(
            model_name='bacteriologo',
            name='areas',
            field=models.ManyToManyField(related_name='bacteriologos', verbose_name='\xc1reas', to='laboratorios.SeccionTrabajo'),
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
        migrations.AddField(
            model_name='input',
            name='campo_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=1, serialize=False, to='laboratorios.Campo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='select',
            name='campo_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=1, serialize=False, to='laboratorios.Campo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='textarea',
            name='campo_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=1, serialize=False, to='laboratorios.Campo'),
            preserve_default=False,
        ),
    ]
