# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.six import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.forms.utils import flatatt
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

from mysite.apps.historias.models import orden as Orden
from mysite.apps.parametros.models import servicios as Servicio


def ruta_imagen_bacteriologo(self, filename):
    return 'bacteriologos/{}'.format(filename)


@python_2_unicode_compatible
class SeccionTrabajo(models.Model):
    """Modelo para guardar las areas o secciones de trabajo."""

    codigo = models.CharField(max_length=50, verbose_name=_('Código'))
    descripcion = models.TextField(verbose_name=_('Descripción'))

    __str__ = lambda self: self.descripcion.upper()

    class Meta:
        verbose_name = _('Sección de Trabajo')
        verbose_name_plural = _('Secciones de Trabajo')


@python_2_unicode_compatible
class Tecnica(models.Model):
    """
    Modelo para guardar las tecnicas usadas por los equipos.
    """

    codigo = models.CharField(max_length=50, verbose_name=_('Código'))
    nombre = models.CharField(max_length=255, verbose_name=_('Nombre'))

    __str__ = lambda self: '{self.nombre} ({self.codigo})'.format(self=self).upper()


@python_2_unicode_compatible
class Equipo(models.Model):
    """
    Modelo para guardar los equipos que son usados en los laboratorios.
    """

    codigo = models.CharField(max_length=50, verbose_name=_('Código'))
    nombre = models.CharField(max_length=255, verbose_name=_('Nombre'))
    tecnica = models.ForeignKey(Tecnica, verbose_name=_('Tecnica'), related_name='equipos')

    __str__ = lambda self: '{self.nombre} ({self.codigo})'.format(self=self).upper()


@python_2_unicode_compatible
class Laboratorio(models.Model):
    """
    Modelo para guardar los laboratorios o pruebas en el sistema.
    """

    codigo = models.CharField(max_length=50, verbose_name=_('Código'))
    nombre = models.CharField(max_length=255, verbose_name=_('Nombre'))
    codigo_internacional = models.CharField(max_length=50, verbose_name=_('Código Internacional'), blank=True, null=True)
    equipo = models.ForeignKey(Equipo, verbose_name=_('Equipo'), related_name='laboratorios')
    seccion_trabajo = models.ForeignKey(SeccionTrabajo, verbose_name=_('Seccion de Trabajo'), related_name=('laboratorios'))
    servicio = models.OneToOneField(Servicio, related_name='laboratorio')

    __str__ = lambda self: '{self.nombre} ({self.codigo})'.format(self=self).upper()


@python_2_unicode_compatible
class Reactivo(models.Model):
    """
    Modelo para guardar los reactivos de cada laboratorio.
    """

    codigo = models.CharField(max_length=50, verbose_name=_('Código'))
    nombre = models.CharField(max_length=255, verbose_name=_('Nombre'))
    laboratorio = models.ForeignKey(Laboratorio, verbose_name=_('Laboratorio'), related_name='reactivos')
    alarma_inferior = models.IntegerField(verbose_name=_('Alarma inferior'), blank=True, null=True)
    alarma_media = models.IntegerField(verbose_name=_('Alarma media'), blank=True, null=True)
    costos = models.IntegerField(verbose_name=_('Costo'))

    __str__ = lambda self: '{self.nombre} ({self.codigo})'.format(self=self)


@python_2_unicode_compatible
class Recarga(models.Model):
    """
    Modelo para contar el historial de las recargas que se hacen a un reactivo.
    """

    reactivo = models.ForeignKey(Reactivo, verbose_name=_('Reactivo'), related_name='recargas')
    cantidad = models.IntegerField(verbose_name=_('Cantidad'))
    fecha = models.DateField(auto_now_add=True)

    __str__ = lambda self: '{self.reactivo}: Recarga de {self.cantidad}'.format(self=self)


@python_2_unicode_compatible
class BancoReactivo(models.Model):
    """
    Modelo de banco de reactivos, para llevar el inventariado de cada reactivo.
    """

    reactivo = models.OneToOneField(Reactivo, verbose_name=_('Reactivo'), related_name='banco_reactivo')
    cantidad = models.IntegerField(verbose_name=_('Cantidad'))

    __str__ = lambda self: '{self.reactivo}: {self.cantidad}'.format(self=self)


@python_2_unicode_compatible
class Caracteristica(models.Model):
    """
    Modelo de las caracteristicas.
    """

    codigo = models.CharField(max_length=50, verbose_name=('Código'))
    descripcion = models.TextField(verbose_name=('Descripción'))

    __str__ = lambda self: self.codigo


@python_2_unicode_compatible
class EspecificacionCaracteristica(models.Model):
    """
    Modelo para guardar las especificaciones de una caracteristica.
    """

    nombre = models.CharField(max_length=255, verbose_name=('Nombre'))
    caracteristica = models.ForeignKey(Caracteristica, verbose_name=('Caracteristica'), related_name='especificaciones')

    __str__ = lambda self: self.nombre


@python_2_unicode_compatible
class Bacteriologo(models.Model):
    """
    Modelo para guardar los bacteriologos del sistema.
    """
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=_('Usuario'))
    codigo = models.CharField(max_length=50, verbose_name=('Código'))
    nombre = models.CharField(max_length=200, verbose_name=('Nombre'))
    registro = models.IntegerField(verbose_name=('Registro'))
    otros = models.CharField(max_length=255, verbose_name=('Otros'), blank=True, null=True)
    firma = models.FileField(upload_to=ruta_imagen_bacteriologo, null=True, blank=True)
    areas = models.ManyToManyField(SeccionTrabajo, related_name='bacteriologos', verbose_name=_('Áreas'))

    __str__ = lambda self: '{self.nombre} ({self.registro})'.format(self=self)


@python_2_unicode_compatible
class Campo(models.Model):
    """
    Modelo para guardar los campos
    """

    TEXT = 'text'
    CHECKBOX = 'checkbox'
    RADIO = 'radio'
    SELECT = 'select'
    TEXTAREA = 'textarea'

    OPCIONES_TIPO = (
        (TEXT, _('Texto')),
        (CHECKBOX, _('Muchas Opciones')),
        (RADIO, _('Única Opción')),
        (SELECT, _('Selección')),
        (TEXTAREA, _('Texto Libre')),
    )

    name = models.CharField(max_length=150, verbose_name=_('Nombre'))
    label = models.CharField(max_length=150, verbose_name=_('Label'))
    help_text = models.CharField(max_length=255, verbose_name=_('Ayuda'), blank=True, null=True)
    value = models.TextField(max_length=255, verbose_name=_('Valor'), blank=True, null=True)
    tipo = models.CharField(max_length=10, choices=OPCIONES_TIPO, default=TEXT)
    referencia = models.CharField(max_length=255, verbose_name=_('Referencia'), blank=True, null=True)
    unidades = models.CharField(max_length=100, verbose_name=_('Unidades'), blank=True, null=True)

    def __str__(self):
        return self.render()

    def save(self, *args, **kwargs):
        if self.label:
            self.name = self.label.replace(' ', '_').lower()
        super(Campo, self).save(*args, **kwargs)

    def render(self):
        # raise NotImplementedError('No existe el método render sobre un campo.')
        return ''


@python_2_unicode_compatible
class Formato(models.Model):
    """Modelo para guardar los formatos definidos para cada prueba de laboratorio."""

    campos = models.ManyToManyField(Campo, related_name='formatos')
    observacion = models.TextField(verbose_name=_('Observación'), blank=True, null=True)
    laboratorio = models.OneToOneField(Laboratorio, related_name='formato', verbose_name=_('Laboratorio'))

    __str__ = lambda self: '({self.id})'.format(self=self)


@python_2_unicode_compatible
class Resultado(models.Model):
    """
    Modelo para guardar los resultados de las pruebas de laboratorio que fueron atendidas
    por un médico especifico.
    """

    orden = models.ForeignKey(Orden, verbose_name=_('Orden'), related_name='resultados_laboratorio')
    laboratorio = models.ForeignKey(Laboratorio, verbose_name=_('Laboratorio'), related_name='resultados')
    bacteriologo = models.ForeignKey(Bacteriologo, verbose_name=_('Bacteriólogo'), related_name='resultados')
    fecha = models.DateField(auto_now_add=True)

    resultado = models.TextField(blank=True, null=True)

    __str__ = lambda self: 'Orden #{self.orden.id} ({self.laboratorio})'.format(self=self)
