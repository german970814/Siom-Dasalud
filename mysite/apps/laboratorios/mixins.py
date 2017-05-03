from django.core.exceptions import FieldDoesNotExist

class IGModelSerializer(object):
    """
    Mixin de Serializer como INGENIARTESOFT.
    """

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super(IGModelSerializer, self).__init__(*args, **kwargs)
        if fields is not None:
            self.nested = True
            for field in self.fields:
                if field not in fields and field != 'id':
                    self.fields.pop(field)

    def get_extra_kwargs(self):
        extra_kwargs = super(IGModelSerializer, self).get_extra_kwargs()
        if getattr(self, 'nested', False):
            extra_kwargs['id'] = {'read_only': False}
        return extra_kwargs

    def create(self, data):
        Model = self.Meta.model
        for field in data:
            try:
                if Model._meta.get_field(field).is_relation:
                    data[field] = Model._meta.get_field(
                        field).related_model.objects.get(pk=data[field]['id'])
            except FieldDoesNotExist:
                continue
        instance, created = Model.objects.get_or_create(**data)
        return instance

    def update(self, instance, data):
        Model = self.Meta.model

        for field in data:
            try:
                if Model._meta.get_field(field).is_relation:
                    data[field] = Model._meta.get_field(
                        field).related_model.objects.get(pk=data[field]['id'])
            except FieldDoesNotExist:
                continue

        for field in data:
            setattr(instance, field, data[field])

        instance.save()
        return instance
