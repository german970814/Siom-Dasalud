from django.db import models
from django.contrib.auth.models import User
#from mysite.apps.organizaciones.models import instituciones
#from mysite.apps.organizaciones.models import instituciones

def url(obj,filename):
	ruta = "MultimediaData/Users/%s/%s"%(obj.user.username,filename)
	return ruta

class departamentos(models.Model):
	codigo 				= models.CharField(max_length=2)
	codigo_municipio	= models.CharField(max_length=4)
	codigo_poblado	= models.CharField(max_length=10)
	nombre_depto = models.CharField(max_length=50)
	nombre_municipio = models.CharField(max_length=50)
	nombre_poblado = models.CharField(max_length=50)
	tipo_poblado = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre_municipio		

class userProfile(models.Model):
	user 		=	models.OneToOneField(User)
	#photo 		=	models.ImageField(upload_to=url)
	#telefono	=	models.CharField(max_length=30)
	#Octubre 5 de 2015
	institucion =   models.ForeignKey("organizaciones.instituciones",related_name='userprofile_institucion',verbose_name=u'Institucion a la que pertenece')
	
	def __unicode__(self):
		return self.user.username

	class Meta:
		permissions = (
			("es_administrador", "Administrador"),
			("es_coordinador_general", "Coordinador General"),
			("es_coordinador_plataforma", "Coordinador Plataforma"),
			("es_coordinador_endoscopia", "Coordinador Endoscopia"),
			("es_auxiliar_plataforma", "Auxiliar Plataforma"),
			("es_auxiliar_endoscopia", "Auxiliar Endoscopia"),            
			("es_auxiliar_contabilidad", "Auxiliar Contabilidad"),
			("es_auxiliar_enfermeria", "Auxiliar Enfermeria"),
			("es_doctor", "Doctor"),
		) 
								