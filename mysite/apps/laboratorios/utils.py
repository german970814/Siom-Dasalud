from rest_framework.response import Response
from rest_framework import status


def get_object_or_404_api(ModelOrQuery, **kwargs):
    try:
        return getattr(ModelOrQuery, 'objects', ModelOrQuery).get(**kwargs)
    except Exception:
        return Response(status=status.HTTP_404_NOT_FOUND)
