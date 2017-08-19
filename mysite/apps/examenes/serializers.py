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
            'vision_lejana', 'vision_cercana', 'av', 'foria', 'campimetria', 'remitir_oftamologia',
            'recomendaciones', 'esf_od', 'cil_od', 'eje_od', 'add_od', 'dp_od', 'np_od', 'alt_od', 'prisma_od',
            'esf_oi', 'cil_oi', 'eje_oi', 'add_oi', 'dp_oi', 'np_oi', 'alt_oi', 'prisma_oi', 'orden', 'estado'
        )

    def __init__(self, *args, **kwargs):
        super(VisiometriaSerializer, self).__init__(*args, **kwargs)
        self.fields['estado'].required = False


class VisiometraSerializer(IGSerializer):
    """
    Serializer de visiometra.
    """

    save_in_nested = ('usuario', )

    usuario = UsuarioSerializer(fields=('username', 'email', 'password', ))

    class Meta:
        model = models.Empleado
        fields = ('id', 'usuario', 'nombre', 'firma', )
