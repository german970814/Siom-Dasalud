# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mysite.apps.examenes.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('historias', '0003_auto_20170801_1706'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('nombre', models.CharField(verbose_name='Nombre', max_length=200)),
                ('firma', models.FileField(blank=True, null=True, upload_to=mysite.apps.examenes.models.ruta_imagen_empleado)),
                ('usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL, verbose_name='Usuario', related_name='empleado_examenes')),
            ],
            options={
                'permissions': (('audiometra', 'Es usuario de Audiometría'), ('visiometra', 'Es usuario de Visiometría'), ('optometra', 'Es usuario de Optometría')),
            },
        ),
        migrations.CreateModel(
            name='Visiometria',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('lentes_correctivos', models.NullBooleanField(verbose_name='Usa Lentes Correctivos')),
                ('hace_cuanto', models.CharField(verbose_name='Hace cuanto tiempo', blank=True, null=True, max_length=100)),
                ('cirugia', models.CharField(verbose_name='Cirugía', blank=True, null=True, max_length=50)),
                ('trauma_ocular', models.CharField(verbose_name='Trauma Ocular', blank=True, null=True, max_length=50)),
                ('pterigio', models.CharField(verbose_name='Pterigio', blank=True, null=True, max_length=50)),
                ('colores', models.CharField(verbose_name='Colores', blank=True, null=True, max_length=50)),
                ('vision_lejana_od', models.CharField(verbose_name='Ojo Derecho', blank=True, null=True, max_length=50)),
                ('vision_lejana_oi', models.CharField(verbose_name='Ojo Izquierdo', blank=True, null=True, max_length=50)),
                ('vision_lejana_ao', models.CharField(verbose_name='Ambos ojos', blank=True, null=True, max_length=50)),
                ('vision_cercana_od', models.CharField(verbose_name='Ojo Derecho', blank=True, null=True, max_length=50)),
                ('vision_cercana_oi', models.CharField(verbose_name='Ojo Izquierdo', blank=True, null=True, max_length=50)),
                ('vision_cercana_ao', models.CharField(verbose_name='Ambos ojos', blank=True, null=True, max_length=50)),
                ('av_od', models.CharField(verbose_name='Ojo Derecho', blank=True, null=True, max_length=50)),
                ('av_oi', models.CharField(verbose_name='Ojo Izquierdo', blank=True, null=True, max_length=50)),
                ('av_ao', models.CharField(verbose_name='Ambos ojos', blank=True, null=True, max_length=50)),
                ('esf_od', models.CharField(verbose_name='ESF', blank=True, null=True, max_length=50)),
                ('cil_od', models.CharField(verbose_name='CIL', blank=True, null=True, max_length=50)),
                ('eje_od', models.CharField(verbose_name='EJE', blank=True, null=True, max_length=50)),
                ('add_od', models.CharField(verbose_name='ADD', blank=True, null=True, max_length=50)),
                ('dp_od', models.CharField(verbose_name='D.P', blank=True, null=True, max_length=50)),
                ('np_od', models.CharField(verbose_name='N.P', blank=True, null=True, max_length=50)),
                ('alt_od', models.CharField(verbose_name='ALT', blank=True, null=True, max_length=50)),
                ('prisma_od', models.CharField(verbose_name='PRISMA', blank=True, null=True, max_length=50)),
                ('esf_oi', models.CharField(verbose_name='ESF', blank=True, null=True, max_length=50)),
                ('cil_oi', models.CharField(verbose_name='CIL', blank=True, null=True, max_length=50)),
                ('eje_oi', models.CharField(verbose_name='EJE', blank=True, null=True, max_length=50)),
                ('add_oi', models.CharField(verbose_name='ADD', blank=True, null=True, max_length=50)),
                ('dp_oi', models.CharField(verbose_name='D.P', blank=True, null=True, max_length=50)),
                ('np_oi', models.CharField(verbose_name='N.P', blank=True, null=True, max_length=50)),
                ('alt_oi', models.CharField(verbose_name='ALT', blank=True, null=True, max_length=50)),
                ('prisma_oi', models.CharField(verbose_name='PRISMA', blank=True, null=True, max_length=50)),
                ('foria', models.CharField(verbose_name='Foria', blank=True, null=True, max_length=100)),
                ('campimetria', models.CharField(verbose_name='Campimetría', blank=True, null=True, max_length=100)),
                ('remitir_oftamologia', models.NullBooleanField(verbose_name='Remitir a oftamología')),
                ('recomendaciones', models.TextField(verbose_name='Recomendaciones', blank=True, null=True)),
                ('tipo', models.CharField(choices=[('VI', 'VISIOMETRIA'), ('OP', 'OPTOMETRIA')], max_length=2)),
                ('estado', models.CharField(choices=[('PE', 'PENDIENTE'), ('RE', 'RESULTADO EMITIDO')], max_length=2)),
                ('orden', models.OneToOneField(to='historias.orden', related_name='visiometria')),
                ('visiometra', models.ForeignKey(to='examenes.Empleado', related_name='visiometrias')),
            ],
        ),
    ]
