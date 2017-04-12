# -*- coding: utf-8 -*- 
from django.db import models
from mysite.apps.parametros.models import procedimientos,consultas
from mysite.apps.datos.models import paciente,medico
from mysite.apps.organizaciones.models import empresas,instituciones
from django.contrib.auth.models import User	


class agenda_consulta(models.Model):
	title = models.CharField(max_length=100, null=True, blank=True)
	start = models.DateTimeField()
	end   = models.DateTimeField()
	medico = models.ForeignKey(medico,related_name='agenda_consulta_medico')
	editable = models.BooleanField(default=False)	
	overlap = models.BooleanField(default= False)
	color = models.CharField(max_length=10, null=True, blank=True)

	def __unicode__(self):
		return self.title

class agenda_procedimiento(models.Model):
	title = models.CharField(max_length=100, null=True, blank=True)
	start = models.DateTimeField()
	end   = models.DateTimeField()
	medico = models.ForeignKey(medico,related_name='agenda_procedimiento_medico')
	editable = models.BooleanField(default=False)	
	overlap = models.BooleanField(default=False)
	color = models.CharField(max_length=10, null=True, blank=True)

	def __unicode__(self):
		return self.title

class citas_consulta(models.Model):
	opciones = (
		('CC', 'Cédula Ciudadanía'),
		('CE', 'Cédula de Extranjería'),
		('PA', 'Pasaporte'),
		('RC', 'Registro Civil'),
 		('TI', 'Tarjeta de Identidad'),
 		('AS', 'Adulto sin Identificar'),
 		('MS', 'Menor sin Identificar'),
 		('UN', 'Numero Unico de Identificación'),
    )

	agenda = models.OneToOneField(agenda_consulta,related_name='citas_consulta_agenda')
	pnombre		= models.CharField(max_length=30,verbose_name=u'Primer Nombre')
	snombre		= models.CharField(max_length=30,verbose_name=u'Segundo Nombre',null=True,blank=True)
	papellido	= models.CharField(max_length=30,verbose_name=u'Primer Apellido')
	sapellido	= models.CharField(max_length=30,verbose_name=u'Segundo Apellido', null=True, blank=True)
	documento   = models.CharField(max_length=2, choices=opciones, verbose_name=u'Documento')
	cedula      = models.CharField(max_length=20)
	telefono    = models.CharField(max_length=20, null=True, blank=True)
	celular     = models.CharField(max_length=20, null=True, blank=True)
	consulta    = models.ForeignKey(consultas,related_name='citas_consulta_consultas')
	empresa 	= models.ForeignKey(empresas,related_name='citas_consulta_empresa',verbose_name=u'Empresa a la que Pertenece')
	llego		= models.BooleanField(verbose_name=u'Paciente Llego',default=False)
	confirmo	= models.BooleanField(verbose_name=u'Confirmo',default=False)
	cumplida	= models.BooleanField(verbose_name=u'Cumplida',default=False)
	anestesiologo = models.BooleanField(verbose_name=u'Anestesiologo',default=False)
	generadapor = models.ForeignKey(User,null=True, blank=True)
	observacion	= models.TextField(max_length=250,null=True, blank=True)
	hora_llegada = models.TimeField(null=True, blank=True)
	paciente	= models.ForeignKey(paciente,related_name='citas_consulta_paciente',null=True, blank=True)

	def __unicode__(self):
		return "%s  %s"%(self.pnombre,self.papellido)

class citas_procedimiento(models.Model):
	opciones = (
		('CC', 'Cédula Ciudadanía'),
		('CE', 'Cédula de Extranjería'),
		('PA', 'Pasaporte'),
		('RC', 'Registro Civil'),
 		('TI', 'Tarjeta de Identidad'),
 		('AS', 'Adulto sin Identificar'),
 		('MS', 'Menor sin Identificar'),
 		('UN', 'Numero Unico de Identificación'),
    )

	agenda = models.OneToOneField(agenda_procedimiento,related_name='citas_procedimiento_agenda')
	pnombre		= models.CharField(max_length=30,verbose_name=u'Primer Nombre')
	snombre		= models.CharField(max_length=30,verbose_name=u'Segundo Nombre')
	papellido	= models.CharField(max_length=30,verbose_name=u'Primer Apellido')
	sapellido	= models.CharField(max_length=30,verbose_name=u'Segundo Apellido', null=True, blank=True)
	documento   = models.CharField(max_length=2, choices=opciones, verbose_name=u'Documento')
	cedula      = models.CharField(max_length=20)
	telefono    = models.CharField(max_length=20, null=True, blank=True)
	celular     = models.CharField(max_length=20, null=True, blank=True)
	procedimiento    = models.ForeignKey(procedimientos,related_name='citas_procedimiento_procedimientos')
	empresa 	= models.ForeignKey(empresas,related_name='citas_procedimiento_empresa',verbose_name=u'Empresa a la que Pertenece')
	llego		= models.BooleanField(verbose_name=u'Paciente Llego',default=False)
	confirmo	= models.BooleanField(verbose_name=u'Confirmo',default=False)
	cumplida	= models.BooleanField(verbose_name=u'Cumplida',default=False)
	anestesiologo = models.BooleanField(verbose_name=u'Anestesiologo',default=False)
	generadapor = models.ForeignKey(User,null=True, blank=True)
	observacion	= models.TextField(max_length=250,null=True, blank=True)
	hora_llegada = models.TimeField(null=True, blank=True)
	paciente	= models.ForeignKey(paciente,related_name='citas_procedimiento_paciente',null=True, blank=True)

	def __unicode__(self):
		return "%s  %s"%(self.pnombre,self.papellido)
