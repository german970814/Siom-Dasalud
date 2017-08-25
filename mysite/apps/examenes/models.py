# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import Group
from django.utils.six import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from mysite.apps.historias.models import orden as Orden
from mysite.apps.parametros.models import servicios as Servicio


def ruta_imagen_empleado(instance, filename):
    return 'examenes/filename/{}_{}'.format(instance.id, filename)


@python_2_unicode_compatible
class Empleado(models.Model):
    """
    Empleado del sistema de Examenes.
    """

    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL, verbose_name=_('Usuario'), related_name='empleado_examenes')
    nombre = models.CharField(max_length=200, verbose_name=('Nombre'))
    firma = models.FileField(upload_to=ruta_imagen_empleado, null=True, blank=True)

    class Meta:
        permissions = (
            ('audiometra', 'Es usuario de Audiometría'),
            ('visiometra', 'Es usuario de Visiometría'),
            ('optometra', 'Es usuario de Optometría'),
        )

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

    VISIOMETRIA = 'VI'
    OPTOMETRIA = 'OP'

    OPCIONES_OJOS = (
        (OJO_DERECHO, _('OJO DERECHO')),
        (OJO_IZQUIERDO, _('OJO IZQUIERDO')),
        (AMBOS_OJOS, _('AMBOS OJOS'))
    )

    OPCIONES_ESTADO = (
        (PENDIENTE, _('PENDIENTE')),
        (RESULTADO_EMITIDO, _('RESULTADO EMITIDO'))
    )

    OPCIONES_TIPO = (
        (VISIOMETRIA, _('VISIOMETRIA')),
        (OPTOMETRIA, _('OPTOMETRIA'))
    )

    lentes_correctivos = models.NullBooleanField(verbose_name=_('Usa Lentes Correctivos'))
    hace_cuanto = models.CharField(
        max_length=100, verbose_name=_('Hace cuanto tiempo'), blank=True, null=True
    )  # hace cuanto tiempo usa lentes

    # antecedentes
    cirugia = models.CharField(max_length=50, verbose_name=_('Cirugía'), blank=True, null=True)
    trauma_ocular = models.CharField(max_length=50, verbose_name=_('Trauma Ocular'), blank=True, null=True)
    pterigio = models.CharField(max_length=50, verbose_name=_('Pterigio'), blank=True, null=True)
    colores = models.CharField(max_length=50, verbose_name=_('Colores'), blank=True, null=True)

    vision_lejana_od = models.CharField(max_length=50, verbose_name=_('Ojo Derecho'), blank=True, null=True)
    vision_lejana_oi = models.CharField(max_length=50, verbose_name=_('Ojo Izquierdo'), blank=True, null=True)
    vision_lejana_ao = models.CharField(max_length=50, verbose_name=_('Ambos ojos'), blank=True, null=True)
    vision_cercana_od = models.CharField(max_length=50, verbose_name=_('Ojo Derecho'), blank=True, null=True)
    vision_cercana_oi = models.CharField(max_length=50, verbose_name=_('Ojo Izquierdo'), blank=True, null=True)
    vision_cercana_ao = models.CharField(max_length=50, verbose_name=_('Ambos ojos'), blank=True, null=True)
    av_od = models.CharField(max_length=50, verbose_name=_('Ojo Derecho'), blank=True, null=True)
    av_oi = models.CharField(max_length=50, verbose_name=_('Ojo Izquierdo'), blank=True, null=True)
    av_ao = models.CharField(max_length=50, verbose_name=_('Ambos ojos'), blank=True, null=True)

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

    tipo = models.CharField(max_length=2, choices=OPCIONES_TIPO)
    orden = models.OneToOneField(Orden, related_name='visiometria')
    visiometra = models.ForeignKey(Empleado, related_name='visiometrias')
    estado = models.CharField(max_length=2, choices=OPCIONES_ESTADO)

    def __str__(self):
        return '{display} #{self.id}'.format(self=self, display=self.get_tipo_display())

    @classmethod
    def get_visiometria_servicio(cls):
        return Servicio.objects.get(nombre__icontains='visiometria')

    @classmethod
    def get_optometria_servicio(cls):
        return Servicio.objects.get(nombre__icontains='optometria')

    @classmethod
    def get_tipo_by_servicio(cls, orden):
        if orden.OrdenProducto_orden.filter(servicio__nombre=cls.get_visiometria_servicio()):
            return cls.VISIOMETRIA
        elif orden.OrdenProducto_orden.filter(servicio__nombre=cls.get_optometria_servicio()):
            return cls.OPTOMETRIA
        return None

    def get_servicio(self):
        """
        Retorna el servicio correspondiente de acuerdo al campo tipo.
        """
        if self.tipo == self.VISIOMETRIA:
            return self.__class__.get_visiometria_servicio()
        elif self.tipo == self.OPTOMETRIA:
            return self.__class__.get_optometria_servicio()
        raise Servicio.DoesNotExist('Servicio no existe')


@python_2_unicode_compatible
class Audiometria(models.Model):
    """Modelo para los examenes de audiometria"""

    tiempo_exposicion = models.CharField(max_length=50, verbose_name=_('Tiempo de exposición'), blank=True)
    frecuencia = models.CharField(max_length=50, verbose_name=_('Frecuencia'), blank=True)
    proteccion_auditiva = models.NullBooleanField(verbose_name=_('Protección auditiva'))
    tipo_proteccion = models.CharField(max_length=200, verbose_name=_('Tipo de protección'), blank=True)

    # antecedentes extra laborales
    servicio_militar = models.NullBooleanField(verbose_name=_('Prestó servicio militar'))
    practiva_poligono = models.NullBooleanField(verbose_name=_('Practicaba o practica poligono'))
    usa_motocicleta = models.NullBooleanField(verbose_name=_('Utiliza motocicleta'))
    cerca_explociones = models.NullBooleanField(verbose_name=_('Ha estado cerca de explociones'))
    musica_volumen = models.NullBooleanField(verbose_name=_('Escucha música alto volumén'))
    usa_audifonos = models.NullBooleanField(verbose_name=_('Usa audifonos/walman'))
    practica_tejo = models.NullBooleanField(verbose_name=_('Practica tejo, caza, entre otros'))
    otros_antecedentes = models.CharField(max_length=200, verbose_name=_('otros'), blank=True)

    # antecedentes patologicos
    cirugia_oido = models.NullBooleanField(verbose_name=_('Cirugía de oido'))
    trauma = models.NullBooleanField(verbose_name=_('Trauma'))
    medicamentos_ototoxicos = models.NullBooleanField(verbose_name=_('Medicamentos ototóxicos'))
    hipoacusia = models.NullBooleanField(verbose_name=_('Hipoacusia'))
    vertigo = models.NullBooleanField(verbose_name=_('Vértigo'))
    acufeno = models.NullBooleanField(verbose_name=_('Acufeno'))
    otitis = models.NullBooleanField(verbose_name=_('Otitis'))
    otorrea = models.NullBooleanField(verbose_name=_('Otorrea'))

    # tamizaje auditivo
    hz250_d = models.IntegerField(verbose_name=_('250hz'))
    hz500_d = models.IntegerField(verbose_name=_('500hz'))
    hz1000_d = models.IntegerField(verbose_name=_('1000hz'))
    hz2000_d = models.IntegerField(verbose_name=_('2000hz'))
    hz3000_d = models.IntegerField(verbose_name=_('3000hz'))
    hz4000_d = models.IntegerField(verbose_name=_('4000hz'))
    hz6000_d = models.IntegerField(verbose_name=_('6000hz'))
    hz8000_d = models.IntegerField(verbose_name=_('8000hz'))
    hz250_i = models.IntegerField(verbose_name=_('250hz'))
    hz500_i = models.IntegerField(verbose_name=_('500hz'))
    hz1000_i = models.IntegerField(verbose_name=_('1000hz'))
    hz2000_i = models.IntegerField(verbose_name=_('2000hz'))
    hz3000_i = models.IntegerField(verbose_name=_('3000hz'))
    hz4000_i = models.IntegerField(verbose_name=_('4000hz'))
    hz6000_i = models.IntegerField(verbose_name=_('6000hz'))
    hz8000_i = models.IntegerField(verbose_name=_('8000hz'))

    otoscopia_od = models.CharField(max_length=200, verbose_name=_('Ototoscopia od'), blank=True)
    otoscopia_oi = models.CharField(max_length=200, verbose_name=_('Ototoscopia oi'), blank=True)

    # recomendaciones
    uso_protectores_auditivos = models.NullBooleanField(verbose_name=_('Otorrea'))
    complementar_audiometria_clinica = models.NullBooleanField(verbose_name=_('Otorrea'))
    control_periodico = models.NullBooleanField(verbose_name=_('Otorrea'))
    otras = models.TextField(verbose_name=_('Otras'), blank=True)

    audiometra = models.ForeignKey()

    def __str__(self):
        return 'Audiometria #{self.id}'.format(self=self)
