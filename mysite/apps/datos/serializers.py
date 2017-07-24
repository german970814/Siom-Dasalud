# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import paciente as Paciente
from mysite.apps.laboratorios.mixins import IGModelSerializer


import os


class PacienteSerializer(IGModelSerializer, serializers.ModelSerializer):
    """
    Serializer para los pacientes
    """

    unidad_edad = serializers.SerializerMethodField()

    class Meta:
        model = Paciente
        fields = (
            'id', 'pnombre', 'snombre', 'papellido',
            'sapellido', 'cedula', 'foto', 'edad',
            'unidad_edad', 'genero', 'telefono'
        )
        extra_kwargs = {'foto': {'read_only': True}}

    def get_nombre_completo(self, obj):
        return '{} {} {} {}'.format(obj.pnombre, obj.snombre or '', obj.papellido, obj.sapellido or '').title()

    def get_unidad_edad(self, obj):
        return obj.get_unidad_display()

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
        extra_kwargs = {'password': {'write_only': True, 'validators': [], 'required': False}, 'username': {'validators': []}}

    def __init__(self, *args, **kwargs):
        if 'instance' in kwargs:
            self.Meta.extra_kwargs['password']['required'] = False
        super(UsuarioSerializer, self).__init__(*args, **kwargs)

    def _validate_username(self, value, instance=None):
        def validate(username=value):
            try:
                self.Meta.model.objects.get(username=username)
                raise serializers.ValidationError('Ya Existe un usuario con ese username')
            except self.Meta.model.DoesNotExist:
                pass
        if instance and instance.pk:
            if instance.username != value:
                validate()
        else:
            validate()

    def _validate_password(self, value, instance=None):
        def validate(password=value):
            if not value:
                raise serializers.ValidationError('La contraseña es obligatoria')
            if len(password) <= 6:
                raise serializers.ValidationError('Esta contraseña es muy corta')
        if instance and instance.pk:
            if value:
                validate()
        else:
            validate()

    def update_password(self, obj, password):
        obj.set_password(password)
        return obj

    def create(self, data, commit=True):
        self._validate_username(data['username'])
        self._validate_password(data['password'])

        user = get_user_model()(**data)
        self.update_password(user, data['password'])
        if commit:
            user.save()
        return user

    def update(self, instance, data, commit=True):
        self._validate_username(data['username'], instance=instance)
        if 'password' in data:
            self._validate_password(data['password'], instance=instance)

        for field in data:
            if field == 'password' and data[field]:
                self.update_password(instance, data[field])
            else:
                setattr(instance, field, data[field])
        if commit:
            instance.save()
        return instance
