# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('historias', '0002_auto_20170329_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historia_clinica',
            name='a_biolog1',
            field=models.CharField(max_length=1, default='6', choices=[('1', 'Virus'), ('2', 'Bacteria'), ('3', 'Hongos'), ('4', 'Parasitos'), ('5', 'Otros'), ('6', 'Ninguno')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='a_biolog2',
            field=models.CharField(max_length=1, default='6', choices=[('1', 'Virus'), ('2', 'Bacteria'), ('3', 'Hongos'), ('4', 'Parasitos'), ('5', 'Otros'), ('6', 'Ninguno')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='a_erg1',
            field=models.CharField(max_length=1, default='4', choices=[('1', 'Posturas'), ('2', 'Reubicación de Puesto'), ('3', 'Otros'), ('4', 'Ninguno')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='a_erg2',
            field=models.CharField(max_length=1, default='4', choices=[('1', 'Posturas'), ('2', 'Reubicación de Puesto'), ('3', 'Otros'), ('4', 'Ninguno')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='a_fis1',
            field=models.CharField(max_length=1, default='B', choices=[('1', 'Quemaduras por Electricidad 1er grado'), ('2', 'Quemaduras por Electricidad  2do grado'), ('3', 'Quemaduras por Electricidad  3er grado'), ('4', 'Altas temperaturas'), ('5', 'Bajas temperaturas'), ('6', 'Iluminación'), ('7', 'Radiaciones'), ('8', 'Vibraciones'), ('9', 'Ruido'), ('A', 'Otros'), ('B', 'Ninguno')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='a_fis2',
            field=models.CharField(max_length=1, default='B', choices=[('1', 'Quemaduras por Electricidad 1er grado'), ('2', 'Quemaduras por Electricidad  2do grado'), ('3', 'Quemaduras por Electricidad  3er grado'), ('4', 'Altas temperaturas'), ('5', 'Bajas temperaturas'), ('6', 'Iluminación'), ('7', 'Radiaciones'), ('8', 'Vibraciones'), ('9', 'Ruido'), ('A', 'Otros'), ('B', 'Ninguno')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='a_mec1',
            field=models.CharField(max_length=1, default='5', choices=[('1', 'Caídas'), ('2', 'Contusiones'), ('3', 'Torceduras'), ('4', 'Otros'), ('5', 'Ninguno')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='a_mec2',
            field=models.CharField(max_length=1, default='5', choices=[('1', 'Caídas'), ('2', 'Contusiones'), ('3', 'Torceduras'), ('4', 'Otros'), ('5', 'Ninguno')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='a_prot1',
            field=models.CharField(max_length=1, default='S', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='a_prot2',
            field=models.CharField(max_length=1, default='S', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='a_psi1',
            field=models.CharField(max_length=1, default='4', choices=[('1', 'Estrés laboral'), ('2', 'Acoso laboral'), ('3', 'Otros'), ('4', 'Ninguno')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='a_psi2',
            field=models.CharField(max_length=1, default='4', choices=[('1', 'Estrés laboral'), ('2', 'Acoso laboral'), ('3', 'Otros'), ('4', 'Ninguno')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='a_qui1',
            field=models.CharField(max_length=1, default='F', choices=[('1', 'Vapores'), ('2', 'Gases'), ('3', 'Quemaduras por corrosivo 1 2 y 3 grado'), ('4', 'Inflamables'), ('5', 'Toxicos'), ('6', 'Irritantes'), ('7', 'Muy toxicos'), ('8', 'Explosivos'), ('9', 'Radiactivos'), ('A', 'Nocivos'), ('B', 'Explosivos'), ('C', 'Polvos'), ('D', 'Solidos'), ('E', 'Otros'), ('F', 'Ninguno')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='a_qui2',
            field=models.CharField(max_length=1, default='F', choices=[('1', 'Vapores'), ('2', 'Gases'), ('3', 'Quemaduras por corrosivo 1 2 y 3 grado'), ('4', 'Inflamables'), ('5', 'Toxicos'), ('6', 'Irritantes'), ('7', 'Muy toxicos'), ('8', 'Explosivos'), ('9', 'Radiactivos'), ('A', 'Nocivos'), ('B', 'Explosivos'), ('C', 'Polvos'), ('D', 'Solidos'), ('E', 'Otros'), ('F', 'Ninguno')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='abdomen',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='accidente',
            field=models.CharField(verbose_name='Accidente de Trabajo', max_length=2, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='accidente_p',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='actividad',
            field=models.CharField(verbose_name='Actividad Realizada', max_length=1, default='P', choices=[('P', 'De Pie'), ('S', 'Sentado'), ('D', 'Deambulado')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='alcohol',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='alcoholismo',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='alergias',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='anexos',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='asma',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='cabeza',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='cancer',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='cicatrices',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='columna_cervical',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='columna_dorsal',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='columna_lumbo',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='concepto',
            field=models.CharField(max_length=1, default='8', choices=[('1', 'Apto'), ('2', 'Apto para trabajar en altura'), ('3', 'Apto para manipulacion de alimentos'), ('4', 'Apto con recomendaciones de seguimiento'), ('5', 'Apto con patologia que no interfieren con el cargo'), ('6', 'Apto con restricciones'), ('7', 'Aplazado'), ('8', 'Concepto NO emitido')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='conjuntivas',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='coordinacion',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='corazon',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='cornetes',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='craneo',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='cuello',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='d_cadera',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='d_cadera_o',
            field=models.TextField(max_length=50, blank=True, null=True, default='Ninguna'),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='d_codo',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='d_codo_o',
            field=models.TextField(max_length=50, blank=True, null=True, default='Ninguna'),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='d_cuello',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='d_cuello_o',
            field=models.TextField(max_length=50, blank=True, null=True, default='Ninguna'),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='d_hombros',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='d_hombros_o',
            field=models.TextField(max_length=50, blank=True, null=True, default='Ninguna'),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='d_muneca',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='d_muneca_o',
            field=models.TextField(max_length=50, blank=True, null=True, default='Ninguna'),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='d_rodilla',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='d_rodilla_o',
            field=models.TextField(max_length=50, blank=True, null=True, default='Ninguna'),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='d_tobillo',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='d_tobillo_o',
            field=models.TextField(max_length=50, blank=True, null=True, default='Ninguna'),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='deportes',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='diabetes',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='diastolicos',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='enf_piel',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='enfermedad_profesional',
            field=models.CharField(verbose_name='Enfermedad Profesional', max_length=2, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='epilepsia',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='escribe',
            field=models.CharField(max_length=1, default='D', choices=[('Z', 'Zurdo'), ('D', 'Diestro'), ('A', 'Ambidiestro')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='estado',
            field=models.CharField(max_length=1, default='B', choices=[('B', 'Bueno'), ('R', 'Regular'), ('M', 'Malo')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='extrasistoles',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='f_accidente_p',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='f_alcoholismo',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='f_alergias',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='f_asma',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='f_audiometria',
            field=models.DateField(verbose_name='Fecha Audiometria', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='f_cancer',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='f_diabetes',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='f_enf_piel',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='f_epilepsia',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='f_espirometria',
            field=models.DateField(verbose_name='Fecha Espirometria', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='f_fracturas',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='f_gripas',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='f_hematologicos',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='f_hipertension',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='f_hospitalizacion',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='f_imagen',
            field=models.DateField(verbose_name='Fecha Imagenologia', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='f_intoxicaciones',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='f_laboratorio',
            field=models.DateField(verbose_name='Fecha Laboratorio', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='f_mentales',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='f_otologicos',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='f_otros',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='f_quirurgicos',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='f_tabaquismo',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='f_tbc',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='f_visiometria',
            field=models.DateField(verbose_name='Fecha Visiometria', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='faringe',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='fibrilacion',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='fondo',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='fracturas',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='fum',
            field=models.DateField(verbose_name='FUM', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='fup',
            field=models.DateField(verbose_name='FUP', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='genitales',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'No Explorado'), ('E', 'Explorado')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='gripas',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='hematologicos',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='hernias',
            field=models.CharField(max_length=1, default='N', choices=[('1', 'Inguinal Derecha'), ('2', 'Inguinal Izquierda'), ('3', 'Umbilical'), ('4', 'Diafragmatica'), ('5', 'Hiatal'), ('N', 'Ninguno')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='hijos',
            field=models.CharField(verbose_name='Hijos', max_length=2, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='hijos_vivos',
            field=models.CharField(verbose_name='Nº Hijos Vivos', max_length=2, blank=True, null=True, default='0'),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='hipertension',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='hospitalizacion',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='intoxicaciones',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='labios',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='m_inferiores',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='m_superiores',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='marcha',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='mentales',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='num_hijos',
            field=models.CharField(verbose_name='Nº Hijos', max_length=2, blank=True, null=True, default='0'),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='o_reflejos',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='o_torax',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='observaciones',
            field=models.TextField(max_length=200, blank=True, null=True, default='Ninguna'),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='ostocopia',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='otologicos',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='otros',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='pabellones',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='pared',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='phannel',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='piel',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='planificacion',
            field=models.CharField(max_length=1, default='9', choices=[('1', 'Preservativo'), ('2', 'Implante Subdermico'), ('3', 'DIU'), ('4', 'Pomeroy'), ('5', 'Inyección'), ('6', 'Píldora'), ('7', 'Ritmo'), ('8', 'Otros'), ('9', 'Ninguno')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='pre_concepto',
            field=models.CharField(max_length=1, default='N', choices=[('A', 'Paciente Aparentemente Sano'), ('O', 'Paciente con Observaciones'), ('N', 'Ninguno')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='presistolicos',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='pulmones',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='pupilas',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='quirurgicos',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='reflejos',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='remitir',
            field=models.CharField(max_length=1, default='N', choices=[('E', 'E.P.S'), ('A', 'A.R.S'), ('N', 'Ninguno')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='ruidos',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='sistolicos',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='soplos',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='tabaquismo',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='tabique',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='tbc',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='tinnel',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='tiroides',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='torax',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='tunel',
            field=models.TextField(max_length=200, blank=True, null=True, default='Ninguno'),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='turno',
            field=models.CharField(verbose_name='Turno', max_length=1, default='D', choices=[('D', 'Diurno'), ('N', 'Nocturno'), ('R', 'Rotatorio')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='varices',
            field=models.CharField(max_length=1, default='N', choices=[('P', 'Primero'), ('S', 'Segundo'), ('T', 'Tercero'), ('N', 'Ninguno')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='vascular',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='vasos',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normales'), ('E', 'Escleroticos')]),
        ),
        migrations.AlterField(
            model_name='historia_clinica',
            name='viseras',
            field=models.CharField(max_length=1, default='N', choices=[('N', 'Normal'), ('A', 'Anormal')]),
        ),
        migrations.AlterField(
            model_name='historia_procedimientos',
            name='ambito',
            field=models.CharField(verbose_name='Ambito de realización del procedimiento', max_length=1, default='1', choices=[('1', 'Ambulatorio'), ('2', 'Hospitalario'), ('3', 'En urgencias')]),
        ),
        migrations.AlterField(
            model_name='historia_procedimientos',
            name='finalidad',
            field=models.CharField(verbose_name='Finalidad del procedimiento', max_length=1, default='1', choices=[('1', 'Diagnostico'), ('2', 'Terapeutico'), ('3', 'Proteccion especifica'), ('4', 'Deteccion temprana de enfermedad general'), ('5', 'Deteccion temprana de enfermedad profesional')]),
        ),
        migrations.AlterField(
            model_name='historia_procedimientos',
            name='forma',
            field=models.CharField(verbose_name='Forma de realizacion del acto quirurgico', max_length=1, default='1', choices=[('1', 'Único o unilateral'), ('2', 'Multiple o Bilateral misma via, diferente especialidad'), ('3', 'Multiple o Bilateral misma via, igual especialidad'), ('4', 'Multiple o Bilateral diferente via, diferente especialidad'), ('5', 'Multiple o Bilateral diferente via, igual especialidad')]),
        ),
        migrations.AlterField(
            model_name='historia_procedimientos',
            name='impresion',
            field=models.TextField(max_length=300, default=''),
        ),
        migrations.AlterField(
            model_name='historia_procedimientos',
            name='personal',
            field=models.CharField(verbose_name='Personal que atiende', max_length=1, default='1', choices=[('1', 'Médico (a) especialista'), ('2', 'Médico (a) general'), ('3', 'Enfermera (o)'), ('4', 'Auxiliar de enfermería'), ('5', 'Otro')]),
        ),
        migrations.AlterField(
            model_name='historia_procedimientos',
            name='remision',
            field=models.TextField(max_length=300, blank=True, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='laboratorios',
            name='fecha',
            field=models.DateField(verbose_name='Fecha Examen', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orden',
            name='empresa_cliente',
            field=models.CharField(verbose_name='Empresa Cliente', max_length=200),
        ),
        migrations.AlterField(
            model_name='orden',
            name='examen',
            field=models.CharField(verbose_name='Examen de', max_length=2, default='5', choices=[('1', 'Ingreso'), ('2', 'Periodico'), ('3', 'Egreso'), ('4', 'Otros'), ('5', 'Ninguno')]),
        ),
        migrations.AlterField(
            model_name='orden',
            name='examen_adicional',
            field=models.CharField(verbose_name='Examen Adicional', max_length=2, default='3', choices=[('1', 'Examen de Altura'), ('2', 'Post Incapacidad'), ('3', 'Ninguno'), ('4', 'Manipulacion de Alimentos')]),
        ),
        migrations.AlterField(
            model_name='orden',
            name='fecha',
            field=models.DateTimeField(verbose_name='Fecha Orden', default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='orden',
            name='fecha_atencion',
            field=models.DateField(verbose_name='Fecha Atencion', default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='orden',
            name='status',
            field=models.CharField(verbose_name='Estado', max_length=1, default='P', choices=[('P', 'Pendiente'), ('R', 'Realizada')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='a_cardiaco',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='a_cerebro_v',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='acrofobia',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='angina_pecho',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='aparato_oir',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='baranay',
            field=models.CharField(max_length=1, default='N', choices=[('A', 'Anormal'), ('N', 'Normal')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='claustrofobia',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='convulsiones',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='convulsiones_p',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='daltonismo',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='dano_oidos',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='debilidad_brazos',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='diabetes',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='dif_agacharse',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='dif_agacharse_piso',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='dif_cabeza_arriba',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='dif_cabeza_lado',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='dif_escalera',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='dificultad_extremidades',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='dificultad_oir',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='dolor_espalda',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='dolor_pecho1',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='dolor_pecho2',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='dolor_pecho3',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='dolor_pecho_indigestion',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='dolor_rigidez',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='enf_mental',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='enfermedad_mental',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='epilepsia',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='hallpike',
            field=models.CharField(max_length=1, default='N', choices=[('A', 'Anormal'), ('N', 'Normal')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='hinchazon_pies',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='insuficiencia_cardiaca',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='late_irregularmente',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='latidos',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='lentes',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='lentes_contacto',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='lesion_espalda',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='otro',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='otros_sintomas',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='perdida_vista',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='presion',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='presion_alta',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='prob_audicion',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='prob_circulacion',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='prob_pulmonares',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='problema_ojos',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='reacciones',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='romberg',
            field=models.CharField(max_length=1, default='N', choices=[('A', 'Anormal'), ('N', 'Normal')]),
        ),
        migrations.AlterField(
            model_name='test_altura',
            name='vertigos',
            field=models.CharField(max_length=1, default='N', choices=[('S', 'Si'), ('N', 'No')]),
        ),
    ]
