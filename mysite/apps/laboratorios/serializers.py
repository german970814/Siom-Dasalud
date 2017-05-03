from rest_framework import serializers

from .models import (
    Laboratorio, Equipo, SeccionTrabajo,
    Tecnica, Reactivo, Caracteristica,
    EspecificacionCaracteristica, Bacteriologo
)
from .mixins import IGModelSerializer
from mysite.apps.parametros.serializers import ServicioSerializer


class TecnicaSerializer(IGModelSerializer, serializers.ModelSerializer):
    """
    Serializer de tecnicas.
    """

    class Meta:
        model = Tecnica
        fields = ('id', 'codigo', 'nombre', )
        # extra_kwargs = {'id': {'read_only': False}}


class EquipoSerializer(IGModelSerializer, serializers.ModelSerializer):
    """
    Serializzer para los equipos.
    """

    tecnica = TecnicaSerializer(fields=('codigo', 'nombre'))

    class Meta:
        model = Equipo
        fields = ('id', 'codigo', 'nombre', 'tecnica', )
        # extra_kwargs = {'id': {'read_only': False}}


class SeccionTrabajoSerializer(IGModelSerializer, serializers.ModelSerializer):
    """
    Serializer para las secciones de trabajo
    """

    class Meta:
        model = SeccionTrabajo
        fields = ('id', 'codigo', 'descripcion', )
        # extra_kwargs = {'id': {'read_only': False}}


class LaboratorioSerializer(IGModelSerializer, serializers.ModelSerializer):
    """
    Serializer para los laboratorios.
    """

    equipo = EquipoSerializer(fields=('codigo', 'nombre', ))
    seccion_trabajo = SeccionTrabajoSerializer(fields=('codigo', 'descripcion', ))
    servicio = ServicioSerializer(fields=('nombre'))

    class Meta:
        model = Laboratorio
        fields = (
            'id', 'codigo', 'nombre',
            'codigo_internacional', 'equipo', 'seccion_trabajo',
            'servicio', )


class ReactivoSerializer(IGModelSerializer, serializers.ModelSerializer):

    laboratorio = LaboratorioSerializer(fields=('codigo', 'nombre', ))

    class Meta:
        model = Reactivo
        fields = ('id', 'codigo', 'nombre', 'laboratorio', 'alarma_media', 'alarma_inferior', 'costos')


class CaracteristicaSerializer(IGModelSerializer, serializers.ModelSerializer):

    class Meta:
        model = Caracteristica
        fields = ('id', 'codigo', 'descripcion', )


class EspecificacionCaracteristicaSerializer(IGModelSerializer, serializers.ModelSerializer):
    caracteristica = CaracteristicaSerializer(fields=('codigo', 'descripcion', ))
    class Meta:
        model = EspecificacionCaracteristica
        fields = ('id', 'nombre', 'caracteristica', )


class BacteriologoSerializer(IGModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = Bacteriologo
        fields = ('id', 'usuario', 'codigo', 'nombre', 'registro', 'firma', 'areas', )
