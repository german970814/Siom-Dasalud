from django.conf.urls import patterns,url

urlpatterns = patterns('mysite.apps.parametros.views',
	url(r'^procedimientos/$','procedimientos_view',name='vista_procedimientos'),
	url(r'^edit/procedimientos/(?P<id_prod>.*)/$','edit_procedimientos_view',name= "vista_editar_procedimientos"),
	url(r'^add/procedimiento/$','add_procedimiento_view',name= "vista_agregar_procedimiento"),
	url(r'^plantillas/$','plantillas_view',name='vista_plantillas'),
	url(r'^edit/plantillas/(?P<id_prod>.*)/$','edit_plantillas_view',name= "vista_editar_plantillas"),
	url(r'^add/plantilla/$','add_plantilla_view',name= "vista_agregar_plantilla"),
	url(r'^servicios/$','servicios_view',name='vista_servicios'),
	url(r'^actualizar/servicio/$','actualizar_servicio_view',name= "vista_actualizar_servicio"),
)