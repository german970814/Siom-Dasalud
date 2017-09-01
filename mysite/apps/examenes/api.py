# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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
    Visiometria, Empleado, Audiometria
)
from .serializers import (
    VisiometriaSerializer, EmpleadoSerializer, AudiometriaSerializer
)
from mysite.apps.historias.models import ordenesProducto as OrdenProducto, orden as Orden
from mysite.apps.historias.serializers import OrdenVisiometriaSerializer, OrdenAudiometriaSerializer
from mysite.apps.parametros.models import servicios as Servicio
from mysite.apps.laboratorios.utils import Pagination
# from mysite.apps.parametros.serializers import ServicioSerializer

import datetime
# import reversion


class OrdenesSinVisiometriaListAPI(generics.ListAPIView):
    queryset = Orden.objects.all()
    serializer_class = OrdenVisiometriaSerializer
    pagination_class = Pagination

    def get_queryset(self, *args, **kwargs):
        # Visiometria.objects.all()
        hoy = timezone.now().date()

        queryset = super(OrdenesSinVisiometriaListAPI, self).get_queryset(*args, **kwargs)
        queryset = queryset.filter(
            id__in=OrdenProducto.objects.filter(
                servicio__nombre=Visiometria.get_visiometria_servicio()
            ).values_list('orden_id', flat=True).distinct(),
            fecha__range=(hoy - datetime.timedelta(days=32), hoy + datetime.timedelta(days=1))
        ).order_by('-fecha')  # .exclude(visiometria__estado=Visiometria.RESULTADO_EMITIDO)

        return queryset


class VisiometriaListAPI(generics.ListCreateAPIView):
    queryset = Visiometria.objects.all()
    serializer_class = VisiometriaSerializer
    pagination_class = Pagination

    def get_queryset(self, *args, **kwargs):
        hoy = timezone.now().date()
        # queryset = super(VisiometriaListAPI, self).get_queryset(*args, **kwargs)
        queryset = self.request.user.empleado_examenes.visiometrias.all()
        queryset = queryset.filter(
            orden__fecha__range=(hoy - datetime.timedelta(days=32), hoy + datetime.timedelta(days=1))
        ).order_by('-orden__fecha')
        return queryset

    def perform_create(self, serializer):
        serializer.save(visiometra=self.request.user.empleado_examenes, estado=Visiometria.PENDIENTE)


class VisiometriaRetrieveUpdateAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Visiometria.objects.all()
    serializer_class = VisiometriaSerializer


class EmpleadoListAPI(generics.ListCreateAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer


class EmpleadoRetrieveUpdateAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer


@api_view(['PUT'])
def cambiar_firma_visiometra(request, pk):
    """Vista para cambiar la firma del visiometra."""

    visiometra = get_object_or_404(Empleado, pk=pk)

    # kwargs_serializer = {'fields': ('firma', )}
    request.data.setdefault('id', pk)
    serializer = EmpleadoSerializer(fields=('firma', ), data=request.data, instance=visiometra)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


class OrdenesSinAudiometriaListAPI(generics.ListAPIView):
    queryset = Orden.objects.all()
    serializer_class = OrdenAudiometriaSerializer
    pagination_class = Pagination

    def get_queryset(self, *args, **kwargs):
        hoy = timezone.now().date()

        queryset = super(OrdenesSinAudiometriaListAPI, self).get_queryset(*args, **kwargs)
        queryset = queryset.filter(
            id__in=OrdenProducto.objects.filter(
                servicio__nombre=Audiometria.get_audiometria_servicio()
            ).values_list('orden_id', flat=True).distinct(),
            fecha__range=(hoy - datetime.timedelta(days=32), hoy + datetime.timedelta(days=1))
        ).order_by('-fecha')  # .exclude(visiometria__estado=Visiometria.RESULTADO_EMITIDO)

        return queryset


class AudiometriaListAPI(generics.ListCreateAPIView):
    queryset = Audiometria.objects.all()
    serializer_class = AudiometriaSerializer
    pagination_class = Pagination

    def get_queryset(self, *args, **kwargs):
        hoy = timezone.now().date()
        queryset = self.request.user.empleado_examenes.audiometrias.all()
        queryset = queryset.filter(
            orden__fecha__range=(hoy - datetime.timedelta(days=32), hoy + datetime.timedelta(days=1))
        ).order_by('-orden__fecha')
        return queryset

    def perform_create(self, serializer):
        serializer.save(audiometra=self.request.user.empleado_examenes, estado=Audiometria.PENDIENTE)


class AudiometriaRetrieveUpdateAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Audiometria.objects.all()
    serializer_class = AudiometriaSerializer
