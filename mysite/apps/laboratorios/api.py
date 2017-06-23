# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.utils import timezone

from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import permissions, generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.pagination import PageNumberPagination

from .models import (
    Laboratorio, Equipo, SeccionTrabajo, Tecnica, Caracteristica, Producto,
    EspecificacionCaracteristica, Formato, Bacteriologo, Resultado,
    PlantillaArea, Recepcion, HojaGasto, PlantillaLaboratorio
)
from .serializers import (
    LaboratorioSerializer, EquipoSerializer, SeccionTrabajoSerializer,
    TecnicaSerializer, CaracteristicaSerializer, ProductoSerializer,
    EspecificacionCaracteristicaSerializer, FormatoSerializer, BacteriologoSerializer,
    ResultadoSerializer, PlantillaAreaSerializer, PlantillaSerializer,
    RecepcionSerializer, HojaGastoSerializer, PlantillaLaboratorioSerializer
)
from .utils import ListViewAPIMixin
from mysite.apps.historias.models import ordenesProducto as OrdenProducto, orden as Orden
from mysite.apps.historias.serializers import OrdenSerializer
from mysite.apps.parametros.models import servicios as Servicio
from mysite.apps.parametros.serializers import ServicioSerializer

import datetime
import reversion


class LaboratoriosListAPI(ListViewAPIMixin, generics.ListCreateAPIView):
    queryset = Laboratorio.objects.all()
    serializer_class = LaboratorioSerializer
    search_params = (
        'nombre', 'codigo', 'codigo_internacional',
        'equipo__nombre', 'equipo__codigo', 'seccion_trabajo__codigo',
        'seccion_trabajo__descripcion'
    )


class EquiposListAPI(generics.ListCreateAPIView):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer


class EquipoDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer


class SeccionesTrabajoListAPI(generics.ListCreateAPIView):
    queryset = SeccionTrabajo.objects.all()
    serializer_class = SeccionTrabajoSerializer


class SeccionTrabajoDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = SeccionTrabajo.objects.all()
    serializer_class = SeccionTrabajoSerializer


class TecnicasListAPI(generics.ListCreateAPIView):
    queryset = Tecnica.objects.all()
    serializer_class = TecnicaSerializer


class TecnicaDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tecnica.objects.all()
    serializer_class = TecnicaSerializer


class ProductosListAPI(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filter_fields = ['tipo']


class ProductoDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class CaracteristicasListAPI(generics.ListCreateAPIView):
    queryset = Caracteristica.objects.all()
    serializer_class = CaracteristicaSerializer


class CaracteristicaDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Caracteristica.objects.all()
    serializer_class = CaracteristicaSerializer


class EspecificacionCaracteristicasListAPI(generics.ListCreateAPIView):
    queryset = EspecificacionCaracteristica.objects.all()
    serializer_class = EspecificacionCaracteristicaSerializer


class EspecificacionCaracteristicaDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = EspecificacionCaracteristica.objects.all()
    serializer_class = EspecificacionCaracteristicaSerializer


class ServiciosListAPI(generics.ListAPIView):
    queryset = Servicio.objects.filter(laboratorio__isnull=True)
    serializer_class = ServicioSerializer


class ServicioLaboratorioAPI(generics.RetrieveAPIView):
    queryset = Servicio.objects.filter(laboratorio__isnull=False)
    serializer_class = ServicioSerializer


class BacteriologoListAPI(generics.ListCreateAPIView):
    queryset = Bacteriologo.objects.all()
    serializer_class = BacteriologoSerializer


class BacteriologoDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bacteriologo.objects.all()
    serializer_class = BacteriologoSerializer


class PlantillaAreaListAPI(generics.ListCreateAPIView):
    queryset = PlantillaArea.objects.all()
    serializer_class = PlantillaAreaSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = super(PlantillaAreaListAPI, self).get_queryset(*args, **kwargs)
        area = self.request.GET.get('area', None)
        if area:
            area = get_object_or_404(SeccionTrabajo, pk=area)
            queryset = area.plantillas.all()
        return queryset


class PlantillaAreaDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlantillaArea.objects.all()
    serializer_class = PlantillaAreaSerializer


class PlantillaLaboratorioAPI(generics.ListCreateAPIView):
    queryset = PlantillaLaboratorio.objects.all()
    serializer_class = PlantillaLaboratorioSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = super(PlantillaLaboratorioAPI, self).get_queryset(*args, **kwargs)
        laboratorio = self.request.GET.get('laboratorio', None)
        if laboratorio:
            laboratorio = get_object_or_404(Laboratorio, pk=laboratorio)
            queryset = laboratorio.plantillas.all()
        return queryset


class PlantillaLaboratorioDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlantillaLaboratorio.objects.all()
    serializer_class = PlantillaLaboratorioSerializer


@api_view(['GET'])
def ordenes_toma_muestra(request):
    """
    Lista las ordenes que vienen de recepcion y son enviadas al area de toma de muestra.
    Aqui empieza el proceso de trazabilidad de un laboratorio.
    """
    hoy = timezone.now().date()
    servicios = Laboratorio.objects.all().values_list('servicio_id', flat=True)
    recepciones = Recepcion.objects.all().values_list('orden__id', flat=True)

    ordenes = Orden.objects.filter(  # actuelmente solo se traen los ultimos 8 días.
        id__in=OrdenProducto.objects.filter(
            servicio__nombre__id__in=servicios
        ).values_list('orden_id', flat=True).distinct(),
        fecha__range=(hoy - datetime.timedelta(days=32), hoy)
    ).order_by('-fecha').exclude(id__in=recepciones)  # .select_related('paciente')

    serializer = OrdenSerializer(ordenes, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def recepcion_api(request):
    """
    Vista para crear una recepcion y sus hojas de gasto.
    """

    args = tuple()
    kwargs = {}

    serializer = RecepcionSerializer(data=request.data)
    if 'hoja_gasto' in request.data:
        serializer_hoja_gasto = HojaGastoSerializer(data=request.data['hoja_gasto'], many=True)
        valid_serializer = serializer.is_valid()
        valid_hoja_gasto = serializer_hoja_gasto.is_valid()
        if valid_hoja_gasto and valid_serializer:
            serializer.save(estado=Recepcion.EN_CURSO)
            serializer_hoja_gasto.save()
            args = ([serializer.data, serializer_hoja_gasto.data], )
        else:
            args = ([getattr(serializer, 'errors', []), getattr(serializer_hoja_gasto, 'errors', [])], )
            kwargs['status'] = status.HTTP_400_BAD_REQUEST
    else:
        if serializer.is_valid():
            serializer.save(estado=Recepcion.EN_CURSO)
            args = (serializer.data, )
        else:
            args = (serializer.errors, )
            kwargs['status'] = status.HTTP_400_BAD_REQUEST

    return Response(*args, **kwargs)


@api_view(['GET'])
def ordenes_laboratorios(request):
    """
    Lista las ordenes que tengan laboratorios.
    """

    args = tuple()
    kwargs = {}
    try:
        bacteriologo = request.user.bacteriologo
    except:
        kwargs['status'] = status.HTTP_403_FORBIDDEN
        return Response(**kwargs)

    pagination = PageNumberPagination()
    pagination.page_size = 10

    ordenes = Recepcion.objects.filter(
        estado=Recepcion.EN_CURSO).select_related('orden').order_by('-orden__fecha')

    result_pagination = pagination.paginate_queryset(ordenes, request)
    # serializer = OrdenSerializer(result_pagination, many=True)
    serializer = RecepcionSerializer(result_pagination, many=True)

    return pagination.get_paginated_response(serializer.data)


@api_view(['GET'])
def search_resultado_api_view(request):
    """
    Vista para buscar y listar todas las ordenes o recepciones de acuerdo a un parametro
    de busqueda.
    """

    param = request.GET.get('param', '')
    pagination = PageNumberPagination()
    pagination.page_size = 10
    querys = (
        Q(orden__paciente__pnombre__icontains=param) | Q(orden__paciente__papellido__icontains=param) |
        Q(orden__paciente__cedula__icontains=param) | Q(orden__id__icontains=param) |
        Q(orden__institucion__razon__icontains=param) | Q(orden__empresa__razon__icontains=param) |
        Q(orden__empresa_cliente__icontains=param)
    )

    servicios = Laboratorio.objects.all().values_list('servicio_id', flat=True)

    ordenes = Recepcion.objects.filter(querys).select_related('orden').order_by('-orden__fecha')

    result_pagination = pagination.paginate_queryset(ordenes, request)
    serializer = RecepcionSerializer(result_pagination, many=True)
    return pagination.get_paginated_response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def detalle_laboratorio(request, pk):
    """
    CRUD para los laboratorios.
    """

    args = tuple()
    kwargs = dict()

    laboratorio = get_object_or_404(Laboratorio, pk=pk)

    if request.method == 'GET':
        serializer = LaboratorioSerializer(laboratorio)
        args = (serializer.data, )
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LaboratorioSerializer(laboratorio, data=data)
        if serializer.is_valid():
            serializer.save()
            args = (serializer.data, )
        else:
            args = (serializer.errors, )
            kwargs['status'] = status.HTTP_400_BAD_REQUEST
    elif request.method == 'DELETE':
        laboratorio.delete()
        kwargs['status'] = status.HTTP_204_NO_CONTENT

    return Response(*args, **kwargs)


@api_view(['POST', 'GET'])
def resultado_api_view(request, pk):
    """
    Vista para listar el formato de resultado y guardar el resultado de un laboratorio.
    """

    orden = get_object_or_404(Orden, pk=pk)
    args = tuple()
    kwargs = {}

    try:
        bacteriologo = request.user.bacteriologo
    except:
        kwargs['status'] = status.HTTP_403_FORBIDDEN
        return Response(**kwargs)

    if request.method == 'GET':
        data = {}
        resultados = orden.resultados_laboratorio.all()
        serializer_resultados = ResultadoSerializer(resultados, many=True)
        data['resultados'] = serializer_resultados.data

        laboratorios = Laboratorio.objects.filter(
            id__in=list(filter(
                lambda x: x is not None,
                Orden.objects.filter(
                    id=orden.id).servicios().values_list('laboratorio__id', flat=True)
                ))
            ).exclude(
                id__in=resultados.values_list('laboratorio__id', flat=True)
            )

        formatos = Formato.objects.filter(id__in=laboratorios.values_list('formato__id', flat=True))
        serializer = FormatoSerializer(formatos, many=True)
        data['formatos'] = serializer.data
        data['orden'] = OrdenSerializer(orden).data
        data['bacteriologo'] = BacteriologoSerializer(bacteriologo).data
        args = (data, )

    if request.method == 'POST':
        kwargs_serializer = {'data': request.data}

        if 'id' in request.data:
            kwargs_serializer['instance'] = get_object_or_404(Resultado, pk=request.data['id'])

        serializer = ResultadoSerializer(**kwargs_serializer)

        if serializer.is_valid():
            with reversion.create_revision():
                serializer.save(bacteriologo=bacteriologo)
                args = (serializer.data, )
                kwargs['status'] = status.HTTP_201_CREATED

                reversion.set_user(request.user)
        else:
            args = (serializer.errors, )
            kwargs['status'] = status.HTTP_400_BAD_REQUEST

    return Response(*args, **kwargs)


@api_view(['GET', 'POST'])
def formato_api_view(request, pk):
    """"""

    laboratorio = get_object_or_404(Laboratorio.objects.all(), pk=pk)
    args = tuple()
    kwargs = {}

    if request.method == 'GET':
        try:
            formato = laboratorio.formato
        except Formato.DoesNotExist:
            formato = Formato(laboratorio=laboratorio)
        serializer = FormatoSerializer(instance=formato)
        args = (serializer.data, )
    elif request.method == 'POST':
        try:
            formato = laboratorio.formato
            formato = FormatoSerializer.update(FormatoSerializer(), formato, request.data)
        except:
            formato = FormatoSerializer.create(FormatoSerializer(), request.data)
        formato = Formato.objects.get(laboratorio=laboratorio)
        serializer = FormatoSerializer(instance=formato)
        args = (serializer.data, )
        kwargs['status'] = status.HTTP_201_CREATED

    return Response(*args, **kwargs)


@api_view(['GET'])
def especificacion_caracteristica_por_caracteristica(request, pk):
    """
    Retorna las especificaciones de una caracteristica
    """
    args = tuple()
    if request.method == 'GET':
        especificaciones = EspecificacionCaracteristica.objects.filter(caracteristica_id=pk)
        serializer = EspecificacionCaracteristicaSerializer(especificaciones, many=True)
        args = (serializer.data, )
    return Response(*args)


@api_view(['GET'])
def plantillas_orden(request, pk):
    """
    Permite ver las plantillas que posee una orden.
    """

    _plantilla = {}
    data = []
    orden = get_object_or_404(Orden, pk=pk)

    _filter = {}
    if request.GET.get('tipo', None):
        _filter['producto__tipo'] = str(request.GET.get('tipo')).upper()

    servicios = orden.OrdenProducto_orden.all().values_list('servicio__nombre__laboratorio__id', flat=True)
    laboratorios = Laboratorio.objects.filter(id__in=servicios).select_related('seccion_trabajo').prefetch_related('plantillas')

    # primero separamos los laboratorios por area.
    areas = SeccionTrabajo.objects.filter(
        id__in=laboratorios.values_list('seccion_trabajo', flat=True)).prefetch_related('plantillas')

    for area in areas:
        for plantilla in area.plantillas.filter(**_filter):
            if not (plantilla.producto in _plantilla) or (
               plantilla.producto in _plantilla and plantilla.cantidad > _plantilla[plantilla.producto]):
                _plantilla[plantilla.producto] = plantilla.cantidad

    for laboratorio in laboratorios:
        for plantilla in laboratorio.plantillas.filter(**_filter):
            if not (plantilla.producto in _plantilla) or (
               plantilla.producto in _plantilla and plantilla.cantidad > _plantilla[plantilla.producto]):
                _plantilla[plantilla.producto] = plantilla.cantidad

    for plantilla in _plantilla:
        data.append({'producto': plantilla, 'cantidad': _plantilla[plantilla], 'model': True})

    return Response(PlantillaSerializer(data, many=True).data)
