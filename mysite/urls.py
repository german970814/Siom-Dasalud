from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

if settings.DEBUG:
    import debug_toolbar

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^laboratorios/', include('mysite.apps.laboratorios.urls', namespace='laboratorios')),
    url(r'^examenes/', include('mysite.apps.examenes.urls', namespace='examenes')),
    url(r'^',include('mysite.apps.citas.urls')),
    url(r'^',include('mysite.apps.home.urls')),
    url(r'^',include('mysite.apps.historias.urls')),
    url(r'^',include('mysite.apps.datos.urls')),
    url(r'^',include('mysite.apps.organizaciones.urls')),
    url(r'^',include('mysite.apps.parametros.urls')),
    url(r'^__debug__/', include(debug_toolbar.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^static/(?P<path>.*)', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
        url(r'^media/(?P<path>.*)', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
