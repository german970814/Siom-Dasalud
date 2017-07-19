# -*- coding: utf-8 -*- 
from django import forms
from mysite.apps.datos.models import medico,paciente

class addmedicoForm(forms.ModelForm):
    class Meta:
        model   = medico
        exclude = {'estado',}

    def __init__(self, *args, **kwargs):
        super(addmedicoForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'class' : 'form-control mayuscula'})
        self.fields['papellido'].widget.attrs.update({'class' : 'form-control mayuscula'})
        self.fields['sapellido'].widget.attrs.update({'class' : 'form-control mayuscula'})
        self.fields['cedula'].widget.attrs.update({'class' : 'form-control'})
        self.fields['especialidad'].widget.attrs.update({'class' : 'form-control'})
        self.fields['registro'].widget.attrs.update({'class' : 'form-control'})
        self.fields['usuario'].widget.attrs.update({'class' : 'form-control'})			
        self.fields['institucion'].widget.attrs.update({'class' : 'form-control'})			

class addPacienteForm(forms.ModelForm):
    class Meta:
        model   = paciente
        exclude = {'usuario','institucion',}	
        def __init__(self, *args, **kwargs):
            super(addPacienteForm, self).__init__(*args, **kwargs)
            self.fields['pnombre'].widget.attrs.update({'class' : 'form-control mayuscula'})
            self.fields['snombre'].widget.attrs.update({'class' : 'form-control mayuscula'})
            self.fields['papellido'].widget.attrs.update({'class' : 'form-control mayuscula'})
            self.fields['sapellido'].widget.attrs.update({'class' : 'form-control mayuscula'})
            self.fields['genero'].widget.attrs.update({'class' : 'form-control'})
            self.fields['fecha_nacimiento'].widget.attrs.update({'class' : 'form-control','placeholder': 'dd/mm/aaaa'})
            self.fields['nacioen'].widget.attrs.update({'class' : 'form-control'})
            self.fields['unidad'].widget.attrs.update({'class' : 'form-control'})
            self.fields['edad'].widget.attrs.update({'class' : 'form-control'})
            self.fields['documento'].widget.attrs.update({'class' : 'form-control'})
            self.fields['cedula'].widget.attrs.update({'class' : 'form-control numerico_sin_punto'})
            self.fields['estadoCivil'].widget.attrs.update({'class' : 'form-control'})
            self.fields['tipo'].widget.attrs.update({'class' : 'form-control'})
            self.fields['afiliado'].widget.attrs.update({'class' : 'form-control'})			
            self.fields['zona'].widget.attrs.update({'class' : 'form-control'})
            self.fields['escolaridad'].widget.attrs.update({'class' : 'form-control'})
            self.fields['ciudad'].widget.attrs.update({'class' : 'form-control'})			
            self.fields['profesion'].widget.attrs.update({'class' : 'form-control'})
            self.fields['direccion'].widget.attrs.update({'class' : 'form-control'})
            self.fields['barrio'].widget.attrs.update({'class' : 'form-control'})
            self.fields['Estrato'].widget.attrs.update({'class' : 'form-control'})
            self.fields['telefono'].widget.attrs.update({'class' : 'form-control'})	
            self.fields['celular'].widget.attrs.update({'class' : 'form-control'})	
            self.fields['email'].widget.attrs.update({'class' : 'form-control'})
            # Información Facturación
            self.fields['procede'].widget.attrs.update({'class' : 'form-control'})
            self.fields['visita'].widget.attrs.update({'class' : 'form-control'})
            self.fields['foto'].widget.attrs.update({'class' : 'form-control'})
            self.fields['firma'].widget.attrs.update({'class' : 'form-control'})
                                                                