# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# @login_required
def index(request):
    return render(request, 'laboratorios/index.html', {})


def prueba_impresion(request):
    # if 'imprimir' in request.POST:
    #     ruta = "static/css/%s.css"
    #     to_html = render_to_string('trazabilidad/reporte.html', data, RequestContext(request))
    #     http_response = HttpResponse(content_type='application/pdf')
    #     http_response['Content-Disposition'] = 'attachment; filename=report-by'
    #     _informes = '_informe_nuevo_grande'
    #     HTML(string=to_html).write_pdf(http_response, stylesheets=[ruta % 'estilos', ruta % 'bootstrap.min', ruta % _informes])
    #     return http_response
    def alerta(resultado):
        if resultado.tipo.name == 'number':
            result = resultado.model_text
            return '*' if result <= resultado.referencia_minima[paciente.genero.upper()] or \
                result >= resultado.referencia_maxima[paciente.genero.upper()] else ''
        return ''

    modelo = {
        'nombre': '',
        'help': '',
        'choices': [{'edit': False, 'name': 'Option 1', id: 0}],
        'choices_select': [],
        'choices_count': 0,
        'model_text': '',
        'model_check': [],
        'unidades': '',
        'tipo': '',
        'genero': {
            'M': {
                'referencia_minima': '',
                'referencia_maxima': '',
            },
            'F': {
                'referencia_minima': '',
                'referencia_maxima': '',
            },
        }
    }
    resultado = [
        {
            'nombre': 'Glicemia',
            'help': 'Esto es para probar',
            'choices': [{'edit': False, 'name': 'Option 1', 'id': 0}],
            'choices_select': [],
            'choices_count': 0,
            'model_text': '142',
            'model_check': [],
            'unidades': 'md/dl',
            'tipo': {
                'text': 'Texto',
                'name': 'text',
                'help': 'Con este campo se puede dar un resultado libre corto y conciso.'
            },
            'genero': {
                'M': {
                    'referencia_minima': '127',
                    'referencia_maxima': '412',
                },
                'F': {
                    'referencia_minima': '504',
                    'referencia_maxima': '852',
                },
            }
        },
        {
            'nombre': 'Croprológico',
            'help': 'Hola como estas',
            'choices': [{'edit': False, 'name': 'Option 1', 'id': 0}],
            'choices_select': [],
            'choices_count': 0,
            'model_text': '159',
            'model_check': [],
            'unidades': 'mg/dl',
            'tipo': {
                'text': 'Texto',
                'name': 'text',
                'help': 'Con este campo se puede dar un resultado libre corto y conciso.'
            },
            'genero': {
                'M': {
                    'referencia_minima': '50',
                    'referencia_maxima': '205',
                },
                'F': {
                    'referencia_minima': '20',
                    'referencia_maxima': '108',
                },
            }
        },
        {
            'nombre': 'Hematocritos',
            'help': 'Hola como estas',
            'choices': [{'edit': False, 'name': 'Option 1', 'id': 0}],
            'choices_select': [],
            'choices_count': 0,
            'model_text': '159',
            'model_check': [],
            'unidades': 'mg/dl',
            'tipo': {
                'text': 'title',
                'name': 'title',
                'help': 'Con este campo se puede dar un resultado libre corto y conciso.'
            },
            'genero': {
                'M': {
                    'referencia_minima': '50',
                    'referencia_maxima': '205',
                },
                'F': {
                    'referencia_minima': '20',
                    'referencia_maxima': '108',
                },
            }
        },
        {
            'nombre': 'Pefil Lipídico',
            'help': 'Hola como estas',
            'choices': [{'edit': False, 'name': 'Option 1', 'id': 0}],
            'choices_select': [],
            'choices_count': 0,
            'model_text': '159',
            'model_check': [],
            'unidades': 'mg/dl',
            'tipo': {
                'text': 'Texto',
                'name': 'text',
                'help': 'Con este campo se puede dar un resultado libre corto y conciso.'
            },
            'genero': {
                'M': {
                    'referencia_minima': '50',
                    'referencia_maxima': '205',
                },
                'F': {
                    'referencia_minima': '20',
                    'referencia_maxima': '108',
                },
            }
        },
    ]
    return render(request, 'laboratorios/resultados.html', {'resultados': resultado})
