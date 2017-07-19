# -*- coding: utf-8 -*-
from django.db import models
from mysite.apps.home.models import departamentos
from django.contrib.auth.models import User

class tipo_empresa(models.Model):
	descripcion		=	models.CharField(max_length=50)
	cuenta_contable		=	models.CharField(max_length=10)

	def __unicode__(self):
		return self.descripcion

class planes_salud(models.Model):
	descripcion		=	models.CharField(max_length=50)
	porcentaje = models.DecimalField(max_digits=3,decimal_places=3)

	def __unicode__(self):
		return self.descripcion

class empresas(models.Model):
	opciones = (
		('C', 'Comun'),
 		('S', 'Simplificado'),
 		('N', 'No Aplica'),
    )

	opciones2 = (
		('1', 'ISS 2001'),
		('2', 'ISS 2004'),
    )

	nit   = models.CharField(max_length=30)
	razon   = models.CharField(max_length=50)
	codigo   = models.CharField(max_length=10)
	direccion   = models.CharField(max_length=50)
	telefono     = models.CharField(max_length=20)
	fax    = models.CharField(max_length=20, null=True, blank=True)
	ciudad	= models.ForeignKey(departamentos,related_name='ciudad_empresas',verbose_name=u'Ciudad')
	representante   = models.CharField(max_length=50)
	tipo  =  models.ForeignKey(tipo_empresa,related_name='tipo_empresas',verbose_name=u'Tipo Empresa')
	contrato  = models.CharField(max_length=8,null=True, blank=True)
	poliza  = models.CharField(max_length=8,null=True, blank=True)
	dias = models.IntegerField(verbose_name='Días Vence Factura',null=True, blank=True)
	tipo_tarifa = models.CharField(max_length=1, choices=opciones2,default='1', verbose_name=u'Tipo de Tarifa')
	plan_beneficios	= models.CharField(max_length=20, null=True, blank=True)
	drogas = models.BooleanField(default=False)
	suministros = models.BooleanField(default=False)
	eps = models.BooleanField(default=False)
	retiene_copago = models.BooleanField(default=False)
	regimen = models.CharField(max_length=1, choices=opciones,default='C', verbose_name=u'Estado')
	autoretenedor = models.BooleanField(default=False)
	plan =  models.ForeignKey(planes_salud,related_name='empresas_plan',verbose_name=u'Plan')
	valor_sedacion = models.PositiveIntegerField(verbose_name='Costo Base de Sedacion',default=0,null=True, blank=True)

	def __unicode__(self):
		return "%s   %s"%(self.razon,self.nit)
	__str__ = lambda self: self.__unicode__()


class usuario_empresa(models.Model):

	empresa     = models.ForeignKey(empresas,related_name='usuario_empresa_empresas',verbose_name="Empresa")
	nombre		= models.CharField(max_length=30)
	usuario		= models.ForeignKey(User) #

	def __unicode__(self):
		nombreCompleto = "Empresa: %s - %s"%(self.empresa,self.usuario)
		return nombreCompleto


def url(self, filename):
	ruta = "MultimediaData/Instituciones/%s" % str(filename)
	return ruta


class instituciones(models.Model):
	opciones = (
		('NI', 'Nro de Id Tributaria'),
 		('CC', 'Cédula de Ciudadanía'),
 		('CE', 'Cédula de Extranjería'),
 		('PA', 'Pasaporte'),
    )

	documento   = models.CharField(max_length=2, choices=opciones, verbose_name=u'Documento')
	numero  = models.CharField(max_length=30)
	razon   = models.CharField(max_length=50)
	codigo   = models.CharField(max_length=12,default = '0')
	direccion   = models.CharField(max_length=50,null=True, blank=True)
	telefono     = models.CharField(max_length=20, null=True, blank=True)
	fax    = models.CharField(max_length=20, null=True, blank=True)
	empresas = models.ManyToManyField(empresas,null=True,blank=True)
	letra_factura	= models.CharField(max_length=3, null=True, blank=True)
	imagen 		= models.ImageField(upload_to=url,null=True,blank=True)
	logo_historia 		= models.ImageField(upload_to=url,null=True,blank=True)
	altura 		= models.ImageField(upload_to=url,null=True,blank=True)
	alimentos 		= models.ImageField(upload_to=url,null=True,blank=True)
	espacios 		= models.ImageField(upload_to=url,null=True,blank=True)
	apto 		= models.ImageField(upload_to=url,null=True,blank=True)
	#Octubre 5 de 2015
	ciudad = models.ForeignKey(departamentos,related_name='instituciones_departamento',verbose_name=u'Ciudad')

	def __unicode__(self):
		return "%s   %s"%(self.razon,self.numero)

class eps(models.Model):
	opciones = (
		('NI', 'Nro de Id Tributaria'),
 		('CC', 'Cédula de Ciudadanía'),
 		('CE', 'Cédula de Extranjería'),
 		('PA', 'Pasaporte'),
    )

	documento   = models.CharField(max_length=2, choices=opciones, default='NI' ,verbose_name=u'Documento')
	numero  = models.CharField(max_length=30 ,null=True, blank=True)
	razon   = models.CharField(max_length=80)
	codigo   = models.CharField(max_length=12,default = '0')
	direccion   = models.CharField(max_length=50,null=True, blank=True)
	telefono     = models.CharField(max_length=20, null=True, blank=True)
	fax    = models.CharField(max_length=20, null=True, blank=True)

	def __unicode__(self):
		return "%s" % self.razon

class arp(models.Model):
	opciones = (
		('NI', 'Nro de Id Tributaria'),
 		('CC', 'Cédula de Ciudadanía'),
 		('CE', 'Cédula de Extranjería'),
 		('PA', 'Pasaporte'),
    )

	documento   = models.CharField(max_length=2, choices=opciones, default='NI' ,verbose_name=u'Documento')
	numero  = models.CharField(max_length=30 ,null=True, blank=True)
	razon   = models.CharField(max_length=80)
	codigo   = models.CharField(max_length=12,default = '0')
	direccion   = models.CharField(max_length=50,null=True, blank=True)
	telefono     = models.CharField(max_length=20, null=True, blank=True)
	fax    = models.CharField(max_length=20, null=True, blank=True)

	def __unicode__(self):
		return "%s" % self.razon

class afp(models.Model):
	opciones = (
		('NI', 'Nro de Id Tributaria'),
 		('CC', 'Cédula de Ciudadanía'),
 		('CE', 'Cédula de Extranjería'),
 		('PA', 'Pasaporte'),
    )

	documento   = models.CharField(max_length=2, choices=opciones, default='NI' ,verbose_name=u'Documento')
	numero  = models.CharField(max_length=30 ,null=True, blank=True)
	razon   = models.CharField(max_length=80)
	codigo   = models.CharField(max_length=12,default = '0')
	direccion   = models.CharField(max_length=50,null=True, blank=True)
	telefono     = models.CharField(max_length=20, null=True, blank=True)
	fax    = models.CharField(max_length=20, null=True, blank=True)

	def __unicode__(self):
		return "%s" % self.razon
