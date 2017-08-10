# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examenes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visiometria',
            name='add_od',
            field=models.CharField(verbose_name='ADD', max_length=50, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='visiometria',
            name='add_oi',
            field=models.CharField(verbose_name='ADD', max_length=50, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='visiometria',
            name='alt_od',
            field=models.CharField(verbose_name='ALT', max_length=50, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='visiometria',
            name='alt_oi',
            field=models.CharField(verbose_name='ALT', max_length=50, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='visiometria',
            name='av',
            field=models.CharField(verbose_name='AV', max_length=2, blank=True, null=True, choices=[('OD', 'OJO DERECHO'), ('OI', 'OJO IZQUIERDO'), ('AO', 'AMBOS OJOS')]),
        ),
        migrations.AlterField(
            model_name='visiometria',
            name='campimetria',
            field=models.CharField(verbose_name='Campimetría', max_length=100, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='visiometria',
            name='cil_od',
            field=models.CharField(verbose_name='CIL', max_length=50, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='visiometria',
            name='cil_oi',
            field=models.CharField(verbose_name='CIL', max_length=50, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='visiometria',
            name='dp_od',
            field=models.CharField(verbose_name='D.P', max_length=50, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='visiometria',
            name='dp_oi',
            field=models.CharField(verbose_name='D.P', max_length=50, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='visiometria',
            name='eje_od',
            field=models.CharField(verbose_name='EJE', max_length=50, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='visiometria',
            name='eje_oi',
            field=models.CharField(verbose_name='EJE', max_length=50, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='visiometria',
            name='esf_od',
            field=models.CharField(verbose_name='ESF', max_length=50, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='visiometria',
            name='esf_oi',
            field=models.CharField(verbose_name='ESF', max_length=50, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='visiometria',
            name='foria',
            field=models.CharField(verbose_name='Foria', max_length=100, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='visiometria',
            name='np_od',
            field=models.CharField(verbose_name='N.P', max_length=50, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='visiometria',
            name='np_oi',
            field=models.CharField(verbose_name='N.P', max_length=50, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='visiometria',
            name='prisma_od',
            field=models.CharField(verbose_name='PRISMA', max_length=50, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='visiometria',
            name='prisma_oi',
            field=models.CharField(verbose_name='PRISMA', max_length=50, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='visiometria',
            name='recomendaciones',
            field=models.TextField(verbose_name='Recomendaciones', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='visiometria',
            name='vision_cercana',
            field=models.CharField(verbose_name='Vision cercana', max_length=2, blank=True, null=True, choices=[('OD', 'OJO DERECHO'), ('OI', 'OJO IZQUIERDO'), ('AO', 'AMBOS OJOS')]),
        ),
        migrations.AlterField(
            model_name='visiometria',
            name='vision_lejana',
            field=models.CharField(verbose_name='Vision lejana', max_length=2, blank=True, null=True, choices=[('OD', 'OJO DERECHO'), ('OI', 'OJO IZQUIERDO'), ('AO', 'AMBOS OJOS')]),
        ),
    ]
