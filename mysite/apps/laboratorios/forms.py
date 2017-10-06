from django import forms
from django.utils.translation import ugettext_lazy as _

import datetime


class HojaTrabajoForm(forms.Form):
    """
    Formulario para crear las hojas de trabajo de los laboratorios.
    """

    desde_fecha = forms.DateField()
    hasta_fecha = forms.DateField(required=False)
    desde_hora = forms.TimeField(required=False)
    hasta_hora = forms.TimeField(required=False)

    def __init__(self, *args, **kwargs):
        super(HojaTrabajoForm, self).__init__(*args, **kwargs)

        if self.is_bound:
            if self.data.get('desde_hora') and not self.data.get('hasta_hora'):
                self.fields['hasta_hora'].required = True
            elif self.data.get('hasta_hora') and not self.data.get('desde_hora'):
                self.fields['desde_hora'].required = False

    def clean(self, *args, **kwargs):
        cleaned_data = super(HojaTrabajoForm, self).clean(*args, **kwargs)

        desde = cleaned_data.get('desde_fecha')
        hasta = cleaned_data.get('hasta_fecha')
        desde_hora = cleaned_data.get('desde_hora')
        hasta_hora = cleaned_data.get('hasta_hora')

        if desde is not None and hasta is not None:
            if desde >= hasta:
                self.add_error('hasta_fecha', _('La fecha "Hasta" no puede ser menor a la fecha "Desde"'))
            elif desde == hasta:
                if desde_hora is not None and hasta_hora is not None:
                    if desde_hora >= hasta_hora:
                        self.add_error('desde_hora',
                            _('La hora "Desde" no puede ser mayor a la hora "Hasta"'))
                        self.add_error('hasta_hora',
                            _('La hora "Hasta" no puede ser menor a la hora "Desde"'))
                else:
                    self.add_error('hasta_fecha', _('La fecha "Hasta" no puede ser igual a la fecha "Desde"'))
                        
        return cleaned_data

    def get_datetime(self, date, time):
        if time is not None:
            return datetime.datetime.combine(date, time)
        return date
