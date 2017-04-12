from django.contrib import admin
from mysite.apps.historias.models import orden,ordenesProducto,historia_clinica,test_altura,historia_procedimientos,laboratorios,posologias,remision,remisionlab

class historiaAdmin(admin.ModelAdmin):
	#Atributo para mostrar campos del modelo
	list_display = ('id','concepto')
	#Agrega un buscador
	#search_fields = ('paciente.pnombre','papellido','sapellido')

class ordenAdmin(admin.ModelAdmin):
	#Atributo para mostrar campos del modelo
	list_display = ('id','paciente', 'fecha', 'medico','empresa','institucion','generadapor')
	list_filter = ('fecha','institucion','empresa')
	search_fields = ('id','paciente__cedula') #Agrega un buscador
	#list_editable = ('valor', 'anulada')	

admin.site.register(orden,ordenAdmin)
admin.site.register(ordenesProducto)
admin.site.register(historia_clinica,historiaAdmin)
admin.site.register(test_altura)
admin.site.register(historia_procedimientos)
admin.site.register(laboratorios)
admin.site.register(posologias)
admin.site.register(remision)
admin.site.register(remisionlab)