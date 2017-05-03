from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
# from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import permissions, generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from .models import (
    Laboratorio, Equipo, SeccionTrabajo, Tecnica, Reactivo, Caracteristica,
    EspecificacionCaracteristica
)
from .serializers import (
    LaboratorioSerializer, EquipoSerializer, SeccionTrabajoSerializer,
    TecnicaSerializer, ReactivoSerializer, CaracteristicaSerializer,
    EspecificacionCaracteristicaSerializer
)
from .utils import get_object_or_404_api
from mysite.apps.historias.models import ordenesProducto as OrdenProducto, orden as Orden
from mysite.apps.historias.serializers import OrdenSerializer
from mysite.apps.parametros.models import servicios as Servicio
from mysite.apps.parametros.serializers import ServicioSerializer


@api_view(['GET', 'POST'])
def lista_laboratorio(request):
    """
    Lista los laboratorios en formato json.
    """
    args = tuple()
    kwargs = dict()

    if request.method == 'GET':
        laboratorios = Laboratorio.objects.all()
        serializer = LaboratorioSerializer(laboratorios, many=True)
        args = (serializer.data, )

    elif request.method == 'POST':
        serializer = LaboratorioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            args = (serializer.data, )
            kwargs['status'] = status.HTTP_201_CREATED
        else:
            args = (serializer.errors, )
            kwargs['status'] = status.HTTP_400_BAD_REQUEST
    return Response(*args, **kwargs)


# @csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
# @authentication_classes((SessionAuthentication, BasicAuthentication))
def detalle_laboratorio(request, pk):
    """
    CRUD para los laboratorios.
    """

    args = tuple()
    kwargs = dict()

    laboratorio = get_object_or_404_api(Laboratorio, pk=pk)

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


class ReactivosListAPI(generics.ListCreateAPIView):
    queryset = Reactivo.objects.all()
    serializer_class = ReactivoSerializer


class ReactivoDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reactivo.objects.all()
    serializer_class = ReactivoSerializer


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


@api_view(['GET'])
def ordenes_laboratorios(request):
    """
    Lista las ordenes que tengan laboratorios.
    """

    args = tuple()
    kwargs = dict()

    if request.method == 'GET':
        # bacteriologo = request.user.bacteriologo
        servicios = Laboratorio.objects.all().values_list('servicio_id', flat=True)

        ordenes = Orden.objects.filter(
            id__in=OrdenProducto.objects.filter(
                servicio__in=servicios
            ).values_list('orden_id', flat=True).distinct()
        )
        serializer = OrdenSerializer(ordenes, many=True)
        args = (serializer.data, )

    return Response(*args, **kwargs)
