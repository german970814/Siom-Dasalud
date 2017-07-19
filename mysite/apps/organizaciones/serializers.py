from rest_framework import serializers

from .models import instituciones as Institucion, empresas as Empresa
from mysite.apps.laboratorios.mixins import IGModelSerializer


class EmpresaSerializer(IGModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ('id', 'codigo', 'nit', 'razon', 'direccion', 'telefono', )


class InstitucionSerializer(IGModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = ('id', 'documento', 'numero', 'razon', 'codigo', 'direccion', 'telefono', )
