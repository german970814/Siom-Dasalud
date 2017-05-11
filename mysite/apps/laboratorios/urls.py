from django.conf.urls import url

from . import views, api

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

# api
urlpatterns += [
    url(r'^api/laboratorios/$', api.lista_laboratorio, name='laboratorios'),
    url(r'^api/laboratorios/(?P<pk>\d+)/$', api.detalle_laboratorio, name='detalle_laboratorio'),
    url(r'^api/equipos/$', api.EquiposListAPI.as_view(), name='equipos'),
    url(r'^api/equipos/(?P<pk>\d+)/$', api.EquipoDetailAPI.as_view(), name='detalle_equipo'),
    url(r'^api/seccion_trabajo/$', api.SeccionesTrabajoListAPI.as_view(), name='secciones_trabajo'),
    url(r'^api/seccion_trabajo/(?P<pk>\d+)/$', api.SeccionTrabajoDetailAPI.as_view(), name='detalle_seccion_trabajo'),
    url(r'^api/tecnicas/$', api.TecnicasListAPI.as_view(), name='tecnicas'),
    url(r'^api/tecnicas/(?P<pk>\d+)/$', api.TecnicaDetailAPI.as_view(), name='detalle_tecnica'),
    url(r'^api/reactivos/$', api.ReactivosListAPI.as_view(), name='reactivos'),
    url(r'^api/reactivos/(?P<pk>\d+)/$', api.ReactivoDetailAPI.as_view(), name='detalle_reactivo'),
    url(r'^api/caracteristicas/$', api.CaracteristicasListAPI.as_view(), name='caracteristicas'),
    url(r'^api/caracteristicas/(?P<pk>\d+)/$', api.CaracteristicaDetailAPI.as_view(), name='detalle_caracteristica'),
    url(r'^api/especificacion_caracteristicas/$', api.EspecificacionCaracteristicasListAPI.as_view(), name='especificacion_caracteristicas'),
    url(r'^api/especificacion_caracteristicas/(?P<pk>\d+)/$', api.EspecificacionCaracteristicaDetailAPI.as_view(), name='detalle_especificacion_caracteristica'),
    url(r'^api/ordenes_laboratorios/$', api.ordenes_laboratorios, name='ordenes_laboratorios'),
    url(r'^api/servicios/$', api.ServiciosListAPI.as_view(), name='servicios'),
    url(r'^api/servicios/(?P<pk>\d+)/$', api.ServicioLaboratorioAPI.as_view(), name='detalle_servicio'),
    url(r'^api/formatos/(?P<pk>\d+)/$', api.formato_api_view, name='formato_laboratorio'),
    url(r'^api/especificacion_caracteristicas/caracteristica/(?P<pk>\d+)/$',
        api.especificacion_caracteristica_por_caracteristica, name='especificaciones_por_carateristica'),
]
