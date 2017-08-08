# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from rest_framework import permissions


class VisiometraPermission(permissions.BasePermission):
    message = _('Usuario no tiene permisos de visiometra')

    def has_permission(self, request, view):
        if request.user.is_authenticated():
            visiometra = getattr(request.user, 'visiometra', None)
            return visiometra is not None and bool(visiometra)
        return False
