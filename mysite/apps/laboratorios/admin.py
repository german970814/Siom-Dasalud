from django.contrib import admin
from .models import (
    Laboratorio, Equipo, SeccionTrabajo,
    Tecnica, Formato, Bacteriologo, Empleado,
    Recarga, Resultado, Recepcion
)
from reversion.admin import VersionAdmin


admin.site.register(Laboratorio)
admin.site.register(Equipo)
admin.site.register(SeccionTrabajo)
admin.site.register(Tecnica)
admin.site.register(Formato)
admin.site.register(Bacteriologo)
admin.site.register(Empleado)
admin.site.register(Recarga)
admin.site.register(Resultado)
admin.site.register(Recepcion, VersionAdmin)
