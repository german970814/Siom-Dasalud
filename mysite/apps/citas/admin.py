from django.contrib import admin
from mysite.apps.citas.models import agenda_consulta,agenda_procedimiento,citas_consulta,citas_procedimiento

admin.site.register(agenda_consulta)
admin.site.register(agenda_procedimiento)
admin.site.register(citas_consulta)
admin.site.register(citas_procedimiento)