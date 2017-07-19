from django import forms
from mysite.apps.organizaciones.models import empresas,instituciones,planes_salud

class addEmpresaForm(forms.ModelForm):
    class Meta:
        model   = empresas
        exclude = {'drogas', 'suministros', 'eps', 'retiene_copago', 'autoretenedor'}
    def __init__(self, *args, **kwargs):
        super(addEmpresaForm, self).__init__(*args, **kwargs)
        self.fields['nit'].widget.attrs.update({'class' : 'form-control'})
        self.fields['razon'].widget.attrs.update({'class' : 'form-control mayuscula'})
        self.fields['codigo'].widget.attrs.update({'class' : 'form-control'})
        self.fields['direccion'].widget.attrs.update({'class' : 'form-control'})
        self.fields['telefono'].widget.attrs.update({'class' : 'form-control'})
        self.fields['fax'].widget.attrs.update({'class' : 'form-control'})
        self.fields['ciudad'].widget.attrs.update({'class' : 'form-control'})
        self.fields['representante'].widget.attrs.update({'class' : 'form-control'})
        self.fields['tipo'].widget.attrs.update({'class' : 'form-control'})	
        self.fields['contrato'].widget.attrs.update({'class' : 'form-control'})	
        self.fields['poliza'].widget.attrs.update({'class' : 'form-control'})	
        self.fields['dias'].widget.attrs.update({'class' : 'form-control'})	
        self.fields['tipo_tarifa'].widget.attrs.update({'class' : 'form-control'})	
        self.fields['plan_beneficios'].widget.attrs.update({'class' : 'form-control'})		
        self.fields['regimen'].widget.attrs.update({'class' : 'form-control'})	
        self.fields['plan'].widget.attrs.update({'class' : 'form-control'})
        self.fields['valor_sedacion'].widget.attrs.update({'class' : 'form-control'})	

class addInstitucionForm(forms.ModelForm):
    class Meta:
        model   = instituciones
        fields = ['documento', 'numero', 'razon', 'codigo', 'direccion', 'telefono', 'fax', 'empresas','letra_factura']
    def __init__(self, *args, **kwargs):
        super(addInstitucionForm, self).__init__(*args, **kwargs)
        self.fields['documento'].widget.attrs.update({'class' : 'form-control'})
        self.fields['numero'].widget.attrs.update({'class' : 'form-control'})
        self.fields['razon'].widget.attrs.update({'class' : 'form-control mayuscula'})
        self.fields['codigo'].widget.attrs.update({'class' : 'form-control'})
        self.fields['direccion'].widget.attrs.update({'class' : 'form-control'})
        self.fields['telefono'].widget.attrs.update({'class' : 'form-control'})
        self.fields['fax'].widget.attrs.update({'class' : 'form-control'})	
        self.fields['empresas'].widget.attrs.update({'class' : 'form-control'})
        self.fields['letra_factura'].widget.attrs.update({'class' : 'form-control'})		

class addPlanForm(forms.ModelForm):
    class Meta:
        model   = planes_salud
        fields = ['descripcion', 'porcentaje']	
        def __init__(self, *args, **kwargs):
            super(addPlanForm, self).__init__(*args, **kwargs)
            self.fields['descripcion'].widget.attrs.update({'class' : 'form-control'})
            self.fields['porcentaje'].widget.attrs.update({'class' : 'form-control'})		
                                                                