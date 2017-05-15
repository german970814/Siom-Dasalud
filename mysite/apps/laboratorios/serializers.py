# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.six import BytesIO
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.parsers import JSONParser

from .models import (
    Laboratorio, Equipo, SeccionTrabajo,
    Tecnica, Reactivo, Caracteristica,
    EspecificacionCaracteristica, Bacteriologo,
    Formato, Resultado
)
from .mixins import IGModelSerializer, IGSerializer
from mysite.apps.parametros.serializers import ServicioSerializer
from mysite.apps.datos.serializers import UsuarioSerializer


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
    """
    Serializer para bacteriologos.
    """
    save_in_nested = ('usuario', )  # permite crear usuarios a partir de el serializer padre.

    usuario = UsuarioSerializer(fields=('username', 'email', 'password', ))
    areas = SeccionTrabajoSerializer(fields=('codigo', 'descripcion', ), many=True)

    class Meta:
        model = Bacteriologo
        fields = ('id', 'usuario', 'codigo', 'nombre', 'registro', 'firma', 'areas', )


class FormatoSerializer(IGSerializer):

    laboratorio = LaboratorioSerializer(fields=('codigo', 'nombre', ))

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


class ResultadoSerializer(IGSerializer):
    laboratorio = LaboratorioSerializer(fields=('codigo', 'nombre', ))
    # orden = OrdenSerializer(fields=)

    class Meta:
        model = Resultado
        fields = ('id', 'laboratorio', 'bacteriologo', 'fecha', 'resultado', )
