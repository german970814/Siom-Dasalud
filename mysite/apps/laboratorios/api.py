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

from .models import Laboratorio, Equipo, SeccionTrabajo
from .serializers import LaboratorioSerializer, EquipoSerializer, SeccionTrabajoSerializer
from .utils import get_object_or_404_api


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


class SeccionesTrabajoListAPI(generics.ListCreateAPIView):
    queryset = SeccionTrabajo.objects.all()
    serializer_class = SeccionTrabajoSerializer


# class DetalleCodigoPuntoView(RetrieveAPIView):
#     """Devuelve la información del un punto de recolección de muestras de agua en formato JSON según el id del codigo
#     del punto."""

#     queryset = CodigoPunto.objects.all()
#     serializer_class = CodigoPuntoSerializer
#     permission_classes = [permissions.IsAuthenticated]

