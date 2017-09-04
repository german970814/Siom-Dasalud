from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from django.db.models import Q


def get_object_or_404_api(ModelOrQuery, **kwargs):  # deprecate
    """
    Funcion para obtener los objetos o arrojar un 404 si no los encuentras
    en formato json para api.
    """
    try:
        return getattr(ModelOrQuery, 'objects', ModelOrQuery).get(**kwargs)
    except Exception:
        raise Response(status=status.HTTP_404_NOT_FOUND)


def get_hemogramas_from_queryset(queryset):
    """
    Funcion que recibe un queryset de resultados y retorna los resultados con
    hemogramas.
    """

    # return list(
    #     filter(lambda resultado: resultado.laboratorio.nombre.lower().startswith('hemograma'),
    #     resultados)
    # )

    hemogramas = queryset.filter(
        laboratorio__nombre__icontains='hemograma'
    )

    if hemogramas.exists():
        hemogramas |= queryset.filter(
            ~Q(id__in=hemogramas.values_list('id', flat=True)),
            laboratorio__seccion_trabajo=hemogramas.first().laboratorio.seccion_trabajo
        )

    resultados = queryset.filter(~Q(id__in=hemogramas.values_list('id', flat=True)))

    return hemogramas, resultados


class Pagination(PageNumberPagination):
    page_size = 10


class ListViewAPIMixin(object):
    """
    Mixin para los ListViewAPI
    """

    search_params = []
    # pagination_class = Pagination

    def get_queryset(self, *args, **kwargs):
        queryset = super(ListViewAPIMixin, self).get_queryset(*args, **kwargs)
        if 'param' in self.request.GET:
            q_set = Q()
            for param in self.search_params:
                q_set |= Q(**{param + '__icontains': self.request.GET.get('param')})
            queryset = queryset.filter(q_set)
        return queryset


class DictToObject(dict):
    """
    Clase para poder usar los diccionarios como si fueran objetos nativos de python
    tal como lo hace javascript con sus objetos.
    """

    VOID = '__VOID__'

    def __getattr__(self, attr):
        data = self.get(attr, self.VOID)
        if data == self.VOID:
            raise TypeError('atributo "{}" no encontrado en "{}"'.format(attr, self))
        if isinstance(data, dict):
            try:
                return DictToObject(data)
            except TypeError:
                pass
        return data

    def __hasattr__(self, attr):
        return attr in self

    def __setattr__(self, attr, value):
        self[attr] = value
