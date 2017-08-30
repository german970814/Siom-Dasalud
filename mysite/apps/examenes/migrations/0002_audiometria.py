# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historias', '0003_auto_20170801_1706'),
        ('examenes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audiometria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('tiempo_exposicion', models.CharField(verbose_name='Tiempo de exposición', max_length=50, blank=True)),
                ('frecuencia', models.CharField(verbose_name='Frecuencia', max_length=50, blank=True)),
                ('proteccion_auditiva', models.NullBooleanField(verbose_name='Protección auditiva')),
                ('tipo_proteccion', models.CharField(verbose_name='Tipo de protección', max_length=200, blank=True)),
                ('servicio_militar', models.NullBooleanField(verbose_name='Prestó servicio militar')),
                ('practica_poligono', models.NullBooleanField(verbose_name='Practicaba o practica poligono')),
                ('usa_motocicleta', models.NullBooleanField(verbose_name='Utiliza motocicleta')),
                ('cerca_explociones', models.NullBooleanField(verbose_name='Ha estado cerca de explociones')),
                ('musica_volumen', models.NullBooleanField(verbose_name='Escucha música alto volumén')),
                ('usa_audifonos', models.NullBooleanField(verbose_name='Usa audifonos/walman')),
                ('practica_tejo', models.NullBooleanField(verbose_name='Practica tejo, caza, entre otros')),
                ('otros_antecedentes', models.CharField(verbose_name='otros', max_length=200, blank=True)),
                ('cirugia_oido', models.NullBooleanField(verbose_name='Cirugía de oido')),
                ('trauma', models.NullBooleanField(verbose_name='Trauma')),
                ('medicamentos_ototoxicos', models.NullBooleanField(verbose_name='Medicamentos ototóxicos')),
                ('hipoacusia', models.NullBooleanField(verbose_name='Hipoacusia')),
                ('vertigo', models.NullBooleanField(verbose_name='Vértigo')),
                ('acufeno', models.NullBooleanField(verbose_name='Acufeno')),
                ('otitis', models.NullBooleanField(verbose_name='Otitis')),
                ('otorrea', models.NullBooleanField(verbose_name='Otorrea')),
                ('hz250_d', models.IntegerField(verbose_name='250hz')),
                ('hz500_d', models.IntegerField(verbose_name='500hz')),
                ('hz1000_d', models.IntegerField(verbose_name='1000hz')),
                ('hz2000_d', models.IntegerField(verbose_name='2000hz')),
                ('hz3000_d', models.IntegerField(verbose_name='3000hz')),
                ('hz4000_d', models.IntegerField(verbose_name='4000hz')),
                ('hz6000_d', models.IntegerField(verbose_name='6000hz')),
                ('hz8000_d', models.IntegerField(verbose_name='8000hz')),
                ('hz250_i', models.IntegerField(verbose_name='250hz')),
                ('hz500_i', models.IntegerField(verbose_name='500hz')),
                ('hz1000_i', models.IntegerField(verbose_name='1000hz')),
                ('hz2000_i', models.IntegerField(verbose_name='2000hz')),
                ('hz3000_i', models.IntegerField(verbose_name='3000hz')),
                ('hz4000_i', models.IntegerField(verbose_name='4000hz')),
                ('hz6000_i', models.IntegerField(verbose_name='6000hz')),
                ('hz8000_i', models.IntegerField(verbose_name='8000hz')),
                ('otoscopia_od', models.CharField(verbose_name='Ototoscopia od', max_length=200, blank=True)),
                ('otoscopia_oi', models.CharField(verbose_name='Ototoscopia oi', max_length=200, blank=True)),
                ('uso_protectores_auditivos', models.NullBooleanField(verbose_name='Otorrea')),
                ('complementar_audiometria_clinica', models.NullBooleanField(verbose_name='Otorrea')),
                ('control_periodico', models.NullBooleanField(verbose_name='Otorrea')),
                ('otras', models.TextField(verbose_name='Otras', blank=True)),
                ('estado', models.CharField(max_length=2, choices=[('PE', 'PENDIENTE'), ('RE', 'RESULTADO EMITIDO')])),
                ('audiometra', models.ForeignKey(related_name='audiometrias', to='examenes.Empleado')),
                ('orden', models.OneToOneField(related_name='audiometria', to='historias.orden')),
            ],
        ),
    ]
