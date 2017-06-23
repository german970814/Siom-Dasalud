# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from rest_framework import permissions


class AdminPermission(permissions.BasePermission):
    message = _('Usuario no tiene permisos de administrador')

    def has_permission(self, request, view):
        if request.user.is_authenticated():
            return request.user.has_perm('home.es_administrador') or request.user.is_superuser or request.user.is_staff
        return False


class BacteriologoPermission(permissions.BasePermission):
    message = _('Usuario no es bacteriologo')

    def has_permission(self, request, view):
        if request.user.is_authenticated():
            bacteriologo = getattr(request.user, 'bacteriologo', None)
            return bacteriologo is not None and bool(bacteriologo)
        return False


class AdminOrBacteriologoPermission(permissions.BasePermission):
    message = _('No tienes permisos de realizar acciones')

    def has_permission(self, request, view):
        admin_permissions = AdminPermission().has_permission(request, view)
        if request.method in permissions.SAFE_METHODS:
            if admin_permissions:
                return True
            return BacteriologoPermission().has_permission(request, view)
        return admin_permissions


class ReadOnlyPermission(permissions.BasePermission):
    message = _('No tienes permisos de realizar acciones')

    def has_permission(self, request, view):
        if request.user.is_authenticated():
            if request.method in permissions.SAFE_METHODS:
                return True
            return AdminPermission().has_permission(request, view)
        return False
