from django.db import models
from mysite.apps.organizaciones.models import empresas

class servicios(models.Model):
	opciones = (
		('S', 'Servicio'),
		('L', 'Laboratorio'),
    )

	nombre = models.CharField(max_length=100)
	tipo   = models.CharField(max_length=1, choices=opciones, default='S', verbose_name='Tipo')
	costo = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Valor Unitario')
	historia = models.BooleanField(default=False)
	
	def __unicode__(self):
		return self.nombre	

class serviciosEmpresa(models.Model):
	nombre = models.ForeignKey(servicios,related_name='serviciosEmpresa_servicios',verbose_name=u'Servicio')
	empresa = models.ForeignKey(empresas,related_name='serviciosEmpresa_empresa',verbose_name=u'Empresa')
	costo = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Valor Unitario')

	def __unicode__(self):
		return self.nombre.nombre

class items(models.Model):
	nombre = models.CharField(max_length=30)
	descripcion	=	models.TextField(max_length=300)
	
	def __unicode__(self):
		return self.nombre	

class procedimientos(models.Model):
	codigo = models.CharField(max_length=7)
	descripcion	=	models.CharField(max_length=350)
	cups = models.CharField(max_length=7,null=True,blank=True)
	cuenta_contable	=	models.CharField(max_length=10,null=True,blank=True)
	equipo	=	models.CharField(max_length=30,null=True,blank=True)
	tarifa = models.PositiveIntegerField(verbose_name='Tarifa',default=0)
	items	= models.ManyToManyField(items,null=True,blank=True)
	uvr = models.PositiveIntegerField(verbose_name='UVR',default=0)
	
	def __unicode__(self):
		return "%s   %s"%(self.codigo,self.descripcion)			

class consultas(models.Model):
	codigo	=	models.CharField(max_length=7)
	descripcion	= models.CharField(max_length=200)
	cuenta_contable	=	models.CharField(max_length=10,null=True,blank=True)
	tarifa = models.PositiveIntegerField(verbose_name='Tarifa',default=0)	

	def __unicode__(self):
		return self.descripcion

class rango_consulta(models.Model):
	descripcion	= models.CharField(max_length=50)
	cuota = models.PositiveIntegerField(verbose_name='Cuota Moderadora',default=0)	

	def __unicode__(self):
		return self.descripcion

class rango_procedimiento(models.Model):
	descripcion	= models.CharField(max_length=50)
	porcentaje = models.DecimalField(max_digits=3,decimal_places=3)

	def __unicode__(self):
		return self.descripcion

class cie(models.Model):
	codigo 		= models.CharField(max_length=4)
	descripcion	= models.CharField(max_length=350)

	def __unicode__(self):
		return "%s   %s"%(self.codigo,self.descripcion)			

class sutura(models.Model):
	ref			= models.CharField(max_length=10)
	codigo 		= models.CharField(max_length=10)
	descripcion	= models.CharField(max_length=350)
	valor		= models.PositiveIntegerField(default=0)

	def __unicode__(self):
		return "%s   %s"%(self.codigo,self.descripcion)

class honorarios(models.Model):
	ref			= models.CharField(max_length=10)
	codigo 		= models.CharField(max_length=10)
	descripcion	= models.CharField(max_length=350)
	valor		= models.PositiveIntegerField(default=0)

	def __unicode__(self):
		return "%s   %s"%(self.codigo,self.descripcion)

class sala(models.Model):
	codigo 		= models.CharField(max_length=10)
	lim_1		= models.PositiveIntegerField(default=0)
	lim_2		= models.PositiveIntegerField(default=0)
	valor		= models.PositiveIntegerField(default=0)

	def __unicode__(self):
		return "%s De %s Hasta %s UVR"%(self.codigo,self.lim_1,self.lim_2)							