from rest_framework.response import Response
from rest_framework import status


def get_object_or_404_api(ModelOrQuery, **kwargs):
    """
    Funcion para obtener los objetos o arrojar un 404 si no los encuentras
    en formato json para api.
    """
    try:
        return getattr(ModelOrQuery, 'objects', ModelOrQuery).get(**kwargs)
    except Exception:
        return Response(status=status.HTTP_404_NOT_FOUND)


class DictToObject(dict):
    """
    Clase para poder usar los diccionarios como si fueran objetos nativos de python
    tal como lo hace javascript con sus objetos.
    """

    VOID = '__VOID__'

    def __getattr__(self, attr):
        data = self.get(attr, self.VOID)
        if data == self.VOID:
            return super(DictToObject, self).__getattr__(attr)
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
