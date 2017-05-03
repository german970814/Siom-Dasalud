from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import paciente as Paciente
from mysite.apps.laboratorios.mixins import IGModelSerializer


class PacienteSerializer(IGModelSerializer, serializers.ModelSerializer):
    """
    Serializer para los pacientes
    """

    class Meta:
        model = Paciente
        fields = ('id', 'pnombre', 'snombre', 'papellido', 'sapellido', 'cedula')

    def get_nombre_completo(self, obj):
        return '{} {} {} {}'.format(obj.pnombre, obj.snombre or '', obj.papellido, obj.sapellido or '').title()

    def to_representation(self, obj):
        representation = super(PacienteSerializer, self).to_representation(obj)
        representation['nombre_completo'] = self.get_nombre_completo(obj)
        return representation


class UsuarioSerializer(IGModelSerializer, serializers.ModelSerializer):
    """
    Serialier de usuarios.
    """

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password', )
        extra_kwargs = {'password': {'write_only': True}}

    def udpate_password(self, obj, password):
        obj.set_password(password)
        return obj

    def create(self, data):
        user = get_user_model(**data)
        self.update_password(user, data['password'])
        user.save()
        return user

    def update(self, instance, data):
        for field in data:
            if field == 'password':
                self.update_password(instance, data[field])
            else:
                setattr(instance, field, data[field])
        return instance
