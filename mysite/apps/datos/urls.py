from django.conf.urls import patterns,url

urlpatterns = patterns('mysite.apps.datos.views',
	url(r'^medicos/$','medicos_view',name='vista_medicos'),
	url(r'^pacientes/page/(?P<pagina>.*)/$','pacientes_view',name='vista_pacientes'),
	url(r'^add/paciente/$','add_paciente_view',name= "vista_agregar_paciente"),
	url(r'^edit/paciente/(?P<id_prod>.*)/$','edit_paciente_view',name= "vista_edit_paciente"),
	url(r'^historial/paciente/(?P<id_prod>.*)/$','historial_paciente_view',name= "vista_historial_paciente"),
)