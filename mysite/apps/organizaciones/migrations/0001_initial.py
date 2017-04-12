# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import mysite.apps.organizaciones.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='afp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('documento', models.CharField(default=b'NI', max_length=2, verbose_name='Documento', choices=[(b'NI', b'Nro de Id Tributaria'), (b'CC', b'C\xc3\xa9dula de Ciudadan\xc3\xada'), (b'CE', b'C\xc3\xa9dula de Extranjer\xc3\xada'), (b'PA', b'Pasaporte')])),
                ('numero', models.CharField(max_length=30, null=True, blank=True)),
                ('razon', models.CharField(max_length=80)),
                ('codigo', models.CharField(default=b'0', max_length=12)),
                ('direccion', models.CharField(max_length=50, null=True, blank=True)),
                ('telefono', models.CharField(max_length=20, null=True, blank=True)),
                ('fax', models.CharField(max_length=20, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='arp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('documento', models.CharField(default=b'NI', max_length=2, verbose_name='Documento', choices=[(b'NI', b'Nro de Id Tributaria'), (b'CC', b'C\xc3\xa9dula de Ciudadan\xc3\xada'), (b'CE', b'C\xc3\xa9dula de Extranjer\xc3\xada'), (b'PA', b'Pasaporte')])),
                ('numero', models.CharField(max_length=30, null=True, blank=True)),
                ('razon', models.CharField(max_length=80)),
                ('codigo', models.CharField(default=b'0', max_length=12)),
                ('direccion', models.CharField(max_length=50, null=True, blank=True)),
                ('telefono', models.CharField(max_length=20, null=True, blank=True)),
                ('fax', models.CharField(max_length=20, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='empresas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nit', models.CharField(max_length=30)),
                ('razon', models.CharField(max_length=50)),
                ('codigo', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
                ('fax', models.CharField(max_length=20, null=True, blank=True)),
                ('representante', models.CharField(max_length=50)),
                ('contrato', models.CharField(max_length=8, null=True, blank=True)),
                ('poliza', models.CharField(max_length=8, null=True, blank=True)),
                ('dias', models.IntegerField(null=True, verbose_name=b'D\xc3\xadas Vence Factura', blank=True)),
                ('tipo_tarifa', models.CharField(default=b'1', max_length=1, verbose_name='Tipo de Tarifa', choices=[(b'1', b'ISS 2001'), (b'2', b'ISS 2004')])),
                ('plan_beneficios', models.CharField(max_length=20, null=True, blank=True)),
                ('drogas', models.BooleanField(default=False)),
                ('suministros', models.BooleanField(default=False)),
                ('eps', models.BooleanField(default=False)),
                ('retiene_copago', models.BooleanField(default=False)),
                ('regimen', models.CharField(default=b'C', max_length=1, verbose_name='Estado', choices=[(b'C', b'Comun'), (b'S', b'Simplificado'), (b'N', b'No Aplica')])),
                ('autoretenedor', models.BooleanField(default=False)),
                ('valor_sedacion', models.PositiveIntegerField(default=0, null=True, verbose_name=b'Costo Base de Sedacion', blank=True)),
                ('ciudad', models.ForeignKey(related_name='ciudad_empresas', verbose_name='Ciudad', to='home.departamentos')),
            ],
        ),
        migrations.CreateModel(
            name='eps',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('documento', models.CharField(default=b'NI', max_length=2, verbose_name='Documento', choices=[(b'NI', b'Nro de Id Tributaria'), (b'CC', b'C\xc3\xa9dula de Ciudadan\xc3\xada'), (b'CE', b'C\xc3\xa9dula de Extranjer\xc3\xada'), (b'PA', b'Pasaporte')])),
                ('numero', models.CharField(max_length=30, null=True, blank=True)),
                ('razon', models.CharField(max_length=80)),
                ('codigo', models.CharField(default=b'0', max_length=12)),
                ('direccion', models.CharField(max_length=50, null=True, blank=True)),
                ('telefono', models.CharField(max_length=20, null=True, blank=True)),
                ('fax', models.CharField(max_length=20, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='instituciones',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('documento', models.CharField(max_length=2, verbose_name='Documento', choices=[(b'NI', b'Nro de Id Tributaria'), (b'CC', b'C\xc3\xa9dula de Ciudadan\xc3\xada'), (b'CE', b'C\xc3\xa9dula de Extranjer\xc3\xada'), (b'PA', b'Pasaporte')])),
                ('numero', models.CharField(max_length=30)),
                ('razon', models.CharField(max_length=50)),
                ('codigo', models.CharField(default=b'0', max_length=12)),
                ('direccion', models.CharField(max_length=50, null=True, blank=True)),
                ('telefono', models.CharField(max_length=20, null=True, blank=True)),
                ('fax', models.CharField(max_length=20, null=True, blank=True)),
                ('letra_factura', models.CharField(max_length=3, null=True, blank=True)),
                ('imagen', models.ImageField(null=True, upload_to=mysite.apps.organizaciones.models.url, blank=True)),
                ('logo_historia', models.ImageField(null=True, upload_to=mysite.apps.organizaciones.models.url, blank=True)),
                ('altura', models.ImageField(null=True, upload_to=mysite.apps.organizaciones.models.url, blank=True)),
                ('alimentos', models.ImageField(null=True, upload_to=mysite.apps.organizaciones.models.url, blank=True)),
                ('espacios', models.ImageField(null=True, upload_to=mysite.apps.organizaciones.models.url, blank=True)),
                ('apto', models.ImageField(null=True, upload_to=mysite.apps.organizaciones.models.url, blank=True)),
                ('ciudad', models.ForeignKey(related_name='instituciones_departamento', verbose_name='Ciudad', to='home.departamentos')),
                ('empresas', models.ManyToManyField(to='organizaciones.empresas', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='planes_salud',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=50)),
                ('porcentaje', models.DecimalField(max_digits=3, decimal_places=3)),
            ],
        ),
        migrations.CreateModel(
            name='tipo_empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=50)),
                ('cuenta_contable', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='usuario_empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('empresa', models.ForeignKey(related_name='usuario_empresa_empresas', verbose_name=b'Empresa', to='organizaciones.empresas')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='empresas',
            name='plan',
            field=models.ForeignKey(related_name='empresas_plan', verbose_name='Plan', to='organizaciones.planes_salud'),
        ),
        migrations.AddField(
            model_name='empresas',
            name='tipo',
            field=models.ForeignKey(related_name='tipo_empresas', verbose_name='Tipo Empresa', to='organizaciones.tipo_empresa'),
        ),
    ]
