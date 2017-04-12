from django.contrib import admin
from mysite.apps.facturacion.models import factura,categorias,producto,detalle

class facturaAdmin(admin.ModelAdmin):
	#Atributo para mostrar campos del modelo
	list_display = ('numero', 'letra_factura', 'orden', 'fecha_emision', 'fecha_vencimiento', 'fecha_atencion')
	#Agrega un buscador
	search_fields = ('orden', 'fecha_emision')

admin.site.register(factura,facturaAdmin)
admin.site.register(categorias)
admin.site.register(producto)
admin.site.register(detalle)