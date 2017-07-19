# -*- coding: utf-8 -*-
from django import forms
from mysite.apps.parametros.models import procedimientos,items, servicios, serviciosEmpresa	


class addProcedimientoForm(forms.ModelForm):
    class Meta:
        model   = procedimientos
        fields = ['codigo', 'descripcion', 'cups', 'cuenta_contable', 'equipo', 'tarifa', 'items', 'uvr']		
        def __init__(self, *args, **kwargs):
            super(addProcedimientoForm, self).__init__(*args, **kwargs)
            self.fields['codigo'].widget.attrs.update({'class' : 'form-control'})
            self.fields['descripcion'].widget.attrs.update({'class' : 'form-control mayuscula'})
            self.fields['cups'].widget.attrs.update({'class' : 'form-control'})
            self.fields['cuenta_contable'].widget.attrs.update({'class' : 'form-control'})
            self.fields['equipo'].widget.attrs.update({'class' : 'form-control'})	
            self.fields['tarifa'].widget.attrs.update({'class' : 'form-control'})
            self.fields['items'].widget.attrs.update({'class' : 'form-control'})
            self.fields['uvr'].widget.attrs.update({'class' : 'form-control'})

class addPlantillaForm(forms.ModelForm):
    class Meta:
        model   = items
        fields = ['nombre', 'descripcion',]		
        def __init__(self, *args, **kwargs):
            super(addPlantillaForm, self).__init__(*args, **kwargs)
            self.fields['nombre'].widget.attrs.update({'class' : 'form-control mayuscula'})
            self.fields['descripcion'].widget.attrs.update({'class' : 'form-control'})

class serviciosForm(forms.ModelForm):
    class Meta:
        model   = serviciosEmpresa
        fields = ['nombre',]		
        def __init__(self, *args, **kwargs):
            super(serviciosForm, self).__init__(*args, **kwargs)
            self.fields['nombre'].widget.attrs.update({'class' : 'form-control'})