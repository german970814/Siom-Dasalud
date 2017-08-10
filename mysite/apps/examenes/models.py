# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.six import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from mysite.apps.historias.models import orden as Orden
from mysite.apps.parametros.models import servicios as Servicio


def ruta_imagen_visiometra(instance, filename):
    return 'visiometria/filename/{}_{}'.format(instance.id, filename)


@python_2_unicode_compatible
class Visiometra(models.Model):
    """
    Usuario perfil de visiometra.
    """

    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=_('Usuario'))
    nombre = models.CharField(max_length=200, verbose_name=('Nombre'))
    firma = models.FileField(upload_to=ruta_imagen_visiometra, null=True, blank=True)

    def __str__(self):
        return self.nombre

    def get_firma(self):
        """
        Metodo para obtener la firma de acuerdo a los perfiles del usuario
        """
        if self.firma:
            return self.firma
        if getattr(self.usuario, 'bacteriologo', None) is not None:
            if self.usuario.bacteriologo.firma:
                return self.usuario.bacteriologo.firma
        return None


@python_2_unicode_compatible
class Visiometria(models.Model):
    """
    Modelo para los examenes de visiometria.
    """

    OJO_DERECHO = 'OD'
    OJO_IZQUIERDO = 'OI'
    AMBOS_OJOS = 'AO'

    PENDIENTE = 'PE'
    RESULTADO_EMITIDO = 'RE'

    OPCIONES_OJOS = (
        (OJO_DERECHO, _('OJO DERECHO')),
        (OJO_IZQUIERDO, _('OJO IZQUIERDO')),
        (AMBOS_OJOS, _('AMBOS OJOS'))
    )

    OPCIONES_ESTADO = (
        (PENDIENTE, _('PENDIENTE')),
        (RESULTADO_EMITIDO, _('RESULTADO EMITIDO'))
    )

    lentes_correctivos = models.NullBooleanField(verbose_name=_('Usa Lentes Correctivos'))
    hace_cuanto = models.CharField(
        max_length=100, verbose_name=_('Hace cuanto tiempo'), blank=True, null=True
    )  # hace cuanto tiempo usa lentes

    # antecedentes
    cirugia = models.NullBooleanField(verbose_name=_('Cirugía'))
    trauma_ocular = models.NullBooleanField(verbose_name=_('Trauma Ocular'))
    pterigio = models.NullBooleanField(verbose_name=_('Pterigio'))
    colores = models.NullBooleanField(verbose_name=_('Colores'))

    vision_lejana = models.CharField(max_length=2, verbose_name=_('Vision lejana'), choices=OPCIONES_OJOS, blank=True, null=True)
    vision_cercana = models.CharField(max_length=2, verbose_name=_('Vision cercana'), choices=OPCIONES_OJOS, blank=True, null=True)
    av = models.CharField(max_length=2, verbose_name=_('AV'), choices=OPCIONES_OJOS, blank=True, null=True)

    esf_od = models.CharField(max_length=50, verbose_name=_('ESF'), blank=True, null=True)
    cil_od = models.CharField(max_length=50, verbose_name=_('CIL'), blank=True, null=True)
    eje_od = models.CharField(max_length=50, verbose_name=_('EJE'), blank=True, null=True)
    add_od = models.CharField(max_length=50, verbose_name=_('ADD'), blank=True, null=True)
    dp_od = models.CharField(max_length=50, verbose_name=_('D.P'), blank=True, null=True)
    np_od = models.CharField(max_length=50, verbose_name=_('N.P'), blank=True, null=True)
    alt_od = models.CharField(max_length=50, verbose_name=_('ALT'), blank=True, null=True)
    prisma_od = models.CharField(max_length=50, verbose_name=_('PRISMA'), blank=True, null=True)

    esf_oi = models.CharField(max_length=50, verbose_name=_('ESF'), blank=True, null=True)
    cil_oi = models.CharField(max_length=50, verbose_name=_('CIL'), blank=True, null=True)
    eje_oi = models.CharField(max_length=50, verbose_name=_('EJE'), blank=True, null=True)
    add_oi = models.CharField(max_length=50, verbose_name=_('ADD'), blank=True, null=True)
    dp_oi = models.CharField(max_length=50, verbose_name=_('D.P'), blank=True, null=True)
    np_oi = models.CharField(max_length=50, verbose_name=_('N.P'), blank=True, null=True)
    alt_oi = models.CharField(max_length=50, verbose_name=_('ALT'), blank=True, null=True)
    prisma_oi = models.CharField(max_length=50, verbose_name=_('PRISMA'), blank=True, null=True)

    foria = models.CharField(max_length=100, verbose_name=_('Foria'), blank=True, null=True)
    campimetria = models.CharField(max_length=100, verbose_name=_('Campimetría'), blank=True, null=True)
    remitir_oftamologia = models.NullBooleanField(verbose_name=_('Remitir a oftamología'))

    recomendaciones = models.TextField(verbose_name=_('Recomendaciones'), blank=True, null=True)
    # constancia = models.CharField(max_length=100, verbose_name=_('En constancia de:'))

    orden = models.OneToOneField(Orden, related_name='visiometria')
    visiometra = models.ForeignKey(Visiometra, related_name='visiometrias')
    estado = models.CharField(max_length=2, choices=OPCIONES_ESTADO)

    def __str__(self):
        return 'Visiometría #{self.id}'.format(self=self)

    @classmethod
    def get_visiometria_servicio(cls):
        return Servicio.objects.get(nombre__icontains='visiometria')
