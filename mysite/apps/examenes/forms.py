# -*-coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from .models import Visiometria


class VisisometriaForm(forms.ModelForm):
    """Formulario de Visiometrias."""

    class Meta:
        model = Visiometria
        fields = ('visiometra', )
    
    def __init__(self, *args, **kwargs):
        # self.orden = orden
        super(Visiometria, self).__init__(*args, **kwargs)
        self.fields['visiometra'].widget.attrs.update({'class': 'form-control'})
        # self.fields['orden'].widget.attrs.update({'class': 'form-control'})
