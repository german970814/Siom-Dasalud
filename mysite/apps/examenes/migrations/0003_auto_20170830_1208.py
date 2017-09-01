# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examenes', '0002_audiometria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiometria',
            name='audiometra',
            field=models.ForeignKey(verbose_name='Audiometra', related_name='audiometrias', to='examenes.Empleado'),
        ),
        migrations.AlterField(
            model_name='audiometria',
            name='hz1000_d',
            field=models.IntegerField(verbose_name='1000hz', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='audiometria',
            name='hz1000_i',
            field=models.IntegerField(verbose_name='1000hz', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='audiometria',
            name='hz2000_d',
            field=models.IntegerField(verbose_name='2000hz', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='audiometria',
            name='hz2000_i',
            field=models.IntegerField(verbose_name='2000hz', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='audiometria',
            name='hz250_d',
            field=models.IntegerField(verbose_name='250hz', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='audiometria',
            name='hz250_i',
            field=models.IntegerField(verbose_name='250hz', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='audiometria',
            name='hz3000_d',
            field=models.IntegerField(verbose_name='3000hz', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='audiometria',
            name='hz3000_i',
            field=models.IntegerField(verbose_name='3000hz', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='audiometria',
            name='hz4000_d',
            field=models.IntegerField(verbose_name='4000hz', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='audiometria',
            name='hz4000_i',
            field=models.IntegerField(verbose_name='4000hz', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='audiometria',
            name='hz500_d',
            field=models.IntegerField(verbose_name='500hz', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='audiometria',
            name='hz500_i',
            field=models.IntegerField(verbose_name='500hz', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='audiometria',
            name='hz6000_d',
            field=models.IntegerField(verbose_name='6000hz', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='audiometria',
            name='hz6000_i',
            field=models.IntegerField(verbose_name='6000hz', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='audiometria',
            name='hz8000_d',
            field=models.IntegerField(verbose_name='8000hz', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='audiometria',
            name='hz8000_i',
            field=models.IntegerField(verbose_name='8000hz', blank=True, null=True),
        ),
    ]
