from django.contrib import admin
from mysite.apps.parametros.models import servicios,serviciosEmpresa,items,procedimientos,consultas,rango_consulta,rango_procedimiento,cie,sutura,honorarios,sala

admin.site.register(servicios)
admin.site.register(serviciosEmpresa)
admin.site.register(items)
admin.site.register(procedimientos)
admin.site.register(consultas)
admin.site.register(rango_consulta)
admin.site.register(rango_procedimiento)
admin.site.register(cie)
admin.site.register(sutura)
admin.site.register(honorarios)
admin.site.register(sala)