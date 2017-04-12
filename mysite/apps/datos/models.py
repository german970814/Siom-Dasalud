# -*- coding: utf-8 -*- 
from django.db import models
from django.contrib.auth.models import User
from mysite.apps.home.models import departamentos
from mysite.apps.organizaciones.models import empresas, instituciones
import datetime


class especialidades(models.Model):
	codigo = models.CharField(max_length=3)
	nombre = models.CharField(max_length=150)

	def __unicode__(self):
		return self.nombre	


def url(self,filename):
	ruta = "MultimediaData/Medicos/%s/%s"%(self.nombre,str(filename))
	return ruta

class medico(models.Model):
	opciones = (
		('A', 'Activo'),
 		('I', 'Inactivo'),
    )	
	nombre		= models.CharField(max_length=30,verbose_name=u'Nombres Medico')
	papellido	= models.CharField(max_length=30,verbose_name=u'Primer Apellido')
	sapellido	= models.CharField(max_length=30,verbose_name=u'Segundo Apellido')
	cedula      = models.CharField(max_length=15,unique=True,verbose_name=u'Cedula')
	estado      = models.CharField(max_length=1, choices=opciones,default='A', verbose_name=u'Estado')
	especialidad = models.ForeignKey(especialidades,verbose_name=u'Especialista en')
	registro    = models.CharField(max_length=20,verbose_name=u'Registro Medico')
	imagen 		= models.ImageField(upload_to=url,null=True,blank=True)
	usuario		= models.ForeignKey(User,null=True,blank=True)
	#Octubre 5 de 2015
	institucion =   models.ForeignKey(instituciones,related_name='medico_institucion',verbose_name=u'Institucion a la que pertenece')

	def __unicode__(self):
		nombreCompleto = "%s %s   %s"%(self.nombre,self.papellido,self.cedula)
		return nombreCompleto

class profesiones(models.Model):
	codigo = models.CharField(max_length=3)
	profesion = models.CharField(max_length=250)
	
	def __unicode__(self):
		return self.profesion	

class paciente(models.Model):
	def url(self,filename):
		ruta = "MultimediaData/Pacientes/%s/%s"%(self.cedula,str(filename))
		return ruta

	opcionesGenero = (
		('M', 'Masculino'),
 		('F', 'Femenino'),
    )

	opcionesEstadoCivil = (
		('C', 'Casado'),
		('U', 'Union Libre'),
		('S', 'Soltero'),
		('V', 'Viudo'),
		('D', 'Divorciado'),
    )

	opciones = (
		('S', 'Si'),
 		('N', 'No'),
    )

	opciones2 = (
		('CC', 'Cédula Ciudadanía'),
		('CE', 'Cédula de Extranjería'),
		('PA', 'Pasaporte'),
		('RC', 'Registro Civil'),
 		('TI', 'Tarjeta de Identidad'),
 		('AS', 'Adulto sin Identificar'),
 		('MS', 'Menor sin Identificar'),
 		('UN', 'Numero Unico de Identificación'),
    )

	opciones3 = (
		('1', 'Años'),
 		('2', 'Meses'),
 		('3', 'Días'),
    )    

	opciones4 = (
		('1', 'Contributivo'),
 		('2', 'Subsidiado'),
 		('3', 'Vinculado'),
 		('4', 'Particular'),
 		('5', 'Otro'),
    )   

	opciones5 = (
		('C', 'Cotizante'),
 		('B', 'Beneficiario'),
 		('A', 'Adicional'),
 		('N', 'Ninguno'),
    ) 

	opciones6 = (
		('U', 'Urbano'),
 		('R', 'Rural'),
    )

	opciones7 = (
		('P', 'Primaria'),
 		('S', 'Secundaria'),
 		('T', 'Tecnico'),
 		('R', 'Tecnologo'),
 		('U', 'Universitaria'),
    )


	pnombre		= models.CharField(max_length=30,verbose_name=u'Primer Nombre')
	snombre		= models.CharField(max_length=30,verbose_name=u'Segundo Nombre',null=True,blank=True)
	papellido	= models.CharField(max_length=30,verbose_name=u'Primer Apellido')
	sapellido	= models.CharField(max_length=30,verbose_name=u'Segundo Apellido')
	genero      = models.CharField(max_length=1, choices=opcionesGenero, verbose_name=u'Genero')
	nacioen 	= models.ForeignKey(departamentos,related_name='pacientes_departamento_nacimiento',verbose_name=u'Nacio en')
	fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
	unidad      = models.CharField(max_length=1, choices=opciones3, default='A',verbose_name=u'Unidad Edad')
	edad        = models.CharField(max_length=2)
	documento   = models.CharField(max_length=2, choices=opciones2, verbose_name=u'Documento')
	cedula      = models.CharField(max_length=20,unique=True)
	estadoCivil = models.CharField(max_length=1, choices=opcionesEstadoCivil, verbose_name="Estado Civil")
	tipo	    = models.CharField(max_length=1, choices=opciones4, default='4',verbose_name=u'Tipo Usuario')
	afiliado    = models.CharField(max_length=1, choices=opciones5, default='N', verbose_name=u'Tipo Afiliado')
	zona   		= models.CharField(max_length=1, choices=opciones6, default='U',verbose_name=u'Zona Residencia')
	escolaridad	= models.CharField(max_length=1, choices=opciones7, default='U',verbose_name=u'Escalonaridad')
	ciudad      = models.ForeignKey(departamentos,related_name='pacientes_departamento_ciudad',verbose_name=u'Ciudad')		
	profesion 	= models.ForeignKey(profesiones,verbose_name=u'Profesion')
	direccion   = models.CharField(max_length=100)
	barrio		= models.CharField(max_length=80)
	Estrato		= models.CharField(max_length=1)
	telefono     = models.CharField(max_length=20)
	celular     = models.CharField(max_length=20, null=True, blank=True)
	status		= models.BooleanField(default=True)
	email		= models.EmailField(max_length=30,null=True, blank=True)
	usuario		= models.ForeignKey(User)  

	# Información Facturación
	procede = models.ForeignKey(empresas,related_name='paciente_empresa',verbose_name=u'Procede de')
	visita = models.DateField(verbose_name="Ultima Visita",default=datetime.date.today)
	foto 		= models.ImageField(upload_to=url,null=True,blank=True)
	firma 		= models.ImageField(upload_to=url,null=True,blank=True)
	#Octubre 5 de 2015
	institucion =   models.ForeignKey(instituciones,related_name='paciente_institucion',verbose_name=u'Institucion que lo atendio')

	def __unicode__(self):
		nombreCompleto = "%s %s  %s"%(self.pnombre,self.papellido,self.cedula)
		return nombreCompleto.encode('utf-8')