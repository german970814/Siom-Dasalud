from django.conf.urls import patterns,url

urlpatterns = patterns('mysite.apps.organizaciones.views',
	url(r'^empresas/$','empresas_view',name='vista_empresas'),
	url(r'^add/empresas/$','add_empresas_view',name= "vista_agregar_empresas"),
	url(r'^edit/empresas/(?P<id_prod>.*)/$','edit_empresas_view',name= "vista_editar_empresas"),
	url(r'^instituciones/$','instituciones_view',name='vista_instituciones'),
	url(r'^add/instituciones/$','add_instituciones_view',name= "vista_agregar_instituciones"),
	url(r'^edit/instituciones/(?P<id_prod>.*)/$','edit_instituciones_view',name= "vista_editar_instituciones"),
	url(r'^planes/$','planes_view',name='vista_planes'),
	url(r'^add/planes/$','add_planes_view',name= "vista_agregar_planes"),
	url(r'^edit/planes/(?P<id_prod>.*)/$','edit_planes_view',name= "vista_editar_planes"),
)