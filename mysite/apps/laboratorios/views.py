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
    return render(request, 'laboratorios/resultados.html', {})
