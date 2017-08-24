from django.conf.urls import url

from . import views, api

urlpatterns = [
    url(r'^$', views.index, name='index_visiometria'),
    url(r'^nueva/(?P<pk>\d+)/$', views.visiometria_create, name='visiometria_nueva'),
    url(r'^resultado/visiometria/(?P<pk>\d+)/$', views.ver_resultado_visiometria, name='ver_resultado_visiometria'),
]

# api
urlpatterns += [
    url(r'^api/visiometria/recepcion/$', api.OrdenesSinVisiometriaListAPI.as_view(), name='ordenes_sin_visiometia'),
    url(r'^api/visiometria/$', api.VisiometriaListAPI.as_view(), name='ordenes_sin_visiometia'),
    url(r'^api/visiometria/(?P<pk>\d+)/$', api.VisiometriaRetrieveUpdateAPI.as_view(), name='visiometria'),
    url(r'^api/visiometra/$', api.EmpleadoListAPI.as_view(), name='visiometra'),
    url(r'^api/visiometra/(?P<pk>\d+)/$', api.EmpleadoRetrieveUpdateAPI.as_view(), name='visiometra_update'),
    url(r'^api/visiometra/firma/(?P<pk>\d+)/$', api.cambiar_firma_visiometra, name='cambiar_firma_visiometra'),
]
