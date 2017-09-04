# -*-coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from .models import Visiometria, Audiometria


class VisiometriaForm(forms.ModelForm):
    """Formulario de Visiometrias."""

    class Meta:
        model = Visiometria
        fields = ('visiometra', )
    
    def __init__(self, *args, **kwargs):
        super(VisiometriaForm, self).__init__(*args, **kwargs)
        self.fields['visiometra'].widget.attrs.update({'class': 'form-control'})


class AudiometriaForm(forms.ModelForm):
    """Formulario de Audiometrias."""

    class Meta:
        model = Audiometria
        fields = ('audiometra', )
    
    def __init__(self, *args, **kwargs):
        super(AudiometriaForm, self).__init__(*args, **kwargs)
        self.fields['audiometra'].widget.attrs.update({'class': 'form-control'})
