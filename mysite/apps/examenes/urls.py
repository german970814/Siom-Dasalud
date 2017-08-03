from django.conf.urls import url

from . import views, api

urlpatterns = [
    url(r'^$', views.index, name='index_visiometria'),
    url(r'^resultado/visiometria/(?P<pk>\d+)/$', views.ver_resultado_visiometria, name='ver_resultado_visiometria'),
]

# api
urlpatterns += [
    url(r'^api/visiometria/recepcion/$', api.OrdenesSinVisiometriaListAPI.as_view(), name='ordenes_sin_visiometia'),
    url(r'^api/visiometria/$', api.VisiometriaListAPI.as_view(), name='ordenes_sin_visiometia'),
    url(r'^api/visiometria/(?P<pk>\d+)/$', api.VisiometriaRetrieveUpdateAPI.as_view(), name='visiometria'),
]
