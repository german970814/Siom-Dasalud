# -*- coding: utf-8 -*- 
from django.db import models
from mysite.apps.historias.models import orden
from mysite.apps.organizaciones.models import empresas,instituciones
import datetime
from django.db.models import Max

class factura(models.Model):
	#def number():
		#Se debe crear el primer registro para empezar a facturar
		#no = factura.objects.all().aggregate(Max('numero'))
		#if no["numero__max"] == None:
		#	return 1
		#else:
		#	return no["numero__max"]+ 1

	#'numero = models.PositiveIntegerField(unique=True, default=number)
	numero = models.PositiveIntegerField()		
	letra_factura	= models.CharField(max_length=3, null=True, blank=True)
	orden			= models.OneToOneField(orden,related_name='factura_orden')
	fecha_emision	= models.DateField(verbose_name="Fecha Emision",default=datetime.date.today)
	fecha_vencimiento = models.DateField(verbose_name="Fecha Vencimiento",default=datetime.date.today)
	fecha_atencion	= models.DateField(verbose_name="Fecha Atención",default=datetime.date.today)
	valor_consulta = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Valor Consulta',default=0)
	valor_honorarios = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Honorarios Medico',default=0)
	valor_sala		= models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Derechos de Sala',default=0)
	valor_sutura	= models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Materiales de Sutura',default=0)
	valor_anestesia = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Anestesia y Sedacion',default=0)
	
	def __unicode__(self):
		nombreCompleto = "%s %s"%(self.orden.empresa,self.id)
		return nombreCompleto


class categorias(models.Model):
	nombre		= models.CharField(max_length=50)
	descripcion	= models.CharField(max_length=100)	
	
	def __unicode__(self):
		nombreCompleto = "%s"%(self.nombre)
		return nombreCompleto

class producto(models.Model):
	nombre		= models.CharField(max_length=50)
	precio		= models.PositiveIntegerField(verbose_name='Precio',default=0)
	stock		= models.PositiveIntegerField(verbose_name='Cantidad',default=0)
	categorias	= models.ManyToManyField(categorias,null=True,blank=True)	

	def __unicode__(self):
		nombreCompleto = "%s"%(self.nombre)
		return nombreCompleto

class detalle(models.Model):
	factura		= models.ForeignKey(factura,related_name='detalle_factura')
	producto	= models.ForeignKey(producto,related_name='detalle_producto')
	cantidad 	= models.PositiveIntegerField(verbose_name='Cantidad',default=0)
	precio		= models.PositiveIntegerField(verbose_name='Precio',default=0)
	
	def __unicode__(self):
		nombreCompleto = "%s %s"%(self.factura.id,self.producto)
		return nombreCompleto