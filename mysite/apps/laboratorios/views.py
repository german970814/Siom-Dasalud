# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils import timezone
from django.template import RequestContext
from django.template.loader import render_to_string
from django.conf import settings

from weasyprint import HTML

from .models import Laboratorio, Resultado, Recepcion
from mysite.apps.historias.models import orden as Orden, ordenesProducto as OrdenProducto

import datetime
import json


@login_required
def index(request):
    return render(request, 'laboratorios/index.html', {})


@login_required
def ordenes_toma_muestra(request):
    """
    Vista para ver las ordenes con el usuario de toma de muestra
    """
    data = {}

    if request.method == 'POST':
        pass
    else:
        hoy = timezone.now().date()
        servicios = Laboratorio.objects.all().values_list('servicio_id', flat=True)

        ordenes = Orden.objects.filter(  # actuelmente solo se traen los ultimos 8 días.
            id__in=OrdenProducto.objects.filter(
                servicio__nombre__id__in=servicios
            ).values_list('orden_id', flat=True).distinct(),
            fecha__range=(hoy - datetime.timedelta(days=8), hoy)
        ).order_by('-fecha')  # .select_related('paciente')
        data['ordenes'] = ordenes

    return render(request, 'laboratorios/toma_muestra.html', data)


def prueba(request, pk):
    orden = get_object_or_404(Orden, pk=pk)
    resultados = orden.resultados_laboratorio.all()

    for resultado in resultados:
        resultado.resultado = json.loads(resultado.resultado)

    return render(request, 'laboratorios/prueba.html', {'resultados': resultados, 'orden': orden})


@login_required
def imprimir_laboratorio(request, pk):

    orden = get_object_or_404(Orden, pk=pk)
    resultados = orden.resultados_laboratorio.all()
    _print = request.GET.get('print', None)

    if 'laboratorio' in request.GET:
        laboratorio = get_object_or_404(Resultado, pk=request.GET.get('laboratorio'))
        resultados = Resultado.objects.filter(id=laboratorio.id)
    else:
        if _print is not None and orden.recepcion.estado != Recepcion.RESULTADO_EMITIDO:
            recepcion = orden.recepcion
            recepcion.estado = Recepcion.RESULTADO_EMITIDO
            recepcion.save()

    for resultado in resultados:
        resultado.resultado = json.loads(resultado.resultado)
    # if 'imprimir' in request.POST:
    ruta = settings.STATIC_ROOT + '/%s'
    to_html = render_to_string('laboratorios/resultados.html', {'resultados': resultados, 'orden': orden}, RequestContext(request))
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=lab-%d' % orden.id
    HTML(string=to_html).write_pdf(
        response, stylesheets=['static/css/bootstrap.min.css', 'static/css/print_laboratorios.css'])

    def alerta(resultado):
        if resultado.tipo.name == 'number':
            result = resultado.model_text
            return '*' if result <= resultado.referencia_minima[paciente.genero.upper()] or \
                result >= resultado.referencia_maxima[paciente.genero.upper()] else ''
        return ''

    return response
