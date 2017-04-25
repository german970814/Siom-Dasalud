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
    url(r'^api/seccion_trabajo/$', api.SeccionesTrabajoListAPI.as_view(), name='secciones_trabajo'),
]
