# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('historias', '0003_auto_20170801_1706'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Visiometra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(verbose_name='Nombre', max_length=200)),
                ('usuario', models.OneToOneField(verbose_name='Usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Visiometria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('lentes_correctivos', models.NullBooleanField(verbose_name='Usa Lentes Correctivos')),
                ('hace_cuanto', models.CharField(verbose_name='Hace cuanto tiempo', max_length=100, blank=True, null=True)),
                ('cirugia', models.NullBooleanField(verbose_name='Cirugía')),
                ('trauma_ocular', models.NullBooleanField(verbose_name='Trauma Ocular')),
                ('pterigio', models.NullBooleanField(verbose_name='Pterigio')),
                ('colores', models.NullBooleanField(verbose_name='Colores')),
                ('vision_lejana', models.CharField(verbose_name='Vision lejana', max_length=2, choices=[('OD', 'OJO DERECHO'), ('OI', 'OJO IZQUIERDO'), ('AO', 'AMBOS OJOS')])),
                ('vision_cercana', models.CharField(verbose_name='Vision cercana', max_length=2, choices=[('OD', 'OJO DERECHO'), ('OI', 'OJO IZQUIERDO'), ('AO', 'AMBOS OJOS')])),
                ('av', models.CharField(verbose_name='AV', max_length=2, choices=[('OD', 'OJO DERECHO'), ('OI', 'OJO IZQUIERDO'), ('AO', 'AMBOS OJOS')])),
                ('esf_od', models.CharField(verbose_name='ESF', max_length=50)),
                ('cil_od', models.CharField(verbose_name='CIL', max_length=50)),
                ('eje_od', models.CharField(verbose_name='EJE', max_length=50)),
                ('add_od', models.CharField(verbose_name='ADD', max_length=50)),
                ('dp_od', models.CharField(verbose_name='D.P', max_length=50)),
                ('np_od', models.CharField(verbose_name='N.P', max_length=50)),
                ('alt_od', models.CharField(verbose_name='ALT', max_length=50)),
                ('prisma_od', models.CharField(verbose_name='PRISMA', max_length=50)),
                ('esf_oi', models.CharField(verbose_name='ESF', max_length=50)),
                ('cil_oi', models.CharField(verbose_name='CIL', max_length=50)),
                ('eje_oi', models.CharField(verbose_name='EJE', max_length=50)),
                ('add_oi', models.CharField(verbose_name='ADD', max_length=50)),
                ('dp_oi', models.CharField(verbose_name='D.P', max_length=50)),
                ('np_oi', models.CharField(verbose_name='N.P', max_length=50)),
                ('alt_oi', models.CharField(verbose_name='ALT', max_length=50)),
                ('prisma_oi', models.CharField(verbose_name='PRISMA', max_length=50)),
                ('foria', models.CharField(verbose_name='Foria', max_length=100)),
                ('campimetria', models.CharField(verbose_name='Campimetría', max_length=100)),
                ('remitir_oftamologia', models.NullBooleanField(verbose_name='Remitir a oftamología')),
                ('recomendaciones', models.TextField(verbose_name='Recomendaciones')),
                ('estado', models.CharField(max_length=2, choices=[('PE', 'PENDIENTE'), ('RE', 'RESULTADO EMITIDO')])),
                ('orden', models.OneToOneField(related_name='visiometria', to='historias.orden')),
                ('visiometra', models.ForeignKey(related_name='visiometrias', to='examenes.Visiometra')),
            ],
        ),
    ]
