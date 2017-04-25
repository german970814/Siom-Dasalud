from rest_framework import serializers

from .models import Laboratorio, Equipo, SeccionTrabajo


class EquipoSerializer(serializers.ModelSerializer):
    """
    Serializzer para los equipos.
    """

    class Meta:
        model = Equipo
        fields = ('id', 'codigo', 'nombre', 'tecnica', )
        extra_kwargs = {'id': {'read_only': False}}


class SeccionTrabajoSerializer(serializers.ModelSerializer):
    """
    Serializer para las secciones de trabajo
    """

    class Meta:
        model = SeccionTrabajo
        fields = ('id', 'codigo', 'descripcion', )
        extra_kwargs = {'id': {'read_only': False}}


class LaboratorioSerializer(serializers.ModelSerializer):
    """
    Serializer para los laboratorios.
    """

    equipo = EquipoSerializer()
    seccion_trabajo = SeccionTrabajoSerializer()

    class Meta:
        model = Laboratorio
        fields = ('id', 'codigo', 'nombre', 'codigo_internacional', 'equipo', 'seccion_trabajo', )
        # read_only_fields = ('equipo', 'seccion_trabajo', )

    def create(self, data):
        equipo = Equipo.objects.get(pk=data.pop('equipo')['id'])
        seccion_trabajo = SeccionTrabajo.objects.get(id=data.pop('seccion_trabajo')['id'])
        return Laboratorio.objects.create(equipo=equipo, seccion_trabajo=seccion_trabajo, **data)

    def update(self, instance, data):
        equipo_id = data.pop('equipo')['id']
        seccion_trabajo_id = data.pop('seccion_trabajo')['id']

        for field in data:
            setattr(instance, field, data[field])

        if instance.equipo_id != equipo_id:
            instance.equipo = Equipo.objects.get(pk=equipo_id)
        if instance.seccion_trabajo_id != seccion_trabajo_id:
            instance.seccion_trabajo = SeccionTrabajo.objects.get(pk=seccion_trabajo_id)

        instance.save()
        return instance
