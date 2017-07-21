# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.six import BytesIO

from rest_framework import serializers
from rest_framework.parsers import JSONParser

from .models import (
    Laboratorio, Equipo, SeccionTrabajo, Tecnica, Caracteristica, Producto,
    EspecificacionCaracteristica, Bacteriologo, Formato, Resultado, PlantillaArea, Recepcion,
    HojaGasto, PlantillaLaboratorio, Empleado, Recarga
)
from .mixins import IGModelSerializer, IGSerializer
from mysite.apps.parametros.serializers import ServicioSerializer
from mysite.apps.datos.serializers import UsuarioSerializer
from mysite.apps.historias.serializers import OrdenSerializer


class RecepcionSerializer(IGSerializer):
    """
    Serializer para Recepciones.
    """

    orden = OrdenSerializer(fields=('paciente', 'fecha', 'empresa', 'institucion', 'empresa_cliente', 'laboratorios', ), read_only_fields=['paciente', 'fecha'])
    estado_display = serializers.SerializerMethodField()

    class Meta:
        model = Recepcion
        fields = ('id', 'estado', 'orden', 'estado_display', )
        extra_kwargs = {'estado_display': {'read_only': True}, 'estado': {'read_only': True}}

    def get_estado_display(self, obj):
        return obj.get_estado_display()


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

    equipo = EquipoSerializer(fields=('codigo', 'nombre', ), required=False)
    seccion_trabajo = SeccionTrabajoSerializer(fields=('codigo', 'descripcion', ))
    servicio = ServicioSerializer(fields=('nombre'))

    class Meta:
        model = Laboratorio
        fields = (
            'id', 'codigo', 'nombre',
            'codigo_internacional', 'equipo', 'seccion_trabajo',
            'servicio', )


class ProductoSerializer(IGModelSerializer, serializers.ModelSerializer):
    """Serializer de productos."""

    tipo_display = serializers.SerializerMethodField()

    def get_tipo_display(sef, obj):
        return getattr(obj, 'get_tipo_display', lambda: '')()

    class Meta:
        model = Producto
        fields = (
            'id', 'codigo', 'nombre', 'tipo_display',
            'alarma_media', 'alarma_inferior', 'tipo', 'cantidad', )


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


class EmpleadoSerializer(IGModelSerializer, serializers.ModelSerializer):
    """
    Serializer para Empleados.
    """
    save_in_nested = ('usuario', )  # permite crear usuarios a partir de el serializer padre.

    usuario = UsuarioSerializer(fields=('username', 'email', 'password', ))

    class Meta:
        model = Empleado
        fields = ('id', 'usuario', 'nombres', 'apellidos', 'documento', )


class FormatoSerializer(IGSerializer):

    laboratorio = LaboratorioSerializer(fields=('codigo', 'nombre', 'seccion_trabajo'))

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
    laboratorio = LaboratorioSerializer(fields=('codigo', 'nombre', 'seccion_trabajo'))
    orden = OrdenSerializer(fields=('id', ))

    class Meta:
        model = Resultado
        fields = ('id', 'laboratorio', 'bacteriologo', 'fecha', 'resultado', 'orden', 'cerrado')
        extra_kwargs = {'fecha': {'read_only': True}, 'bacteriologo': {'read_only': True}}

    def to_representation(self, instance):
        data = super(ResultadoSerializer, self).to_representation(instance)
        if instance.resultado:
            resultado_string = instance.resultado
            stream = BytesIO(resultado_string.encode('utf-8'))
            data["resultado"] = JSONParser().parse(stream)
        return data


class PlantillaAreaSerializer(IGSerializer):
    """
    Serializer para las plantillas de areas
    """

    producto = ProductoSerializer(fields=('codigo', 'nombre'))
    area = SeccionTrabajoSerializer(fields=('codigo', 'descripcion', ))

    class Meta:
        model = PlantillaArea
        fields = (
            'id', 'cantidad', 'producto', 'area'
        )


class PlantillaLaboratorioSerializer(IGSerializer):
    """
    Serializer para las plantillas de laboratorios
    """

    producto = ProductoSerializer(fields=('codigo', 'nombre', 'tipo', 'tipo_display'))
    laboratorio = LaboratorioSerializer(fields=('codigo', 'codigo_internacional', 'nombre'))

    class Meta:
        model = PlantillaLaboratorio
        fields = (
            'id', 'cantidad', 'producto', 'laboratorio'
        )


class PlantillaSerializer(serializers.Serializer):
    """
    Serializer para las plantillas
    """

    cantidad = serializers.IntegerField()
    producto = ProductoSerializer(fields=('codigo', 'nombre', 'tipo_display', 'tipo'))
    model = serializers.BooleanField()


class HojaGastoSerializer(IGSerializer):
    """
    Serializer de hoja de gastos.
    """

    producto = ProductoSerializer(fields=('codigo', 'nombre', 'tipo', 'tipo_display'))
    orden = OrdenSerializer(fields=('id', ))

    class Meta:
        model = HojaGasto
        fields = ('id', 'cantidad', 'producto', 'orden', )


class RecargaSerializer(IGSerializer):
    """Serializer de Recargas."""

    fecha_vencimiento = serializers.DateField(format='%M-%d-%YY')

    class Meta:
        model = Recarga
        fields = (
            'id', 'producto', 'cantidad', 'fecha', 'fecha_vencimiento',
            'lote', 'distribuidor', 'fabricante', 'marca', 'fecha_distribucion',
            'presentacion', 'invima', 'casa_comercial'
        )
        extra_kwargs = {'fecha': {'read_only': True}, 'producto': {'read_only': True}}
