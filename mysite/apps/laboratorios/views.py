# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils import timezone
# from django.utils.six import BytesIO
from django.core.files import File
from django.template import RequestContext
from django.template.loader import render_to_string
from django.conf import settings

from weasyprint import HTML

from .models import Laboratorio, Resultado, Recepcion, Formato
from mysite.apps.historias.models import orden as Orden, ordenesProducto as OrdenProducto

import datetime
import json
import io


@login_required
def index(request):
    return render(request, 'laboratorios/index.html', {})


@login_required
def ver_resultado_laboratorio(request, pk):
    """
    Vista para ver los resultados de los examenes de laboratorios, de manera individual o coletiva,
    permite visualizar el resultado como HTML o PDF.
    """
    orden = get_object_or_404(Orden, pk=pk)
    resultados = orden.resultados_laboratorio.all().order_by('laboratorio__seccion_trabajo', 'bacteriologo')

    _verified_formats = ['html', 'pdf']
    _verified_modes = ['inline', 'attachment']
    _mode = request.GET.get('inline', 'attachment')
    _laboratorio = request.GET.get('laboratorio', None)
    spec = request.GET.get('format', 'html').lower()

    if spec not in _verified_formats or _mode not in _verified_modes:
        from django.http import HttpResponseNotAllowed
        return HttpResponseNotAllowed('Spect or format not allowed for: {}'.format(spec))

    if _laboratorio is not None:
        laboratorio = get_object_or_404(Resultado, pk=_laboratorio)
        if laboratorio.archivo and spec == 'pdf':
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = '%s; filename=lab-%d.pdf' % (_mode, orden.id)
            with open(laboratorio.archivo.file.file.name, 'rb') as f:
                for line in f.readlines():
                    response.write(line)
            return response
        else:
            resultados = Resultado.objects.filter(id=laboratorio.id).order_by('laboratorio__seccion_trabajo', 'bacteriologo')


    for resultado in resultados:
        resultado.resultado = json.loads(resultado.resultado)

    data = {'resultados': resultados, 'orden': orden, 'request': request}
    # weasyprint
    if spec == 'pdf':
        to_html = render_to_string('laboratorios/prueba.html', data, RequestContext(request))
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = '%s; filename=lab-%d.pdf' % (_mode, orden.id)
        HTML(string=to_html).write_pdf(
            response, stylesheets=['static/css/bootstrap.min.css', 'static/css/print_laboratorios.css'])
        return response

    return render(request, 'laboratorios/prueba.html', data)


@login_required
def imprimir_laboratorio(request, pk):
    """
    Vista para generar e imprimir resultado de laboratorios, esta funcion es capaz
    de generar cada resultado de laboratorio de acuerdo a una orden, y tambien es
    capaz de enviar un resultado generico.
    """

    orden = get_object_or_404(Orden, pk=pk)
    _print = request.GET.get('print', None)
    mode = request.GET.get('inline', 'attachment')
    resultados = orden.resultados_laboratorio.all().order_by('laboratorio__seccion_trabajo', 'bacteriologo')

    stylesheets = ['static/css/bootstrap.min.css', 'static/css/print_laboratorios.css']

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = '%s; filename=lab-%d.pdf' % (mode, orden.id)

    for resultado in resultados:
        resultado._resultado = resultado.resultado

        if resultado.cerrado and not resultado.archivo:
            with io.BytesIO() as _buffer:
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
        resultados = Resultado.objects.filter(
            id=laboratorio.id).order_by('laboratorio__seccion_trabajo', 'bacteriologo')
        for resultado in resultados:
            resultado.resultado = json.loads(resultado.resultado)
    else:
        if _print is not None and orden.recepcion.estado != Recepcion.RESULTADO_EMITIDO:
            recepcion = orden.recepcion
            recepcion.estado = Recepcion.RESULTADO_EMITIDO
            recepcion.save()

    to_html = render_to_string(
        'laboratorios/resultados.html',
        {'resultados': resultados, 'orden': orden, 'request': request},
        RequestContext(request)
    )
    HTML(string=to_html).write_pdf(response, stylesheets=stylesheets)

    return response


@login_required
def preview(request, pk):
    """
    Vista para previsualizar los resultados de los laboratorios de manera que se puedan ver aún los
    resultados de los laboratorios que no han sido digitados.
    """

    orden = get_object_or_404(Orden, pk=pk)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename=lab-%d.pdf' % orden.id

    resultados = orden.resultados_laboratorio.all().order_by('laboratorio__seccion_trabajo', 'bacteriologo')

    laboratorios = Laboratorio.objects.filter(
        id__in=Orden.objects.filter(id=orden.id).servicios().values_list('laboratorio__id', flat=True)
    ).exclude(
        id__in=resultados.values_list('laboratorio__id', flat=True)
    )
    formatos = Formato.objects.filter(id__in=laboratorios.values_list('formato__id', flat=True))

    resultados = list(resultados)
    for formato in formatos:
        resultados.append(
            Resultado(orden=orden, laboratorio=formato.laboratorio, resultado=formato.formato)
        )
    for resultado in resultados:
        resultado.resultado = json.loads(resultado.resultado)

    stylesheets = ['static/css/bootstrap.min.css', 'static/css/print_laboratorios.css']

    to_html = render_to_string(
        'laboratorios/resultados.html',
        {'resultados': resultados, 'orden': orden, 'request': request},
        RequestContext(request)
    )
    HTML(string=to_html).write_pdf(response, stylesheets=stylesheets)
    return response
