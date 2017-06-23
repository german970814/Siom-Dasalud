from django.conf.urls import url

from . import views, api

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^imprimir/(?P<pk>\d+)/$', views.imprimir_laboratorio, name='imprimir'),
    url(r'^pr/(?P<pk>\d+)/$', views.prueba, name='imprimir_pras'),
]

# api
urlpatterns += [
    url(r'^api/laboratorios/$', api.LaboratoriosListAPI.as_view(), name='laboratorios'),
    url(r'^api/laboratorios/(?P<pk>\d+)/$', api.detalle_laboratorio, name='detalle_laboratorio'),
    url(r'^api/laboratorios/plantilla/(?P<pk>\d+)/$', api.plantillas_orden, name='plantilla_laboratorios'),
    url(r'^api/laboratorios/plantilla_laboratorios/$', api.PlantillaLaboratorioAPI.as_view(), name='plantillas_laboratorio'),
    url(r'^api/laboratorios/plantilla_laboratorios/(?P<pk>\d+)/$', api.PlantillaLaboratorioDetailAPI.as_view(), name='detalle_plantillas_laboratorio'),
    url(r'^api/equipos/$', api.EquiposListAPI.as_view(), name='equipos'),
    url(r'^api/equipos/(?P<pk>\d+)/$', api.EquipoDetailAPI.as_view(), name='detalle_equipo'),
    url(r'^api/seccion_trabajo/$', api.SeccionesTrabajoListAPI.as_view(), name='secciones_trabajo'),
    url(r'^api/seccion_trabajo/(?P<pk>\d+)/$', api.SeccionTrabajoDetailAPI.as_view(), name='detalle_seccion_trabajo'),
    url(r'^api/seccion_trabajo/plantillas/$', api.PlantillaAreaListAPI.as_view(), name='plantillas_area'),
    url(r'^api/seccion_trabajo/plantillas/(?P<pk>\d+)/$', api.PlantillaAreaDetailAPI.as_view(), name='detalle_plantillas_area'),
    url(r'^api/tecnicas/$', api.TecnicasListAPI.as_view(), name='tecnicas'),
    url(r'^api/tecnicas/(?P<pk>\d+)/$', api.TecnicaDetailAPI.as_view(), name='detalle_tecnica'),
    url(r'^api/productos/$', api.ProductosListAPI.as_view(), name='productos'),
    url(r'^api/productos/(?P<pk>\d+)/$', api.ProductoDetailAPI.as_view(), name='detalle_producto'),
    url(r'^api/bacteriologos/$', api.BacteriologoListAPI.as_view(), name='bacteriologos'),
    url(r'^api/bacteriologos/(?P<pk>\d+)/$', api.BacteriologoDetailAPI.as_view(), name='detalle_bacteriologo'),
    url(r'^api/caracteristicas/$', api.CaracteristicasListAPI.as_view(), name='caracteristicas'),
    url(r'^api/caracteristicas/(?P<pk>\d+)/$', api.CaracteristicaDetailAPI.as_view(), name='detalle_caracteristica'),
    url(r'^api/especificacion_caracteristicas/$', api.EspecificacionCaracteristicasListAPI.as_view(), name='especificacion_caracteristicas'),
    url(r'^api/especificacion_caracteristicas/(?P<pk>\d+)/$', api.EspecificacionCaracteristicaDetailAPI.as_view(), name='detalle_especificacion_caracteristica'),
    url(r'^api/ordenes_laboratorios/$', api.ordenes_laboratorios, name='ordenes_laboratorios'),
    url(r'^api/servicios/$', api.ServiciosListAPI.as_view(), name='servicios'),
    url(r'^api/servicios/(?P<pk>\d+)/$', api.ServicioLaboratorioAPI.as_view(), name='detalle_servicio'),
    url(r'^api/formatos/(?P<pk>\d+)/$', api.formato_api_view, name='formato_laboratorio'),
    url(r'^api/resultado/(?P<pk>\d+)/$', api.resultado_api_view, name='resultado'),
    url(r'^api/ordenes/buscar/$', api.search_resultado_api_view, name='busqueda_ordenes'),
    url(r'^api/ordenes/toma_muestra/$', api.ordenes_toma_muestra, name='ordenes_toma_muestra'),
    url(r'^api/especificacion_caracteristicas/caracteristica/(?P<pk>\d+)/$',
        api.especificacion_caracteristica_por_caracteristica, name='especificaciones_por_carateristica'),
]
