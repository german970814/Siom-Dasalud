# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.db import transaction
# from django.utils import timezone
# from django.utils.six import BytesIO
# from django.core.files import File
from django.template import RequestContext
from django.template.loader import render_to_string
# from django.conf import settings

from weasyprint import HTML

from . import models, forms
from mysite.apps.historias.models import orden as Orden

# import datetime
# import json


@login_required
def visiometria_create(request, pk):
    """Vista para crear visiometrías y optometrías"""

    orden = get_object_or_404(Orden, pk=pk)

    tipo = models.Visiometria.get_tipo_by_servicio(orden)

    if getattr(orden, 'visiometria', None) is not None:
        instance = orden.visiometria
        form_kwargs = {'instance': instance}
    else:
        form_kwargs = {}

    if request.method == 'POST':
        form_kwargs['data'] = request.POST
        form = forms.VisiometriaForm(**form_kwargs)

        if form.is_valid():
            visiometria = form.save(commit=False)
            visiometria.orden = orden
            visiometria.tipo = tipo
            visiometria.estado = models.Visiometria.PENDIENTE
            visiometria.save()
            return redirect('/pacientes/page/1/')
        else:
            messages.error(request, _('Escoja un Visiometra'))
    else:
        form = forms.VisiometriaForm(**form_kwargs)

    data = {
        'form': form,
        'orden': orden
    }
    return render(request, 'examenes/visiometria.html', data)


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


@login_required
def ver_resultado_examenes(request, pk):
    """"""

    RESPONSE_MODES = ('inline', 'attachment', )
    RESPONSE_FORMATS = ('pdf', 'html', )
    ACEPTED_EXAMENS = ('visiometria', 'audiometria', )
    EXAMEN_MODEL_DIR = {
        'visiometria': models.Visiometria,
        'audiometria': models.Audiometria
    }

    _response_mode = request.GET.get('inline', 'attachment')
    _response_format = request.GET.get('format', 'html')

    if _response_mode not in RESPONSE_MODES:
        _response_mode = RESPONSE_MODES[1]
    if _response_format not in RESPONSE_FORMATS:
        _response_format = RESPONSE_FORMATS[1]

    orden = get_object_or_404(Orden, pk=pk)

    _examen = request.GET.get('examen', '')

    if _examen not in ACEPTED_EXAMENS:
        from django.http import HttpResponseNotAllowed
        return HttpResponseNotAllowed('Examén no encontrado')

    examen = get_object_or_404(EXAMEN_MODEL_DIR[_examen].objects.all(), orden=orden)

    data = {
        'orden': orden, 'examen': examen, 'request': request, 'tipo': _examen
    }

    if _response_format == 'pdf':
        stylesheets = ['static/css/bootstrap.min.css', 'static/css/print_examenes.css']
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = '%s; filename=examen-%d.pdf' % (_response_mode, orden.id,)
        _string = render_to_string(
            'examenes/resultado_base.html', data, RequestContext(request)
        )
        HTML(string=_string).write_pdf(response, stylesheets=stylesheets)
        return response

    return render(request, 'examenes/resultado_base.html', data)


@login_required
def asignar_especialista_examen(request, pk):
    """Vista para crear audiometrías"""

    orden = get_object_or_404(Orden, pk=pk)
    form_visiometra_kwargs = {}
    form_audiometra_kwargs = {}
    tipo = None

    visiometria = request.GET.get('visiometria', False)
    audiometria = request.GET.get('audiometria', False)

    if getattr(orden, 'audiometria', None) is not None:
        form_audiometra_kwargs['instance'] = orden.audiometria
    if getattr(orden, 'visiometria', None) is not None:
        form_visiometra_kwargs['instance'] = orden.visiometria

    _forms = {}
    if audiometria:
        _forms[forms.AudiometriaForm] = form_audiometra_kwargs
    if visiometria:
        _forms[forms.VisiometriaForm] = form_visiometra_kwargs
        tipo = models.Visiometria.get_tipo_by_servicio(orden)

    if request.method == 'POST':
        for Form in _forms:
            _forms[Form]['data'] = request.POST

        _forms = [Form(**_forms[Form]) for Form in _forms]

        if all([form.is_valid() for form in _forms]):
            with transaction.atomic():
                for form in _forms:
                    instance = form.save(commit=False)
                    instance.estado = form.Meta.model.PENDIENTE
                    instance.orden = orden
                    instance.tipo = tipo
                    instance.save()
            return redirect('/pacientes/page/1/')
        else:
            messages.error(request, _('Escoja un especialista'))
    else:
        _forms = [Form(**_forms[Form]) for Form in _forms]

    def get(value, where):
        first = list(filter(lambda x: x.__class__ == value, where))
        if first:
            return first[0]
        return None

    data = {
        'form_visiometra': get(forms.VisiometriaForm, _forms),
        'form_audiometra': get(forms.AudiometriaForm, _forms),
        'audiometria': audiometria, 'visiometria': visiometria,
        'orden': orden
    }
    return render(request, 'examenes/asignar_especialista.html', data)
