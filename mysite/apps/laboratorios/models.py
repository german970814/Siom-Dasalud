# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models, transaction
from django.utils.six import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.forms.utils import flatatt
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

from mysite.apps.historias.models import orden as Orden
from mysite.apps.parametros.models import servicios as Servicio

import reversion
import copy


def ruta_imagen_bacteriologo(self, filename):
    return 'laboratorios/bacteriologos/{}'.format(filename)

def ruta_imagen_empleado(self, filename):
    return 'laboratorios/empleados/{}'.format(filename)

def ruta_archivo_resultado(self, filename):
    return 'laboratorios/resultados/{}_{}'.format(self.orden.id, filename)


@python_2_unicode_compatible
class Empleado(models.Model):
    """Modelo para guardar los usuarios empleados del laboratorio"""

    nombres = models.CharField(max_length=255, verbose_name=_('Nombres'))
    apellidos = models.CharField(max_length=255, verbose_name=_('Apellidos'))
    documento = models.CharField(max_length=100, verbose_name=_('Documento'))
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=('Usuario'))
    # firma = models.FileField(upload_to=ruta_imagen_empleado, null=True, blank=True)

    def __str__(self):
        return '{self.nombres} {self.apellidos}'.format(self=self).upper()


@python_2_unicode_compatible
class Recepcion(models.Model):
    """
    Modelo para manejar las recepciones de ordenes en el sistema.
    """

    TOMA_MUESTRA = 'TO'
    EN_CURSO = 'EC'
    RESULTADO_EMITIDO = 'RE'

    ESTADO_OPCIONES = (
        (TOMA_MUESTRA, 'TOMA DE MUESTRA'),
        (EN_CURSO, 'EN CURSO'),
        (RESULTADO_EMITIDO, 'RESULTADO EMITIDO'),
    )

    orden = models.OneToOneField(Orden, related_name='recepcion', verbose_name=_('Orden'))
    estado = models.CharField(max_length=2, verbose_name=_('Estado'), choices=ESTADO_OPCIONES, default=TOMA_MUESTRA)
    empleado = models.ForeignKey(Empleado, related_name='recepciones', verbose_name=_('Empleado'))

    def __str__(self):
        laboratorios = Laboratorio.objects.filter(
            servicio__in=self.orden.OrdenProducto_orden.all().values_list('servicio__nombre__id', flat=True).distinct()
        ).values_list('codigo', flat=True)
        lab_str = ' | '.join(list(laboratorios))
        return 'Recepcion #{self.orden.id} | {laboratorios}'.format(self=self, laboratorios=lab_str)

    def save(self, *args, **kwargs):
        super(Recepcion, self).save(*args, **kwargs)
        print("si guardo")


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
class Producto(models.Model):
    """
    Modelo para guardar los productos de cada laboratorio.
    """

    REACTIVO = 'R'
    INSUMO = 'I'

    OPCIONES_TIPO = (
        (REACTIVO, _('REACTIVO')),
        (INSUMO, _('INSUMO'))
    )

    codigo = models.CharField(max_length=50, verbose_name=_('Código'))
    nombre = models.CharField(max_length=255, verbose_name=_('Nombre'))
    alarma_inferior = models.IntegerField(verbose_name=_('Alarma inferior'), blank=True, null=True)
    alarma_media = models.IntegerField(verbose_name=_('Alarma media'), blank=True, null=True)
    tipo = models.CharField(max_length=1, choices=OPCIONES_TIPO, verbose_name=_('Tipo'))
    cantidad = models.IntegerField(verbose_name=_('Cantidad'))

    __str__ = lambda self: '{self.nombre} ({self.codigo})'.format(self=self)


@reversion.register()
@python_2_unicode_compatible
class Recarga(models.Model):
    """
    Modelo para contar el historial de las recargas que se hacen a un reactivo.
    """

    producto = models.ForeignKey(Producto, verbose_name=_('Producto'), related_name='recargas')
    cantidad = models.IntegerField(verbose_name=_('Cantidad'))
    fecha = models.DateField(auto_now_add=True)
    fecha_vencimiento = models.DateField(verbose_name=_('Fecha de vencimiento'), blank=True, null=True)
    lote = models.CharField(max_length=100, verbose_name=_('Lote'), blank=True)
    distribuidor = models.CharField(max_length=100, verbose_name=_('Distribuidor'), blank=True)
    fabricante = models.CharField(max_length=100, verbose_name=_('Fabricante'), blank=True)
    marca = models.CharField(max_length=100, verbose_name=_('Marca'), blank=True)
    # fecha en la que se crea el producto.
    fecha_distribucion = models.DateField(verbose_name=_('Fecha de distribución'), blank=True, null=True)
    presentacion = models.CharField(max_length=100, verbose_name=_('Presentación'), blank=True)
    invima = models.CharField(max_length=100, verbose_name=_('Invima'), blank=True)
    casa_comercial = models.CharField(max_length=100, verbose_name=_('Casa comercial'), blank=True)

    def __str__(self):
        return '{self.producto}: Recarga de {self.cantidad}'.format(self=self)

    def save(self, *args, **kwargs):  # revisar
        with transaction.atomic():
            producto = self.producto
            if not self.pk:
                producto.cantidad += self.cantidad
            else:
                self_copy = copy.deepcopy(self)
                self_copy.refresh_from_db()

                if self.cantidad > self_copy.cantidad:  # si se ingresó más de lo que se había guardado
                    producto.cantidad += self.cantidad - self_copy.cantidad
                if self.cantidad < self_copy.cantidad:  # se se ingresó menos de lo que se había guardado
                    producto.cantidad -= self_copy.cantidad - self.cantidad
            producto.save()
            super(Recarga, self).save(*args, **kwargs)


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
class Formato(models.Model):
    """Modelo para guardar los formatos definidos para cada prueba de laboratorio."""

    formato = models.TextField()
    laboratorio = models.OneToOneField(Laboratorio, related_name='formato', verbose_name=_('Laboratorio'))

    __str__ = lambda self: '({self.id})'.format(self=self)


@reversion.register()
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
    cerrado = models.NullBooleanField(default=False, verbose_name=_('Cerrado'))
    resultado = models.TextField(blank=True, null=True)
    archivo = models.FileField(verbose_name=_('Archivo'), upload_to=ruta_archivo_resultado, blank=True, null=True)

    def __str__(self):
        return 'Orden #{self.orden.id} ({self.laboratorio})'.format(self=self)

    @transaction.atomic
    def save_hojas_gasto(self, plantillas):
        """Método para guardar las hojas de gasto."""

        if self._can_save_hojas_gasto:
            for plantilla in plantillas:
                plantilla.pop('model', None)  # PlantillaSerializer has a model prop, not use it here
                try:
                    plantilla['producto'] = Producto.objects.get(id=plantilla['producto']['id'])
                    HojaGasto.objects.create(orden=self.orden, **plantilla)
                except Producto.DoesNotExist:
                    pass
    @property
    def _can_save_hojas_gasto(self):
        """Retorna verdader si puede guardar las hojas de gasto."""

        return (
            self.cerrado and not self.orden.hojas_gasto.filter(producto__tipo=Producto.REACTIVO).exists()
        )


@python_2_unicode_compatible
class PlantillaLaboratorio(models.Model):
    """
    Modelo para guardar las plantillas por laboratorios de hojas de gastos.
    """

    laboratorio = models.ForeignKey(Laboratorio, verbose_name=_('Laboratorio'), related_name='plantillas')
    producto = models.ForeignKey(Producto, verbose_name=_('Producto'), related_name='plantillas_laboratorio')
    cantidad = models.IntegerField(default=1, verbose_name=_('Cantidad'))

    def __str__(self):
        return 'Plantilla Laboratorio #{}'.format(self.id)


@python_2_unicode_compatible
class PlantillaArea(models.Model):
    """
    Modelo para guardar las plantillas por laboratorios de hojas de gastos.
    """

    area = models.ForeignKey(SeccionTrabajo, verbose_name=_('Area'), related_name='plantillas')
    producto = models.ForeignKey(Producto, verbose_name=_('Producto'), related_name='plantillas_area')
    cantidad = models.IntegerField(default=1, verbose_name=_('Cantidad'))

    def __str__(self):
        return 'Plantilla Area #{}'.format(self.id)


@reversion.register()
@python_2_unicode_compatible
class HojaGasto(models.Model):
    """
    Modelo para guardar la hoja de gasto de los productos con respecto a las ordenes.
    """

    producto = models.ForeignKey(Producto, verbose_name=_('Producto'))
    orden = models.ForeignKey(Orden, verbose_name=_('Orden'), related_name='hojas_gasto')
    cantidad = models.IntegerField(default=1, verbose_name=_('Cantidad'))

    def __str__(self):
        return 'Hoja de gasto para orden #{}'.format(self.orden.id)

    def save(self, *args, **kwargs):
        with transaction.atomic():
            if not self.pk:
                producto = self.producto
                producto.cantidad -= self.cantidad
                producto.save()
            else:
                self_copy = copy.deepcopy(self)
                self_copy.refresh_from_db()
                producto = self.producto
                if self.cantidad > self_copy.cantidad:  # si se gastó más de lo que se había guardado
                    producto.cantidad -= self.cantidad - self_copy.cantidad
                    producto.save()
                if self.cantidad < self_copy.cantidad:  # se se gastó menos de lo que se había guardado
                    producto.cantidad += self_copy.cantidad - self.cantidad
                    producto.save()
            super(HojaGasto, self).save(*args, **kwargs)
