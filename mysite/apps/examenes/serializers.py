from rest_framework import serializers

from . import models
from mysite.apps.historias.serializers import OrdenSerializer
from mysite.apps.datos.serializers import UsuarioSerializer
from mysite.apps.laboratorios.mixins import IGSerializer


class VisiometriaSerializer(IGSerializer):
    """
    Serializer para las visiometrias.
    """

    orden = OrdenSerializer(
        fields=('paciente', 'fecha', 'empresa', 'institucion', 'empresa_cliente', ),
        read_only_fields=['paciente', 'fecha']
    )
    # estado_display = serializers.SerializerMethodField()

    class Meta:
        model = models.Visiometria
        fields = (
            'id', 'lentes_correctivos', 'hace_cuanto', 'cirugia', 'trauma_ocular', 'pterigio', 'colores',
            'vision_lejana_od', 'vision_lejana_oi', 'vision_lejana_ao', 'vision_cercana_od', 'vision_cercana_oi',
            'vision_cercana_ao', 'av_od', 'av_oi', 'av_ao', 'foria', 'campimetria', 'remitir_oftamologia',
            'recomendaciones', 'esf_od', 'cil_od', 'eje_od', 'add_od', 'dp_od', 'np_od', 'alt_od', 'prisma_od',
            'esf_oi', 'cil_oi', 'eje_oi', 'add_oi', 'dp_oi', 'np_oi', 'alt_oi', 'prisma_oi', 'orden', 'estado',
            'tipo',
        )
        extra_kwargs = {'tipo': {'read_only': True}}

    def __init__(self, *args, **kwargs):
        super(VisiometriaSerializer, self).__init__(*args, **kwargs)
        self.fields['estado'].required = False


class AudiometriaSerializer(IGSerializer):
    """
    Serializer para las audiometrias.
    """

    orden = OrdenSerializer(
        fields=('paciente', 'fecha', 'empresa', 'institucion', 'empresa_cliente', ),
        read_only_fields=['paciente', 'fecha']
    )

    class Meta:
        model = models.Audiometria
        fields = (
            'id', 'tiempo_exposicion', 'frecuencia', 'proteccion_auditiva', 'tipo_proteccion',
            'servicio_militar', 'practica_poligono', 'usa_motocicleta', 'cerca_explociones',
            'musica_volumen', 'usa_audifonos', 'practica_tejo', 'otros_antecedentes',
            'cirugia_oido', 'trauma', 'medicamentos_ototoxicos', 'hipoacusia', 'vertigo',
            'acufeno', 'otitis', 'otorrea', 'hz250_d', 'hz500_d', 'hz1000_d', 'hz2000_d',
            'hz3000_d', 'hz4000_d', 'hz6000_d', 'hz8000_d', 'hz250_i', 'hz500_i', 'hz1000_i',
            'hz2000_i', 'hz3000_i', 'hz4000_i', 'hz6000_i', 'hz8000_i', 'otoscopia_od',
            'otoscopia_oi', 'uso_protectores_auditivos', 'complementar_audiometria_clinica',
            'control_periodico', 'otras', 'orden', 'estado',
        )

    def __init__(self, *args, **kwargs):
        super(AudiometriaSerializer, self).__init__(*args, **kwargs)
        self.fields['estado'].required = False


class EmpleadoSerializer(IGSerializer):
    """
    Serializer de visiometra.
    """

    save_in_nested = ('usuario', )

    usuario = UsuarioSerializer(fields=('username', 'email', 'password', ))

    class Meta:
        model = models.Empleado
        fields = ('id', 'usuario', 'nombre', 'firma', )
