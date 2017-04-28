from rest_framework import serializers
from django.core.exceptions import FieldDoesNotExist

from .models import Laboratorio, Equipo, SeccionTrabajo, Tecnica, Reactivo, Caracteristica, EspecificacionCaracteristica

import copy


class IGModelSerializer(object):
    """"""

    # id = serializers.IntegerField(required=False, read_only=False)

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super(IGModelSerializer, self).__init__(*args, **kwargs)
        if fields is not None:
            self.nested = True
            for field in self.fields:
                if field not in fields and field != 'id':
                    self.fields.pop(field)

    def get_extra_kwargs(self):
        extra_kwargs = super(IGModelSerializer, self).get_extra_kwargs()
        if getattr(self, 'nested', False):
            extra_kwargs['id'] = {'read_only': False}
        return extra_kwargs

    def create(self, data):
        Model = self.Meta.model
        for field in data:
            try:
                if Model._meta.get_field(field).is_relation:
                    data[field] = Model._meta.get_field(
                        field).related_model.objects.get(pk=data[field]['id'])
            except FieldDoesNotExist:
                continue
        instance, created = Model.objects.get_or_create(**data)
        return instance

    def update(self, instance, data):
        Model = self.Meta.model

        for field in data:
            try:
                if Model._meta.get_field(field).is_relation:
                    data[field] = Model._meta.get_field(
                        field).related_model.objects.get(pk=data[field]['id'])
            except FieldDoesNotExist:
                continue

        for field in data:
            setattr(instance, field, data[field])

        instance.save()
        return instance


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

    class Meta:
        model = Laboratorio
        fields = ('id', 'codigo', 'nombre', 'codigo_internacional', 'equipo', 'seccion_trabajo', )
        # read_only_fields = ('equipo', 'seccion_trabajo', )
        # extra_kwargs = {'id': {'read_only': False}}


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
