from rest_framework import serializers

from .models import servicios as Servicio
from mysite.apps.laboratorios.mixins import IGModelSerializer


class ServicioSerializer(IGModelSerializer, serializers.ModelSerializer):
    """
    Serializer para los Servicios
    """

    class Meta:
        model = Servicio
        fields = ('id', 'nombre', 'costo', )
