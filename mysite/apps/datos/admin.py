from django.contrib import admin
from mysite.apps.datos.models import especialidades,paciente,medico,profesiones

class pacienteAdmin(admin.ModelAdmin):
	#Atributo para mostrar campos del modelo
	list_display = ('id','documento','cedula', 'pnombre','snombre','papellido','sapellido','genero',)
	#Agrega un buscador
	search_fields = ('cedula','pnombre','papellido','sapellido')

admin.site.register(especialidades)
admin.site.register(paciente,pacienteAdmin)
admin.site.register(medico)
admin.site.register(profesiones)
