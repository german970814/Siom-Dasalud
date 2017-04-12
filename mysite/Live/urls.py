from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('mysite.apps.citas.urls')),
    url(r'^',include('mysite.apps.home.urls')),
    url(r'^',include('mysite.apps.historias.urls')),
    url(r'^',include('mysite.apps.datos.urls')),
    url(r'^',include('mysite.apps.organizaciones.urls')),
    url(r'^',include('mysite.apps.parametros.urls')),
)
