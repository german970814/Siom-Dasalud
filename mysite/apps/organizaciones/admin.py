from django.contrib import admin
from mysite.apps.organizaciones.models import tipo_empresa,planes_salud,empresas,instituciones,usuario_empresa,eps,arp,afp

admin.site.register(tipo_empresa)
admin.site.register(planes_salud)
admin.site.register(empresas)
admin.site.register(instituciones)
admin.site.register(usuario_empresa)
admin.site.register(eps)
admin.site.register(arp)
admin.site.register(afp)
