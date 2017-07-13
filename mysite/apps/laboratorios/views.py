# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils import timezone
from django.utils.six import BytesIO
from django.core.files import File
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


def ver_resultado_laboratorio(request, pk):
    orden = get_object_or_404(Orden, pk=pk)
    resultados = orden.resultados_laboratorio.all()

    _verified_formats = ['html', 'pdf']

    _laboratorio = request.GET.get('laboratorio', None)
    spec = request.GET.get('format', 'html').lower()

    if spec not in _verified_formats:
        from django.http import HttpResponseNotAllowed
        return HttpResponseNotAllowed('Spect or format not allowed for: {}'.format(spec))

    if _laboratorio is not None:
        laboratorio = get_object_or_404(Resultado, pk=_laboratorio)
        if laboratorio.archivo and spec == 'pdf':
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=lab-%d' % orden.id
            with open(laboratorio.archivo.file.file.name, 'rb') as f:
                for line in f.readlines():
                    response.write(line)
            return response
        else:
            resultados = Resultado.objects.filter(id=laboratorio.id)


    for resultado in resultados:
        resultado.resultado = json.loads(resultado.resultado)

    # weasyprint
    if spec == 'pdf':
        to_html = render_to_string('laboratorios/prueba.html', {'resultados': resultados, 'orden': orden, 'request': request}, RequestContext(request))
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=lab-%d' % orden.id
        HTML(string=to_html).write_pdf(
            response, stylesheets=['static/css/bootstrap.min.css', 'static/css/print_laboratorios.css'])
        return response

    return render(request, 'laboratorios/prueba.html', {'resultados': resultados, 'orden': orden, 'request': request})


@login_required
def imprimir_laboratorio(request, pk):
    """
    Vista para generar e imprimir resultado de laboratorios, esta funcion es capaz
    de generar cada resultado de laboratorio de acuerdo a una orden, y tambien es
    capaz de enviar un resultado generico.
    """

    orden = get_object_or_404(Orden, pk=pk)
    _print = request.GET.get('print', None)
    resultados = orden.resultados_laboratorio.all()

    stylesheets = ['static/css/bootstrap.min.css', 'static/css/print_laboratorios.css']

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=lab-%d' % orden.id

    for resultado in resultados:
        resultado._resultado = resultado.resultado

        if resultado.cerrado and not resultado.archivo:
            with BytesIO() as _buffer:
            # _buffer = io.BytesIO()
                _resultados = Resultado.objects.filter(id=resultado.id)
                for result_object in _resultados:
                    result_object.resultado = json.loads(resultado.resultado)
                _buffer = File(_buffer)
                _to_html = render_to_string(
                    'laboratorios/resultados.html',
                    {'resultados': _resultados, 'orden': orden, 'request': request},
                    RequestContext(request)
                )
                HTML(string=_to_html).write_pdf(_buffer, stylesheets=stylesheets)
                resultado.archivo.save('resultado{}.pdf'.format(resultado.id), _buffer)
                resultado.resultado = resultado._resultado
                resultado.save(update_fields=['archivo'])

        resultado.resultado = json.loads(resultado.resultado)

    if 'laboratorio' in request.GET:
        laboratorio = get_object_or_404(Resultado, pk=request.GET.get('laboratorio'))

        if laboratorio.archivo:
            with open(laboratorio.archivo.file.file.name, 'rb') as f:
                for line in f.readlines():
                    response.write(line)
            return response
        resultados = Resultado.objects.filter(id=laboratorio.id)

    else:
        if _print is not None and orden.recepcion.estado != Recepcion.RESULTADO_EMITIDO:
            recepcion = orden.recepcion
            recepcion.estado = Recepcion.RESULTADO_EMITIDO
            recepcion.save()

    # if 'imprimir' in request.POST:
    # ruta = settings.STATIC_ROOT + '/%s'
    to_html = render_to_string(
        'laboratorios/resultados.html',
        {'resultados': resultados, 'orden': orden, 'request': request},
        RequestContext(request)
    )
    HTML(string=to_html).write_pdf(response, stylesheets=stylesheets)

    return response
