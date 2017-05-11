# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.six import BytesIO
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.fields import CharField

from .models import (
    Laboratorio, Equipo, SeccionTrabajo,
    Tecnica, Reactivo, Caracteristica,
    EspecificacionCaracteristica, Bacteriologo, Formato
)
from .mixins import IGModelSerializer, IGSerializer
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
        fields = ('id', 'codigo', 'nombre', 'laboratorio', 'alarma_media', 'alarma_inferior', 'costos', )


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


class _FormatoSerializer_(CharField):
    def to_representation(self, value):
        from django.utils import six
        return six.text_type(value.decode('utf-8'))

class FormatoSerializer(IGSerializer):

    laboratorio = LaboratorioSerializer(fields=('codigo', 'nombre', ))
    # formato = _FormatoSerializer_()

    class Meta:
        model = Formato
        fields = ('id', 'formato', 'laboratorio', )

    def to_representation(self, instance):
        data = super(FormatoSerializer, self).to_representation(instance)
        if instance.formato:
            formato_string = instance.formato
            stream = BytesIO(formato_string.encode('utf-8'))
            data["formato"] = JSONParser().parse(stream)
        return data
