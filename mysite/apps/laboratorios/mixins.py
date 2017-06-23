from django.core.exceptions import FieldDoesNotExist
from django.db.models import ManyToManyField
from django.db import transaction

from rest_framework import serializers

import copy


class UtilsModelMixin:
    """
    Mixin de utilidades para los modelos.
    """

    def update(self, **options):
        """
        Actualiza los datos de el modelo.

        :param *options:
            Las opciones en clave:valor que van a ser cambiadas de los atributos del modelo.
        """

        keys = []
        with transaction.atomic():
            for key, value in options.items():
                setattr(self, key, value)
                keys.append(key)
            self.save(update_fields=keys)


class IGModelSerializer(object):
    """
    Mixin de Serializer como INGENIARTESOFT.
    """
    save_in_nested = False

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        read_only_fields = kwargs.pop('read_only_fields', [])
        self.save_in_nested = kwargs.pop('save_in_nested', False) or self.save_in_nested
        super(IGModelSerializer, self).__init__(*args, **kwargs)
        if fields is not None:
            self.nested = True
            for field in self.fields:
                if field not in fields and field != 'id':
                    self.fields.pop(field)
                    continue
                if field in read_only_fields:
                    self.fields[field].read_only = True

    def get_extra_kwargs(self):
        extra_kwargs = super(IGModelSerializer, self).get_extra_kwargs()
        if getattr(self, 'nested', False):
            extra_kwargs['id'] = {'read_only': False}
        return extra_kwargs

    @transaction.atomic
    def create(self, data, commit=True):
        Model = self.Meta.model
        related = {}
        for field in data:
            try:
                if Model._meta.get_field(field).is_relation:
                    if self.save_in_nested and field in self.save_in_nested:
                        if isinstance(Model._meta.get_field(field), ManyToManyField):
                            raise TypeError('No esta soportado `save_in_nested` con campos manyToMany')
                        if field in self.fields and hasattr(self.fields[field], 'create'):
                            data[field] = self.fields[field].create(
                                self._get_data_for_type(self.fields[field], data[field]), commit=commit)
                        else:
                            data[field], _ = Model._meta.get_field(
                                field).related_model.objects.get_or_create(**data[field])
                    elif isinstance(Model._meta.get_field(field), ManyToManyField):
                        related[field] = Model._meta.get_field(
                            field).related_model.objects.filter(id__in=map(
                                lambda item: item['id'] if isinstance(item, dict) else item.id, data[field]))
                    else:
                        data[field] = Model._meta.get_field(
                            field).related_model.objects.get(
                                pk=data[field]['id'] if isinstance(data[field], dict) else data[field].id)
            except FieldDoesNotExist:
                continue

        for field in related:
            if field in data:
                data.pop(field)

        if commit:
            instance, created = Model.objects.get_or_create(**data)
            for field in related:
                for model in related[field]:
                    getattr(instance, field).add(model)

        else:
            try:
                instance = Model.objects.get(**data)
            except Model.DoesNotExist:
                instance = Model(**data)
        return instance

    @transaction.atomic
    def update(self, instance, data, commit=True):
        Model = self.Meta.model
        related = {}

        for field in data:
            try:
                if Model._meta.get_field(field).is_relation:
                    if self.save_in_nested and field in self.save_in_nested:
                        if isinstance(Model._meta.get_field(field), ManyToManyField):
                            raise TypeError('No esta soportado `save_in_nested` para campos ManyToManyField.')
                        if field in self.fields and hasattr(self.fields[field], 'update'):
                            data[field] = self.fields[field].update(
                                getattr(instance, field), self._get_data_for_type(self.fields[field], data[field]), commit=commit)
                        else:
                            if hasattr(instance, field) and getattr(instance, field, None) is not None:
                                subinstance = getattr(instance, field)
                            else:
                                if not isinstance(data[field], dict):
                                    subdict = data[field].__dict__
                                    subdict.pop('_state', None)
                                    data[field] = subdict
                                if 'id' in data[field] or 'pk' in data[field]:
                                    subinstance = Model._meta.get_field(
                                        field).related_model_objects.get(pk=data[field]['id'] if 'id' in data[field] else data[field]['pk'])
                                else:
                                    if field in self.fields and hasattr(self.fields[field], 'create'):
                                        subinstance = self.fields[field].create(
                                            self._get_data_for_type(self.fields[field], data[field]), commit=commit)
                                        data[field] = subinstance
                                        continue
                                    else:
                                        subinstance, _ = Model._meta.get_field(
                                            field).related_model.objects.get_or_create(**data[field])
                                        data[field] = subinstance
                                        continue
                                for key in data[field]:
                                    setattr(subinstance, data[field][key])
                                subinstance.save()
                                subinstance.refresh_from_db()
                                data[field] = subinstance
                    elif isinstance(Model._meta.get_field(field), ManyToManyField):
                        related[field] = Model._meta.get_field(
                            field).related_model.objects.filter(id__in=map(
                                lambda item: item['id'] if isinstance(item, dict) else item.id, data[field]))
                    else:
                        overwrite = True
                        if hasattr(instance, field) and getattr(instance, field, None) is not None:
                            subinstance = getattr(instance, field)
                            if not isinstance(data[field], dict):
                                data[field] = data[field].__dict__
                            if data[field]['id'] == subinstance.id:
                                overwrite = False
                                data[field] = subinstance
                        if overwrite:
                            data[field] = Model._meta.get_field(
                                field).related_model.objects.get(
                                    pk=data[field]['id'] if isinstance(data[field], dict) else data[field].id)
            except FieldDoesNotExist:
                continue

        for field in related:
            if field in data:
                data.pop(field)
        for field in data:
            setattr(instance, field, data[field])
        if commit:
            instance.save()
            for field in related:
                getattr(instance, field).clear()
                for model in related[field]:
                    getattr(instance, field).add(model)
        return instance

    @staticmethod
    def _get_data_for_type(field, data):
        """
        Funcion para retornar solo las llaves necesarias de acuerdo a un objeto.
        """
        new_data = {}
        for key in data:
            if key in getattr(field.Meta, 'fields', field.fields):
                new_data[key] = data[key]
        return new_data

class IGSerializer(IGModelSerializer, serializers.ModelSerializer):
    pass
