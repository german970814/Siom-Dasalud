from django.db import models
from mysite.apps.parametros.models import servicios as Servicio


class OrdenQuerySet(models.QuerySet):
    """
    Queryset para las Ordenes
    """

    def servicios(self):
        """
        Retorna los servicios de laboratorios.
        """
        return Servicio.objects.filter(
            id__in=self.values_list('OrdenProducto_orden__servicio__nombre_id', flat=True))

class OrdenManager(models.Manager.from_queryset(OrdenQuerySet)):
    """
    Manager para Ordenes.
    """

    def servicios_laboratorios(self):
        """
        Retorna las ordenes con servicios de laboratorios
        """
        return self.filter(
            OrdenProducto_orden__servicio__nombre__in=self.servicios()
        ).distinct()
