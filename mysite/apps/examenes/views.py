# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# from django.utils import timezone
# from django.utils.six import BytesIO
# from django.core.files import File
from django.template import RequestContext
from django.template.loader import render_to_string
# from django.conf import settings

from weasyprint import HTML

# from .models import Laboratorio, Resultado, Recepcion
from mysite.apps.historias.models import orden as Orden

# import datetime
# import json


@login_required
def index(request):
    return render(request, 'examenes/index.html', {})


@login_required
def ver_resultado_visiometria(request, pk):
    """
    Vista para ver el resultado de una visiometria
    """

    RESPONSE_MODES = ('inline', 'attachment', )
    RESPONSE_FORMATS = ('pdf', 'html', )

    _response_mode = request.GET.get('inline', 'attachment')
    _response_format = request.GET.get('format', 'html')

    if _response_mode not in RESPONSE_MODES:
        _response_mode = RESPONSE_MODES[1]
    if _response_format not in RESPONSE_FORMATS:
        _response_format = RESPONSE_FORMATS[1]

    orden = get_object_or_404(Orden, pk=pk)
    visiometria = orden.visiometria

    data = {'orden': orden, 'visiometria': visiometria, 'request': request}

    if _response_format == 'pdf':
        stylesheets = ['static/css/bootstrap.min.css', 'static/css/print_examenes.css']
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = '%s; filename=visiometria-%d.pdf' % (_response_mode, orden.id,)
        _string = render_to_string(
            'examenes/resultado_base.html', data, RequestContext(request)
        )
        HTML(string=_string).write_pdf(response, stylesheets=stylesheets)
        return response

    return render(request, 'examenes/resultado_base.html', data)
