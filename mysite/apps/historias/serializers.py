from rest_framework import serializers

from .models import orden as Orden, ordenesProducto as OrdenProducto
from mysite.apps.laboratorios.models import Laboratorio
from mysite.apps.laboratorios.mixins import IGModelSerializer
from mysite.apps.datos.serializers import PacienteSerializer
from mysite.apps.organizaciones.serializers import InstitucionSerializer, EmpresaSerializer


class OrdenProductoSerializer(IGModelSerializer):

    class Meta:
        model = OrdenProducto
        fields = ('id', 'orden', 'servicio', )


class OrdenSerializer(IGModelSerializer, serializers.ModelSerializer):

    paciente = PacienteSerializer(fields=('pnombre', 'snombre', 'papellido', 'sapellido', 'cedula', 'foto', 'edad', 'unidad_edad'))
    institucion = InstitucionSerializer(fields=('razon', ))
    empresa = EmpresaSerializer(fields=('razon', ))

    laboratorios = serializers.SerializerMethodField()

    class Meta:
        model = Orden
        fields = ('id', 'paciente', 'fecha', 'empresa', 'institucion', 'empresa_cliente', 'laboratorios', )

    def get_laboratorios(self, obj):
        servicios = Orden.objects.filter(id=obj.id).servicios()
        laboratorios = Laboratorio.objects.filter(servicio__in=servicios).distinct()
        return [{
            'id': laboratorio.id,
            'nombre': laboratorio.nombre,
            'codigo': laboratorio.codigo
        } for laboratorio in laboratorios.iterator()]

    def to_representation(self, obj):
        representation = super(OrdenSerializer, self).to_representation(obj)
        representation['fecha'] = obj.fecha.strftime('%Y-%m-%d')
        return representation
