from django import forms
from mysite.apps.citas.models import agenda_consulta,agenda_procedimiento,citas_consulta,citas_procedimiento

class fechaForm(forms.Form):
    fechai = forms.DateField(label='Fecha', required=True)

    def __init__(self, *args, **kwargs):
		super(fechaForm, self).__init__(*args, **kwargs)
		self.fields['fechai'].widget.attrs.update({'class' : 'form-control', 'placeholder':'aaaa-mm-dd'})

class addAgendaConsultaForm(forms.ModelForm):
	class Meta:
		model   = agenda_consulta
		exclude = {'title', 'medico','editable','overlap','color'}

	def __init__(self, *args, **kwargs):
		super(addAgendaConsultaForm, self).__init__(*args, **kwargs)
		self.fields['start'].widget.attrs.update({'class' : 'form-control'})
		self.fields['end'].widget.attrs.update({'class' : 'form-control'})
															
class addCitaConsultaForm(forms.ModelForm):
	class Meta:
		model   = citas_consulta
		exclude = {'agenda', 'generadapor','paciente'}

	def __init__(self, *args, **kwargs):
		super(addCitaConsultaForm, self).__init__(*args, **kwargs)
		self.fields['pnombre'].widget.attrs.update({'class' : 'form-control mayuscula'})
		self.fields['snombre'].widget.attrs.update({'class' : 'form-control mayuscula'})
		self.fields['papellido'].widget.attrs.update({'class' : 'form-control mayuscula'})
		self.fields['sapellido'].widget.attrs.update({'class' : 'form-control mayuscula'})
		self.fields['documento'].widget.attrs.update({'class' : 'form-control'})
		self.fields['cedula'].widget.attrs.update({'class' : 'form-control'})
		self.fields['telefono'].widget.attrs.update({'class' : 'form-control'})
		self.fields['celular'].widget.attrs.update({'class' : 'form-control'})
		self.fields['consulta'].widget.attrs.update({'class' : 'form-control'})
		self.fields['empresa'].widget.attrs.update({'class' : 'form-control'})
		self.fields['observacion'].widget.attrs.update({'class' : 'form-control','rows' : '2'})
		self.fields['hora_llegada'].widget.attrs.update({'class' : 'form-control'})

class addAgendaProcedimientoForm(forms.ModelForm):
	class Meta:
		model   = agenda_procedimiento
		exclude = {'title', 'medico','editable','overlap','color'}

	def __init__(self, *args, **kwargs):
		super(addAgendaProcedimientoForm, self).__init__(*args, **kwargs)
		self.fields['start'].widget.attrs.update({'class' : 'form-control'})
		self.fields['end'].widget.attrs.update({'class' : 'form-control'})
															
class addCitaProcedimientoForm(forms.ModelForm):
	class Meta:
		model   = citas_procedimiento
		exclude = {'agenda', 'generadapor','paciente'}

	def __init__(self, *args, **kwargs):
		super(addCitaProcedimientoForm, self).__init__(*args, **kwargs)
		self.fields['pnombre'].widget.attrs.update({'class' : 'form-control mayuscula'})
		self.fields['snombre'].widget.attrs.update({'class' : 'form-control mayuscula'})
		self.fields['papellido'].widget.attrs.update({'class' : 'form-control mayuscula'})
		self.fields['sapellido'].widget.attrs.update({'class' : 'form-control mayuscula'})
		self.fields['documento'].widget.attrs.update({'class' : 'form-control'})
		self.fields['cedula'].widget.attrs.update({'class' : 'form-control'})
		self.fields['telefono'].widget.attrs.update({'class' : 'form-control'})
		self.fields['celular'].widget.attrs.update({'class' : 'form-control'})
		self.fields['procedimiento'].widget.attrs.update({'class' : 'form-control'})
		self.fields['empresa'].widget.attrs.update({'class' : 'form-control'})
		self.fields['observacion'].widget.attrs.update({'class' : 'form-control','rows' : '2'})
		self.fields['hora_llegada'].widget.attrs.update({'class' : 'form-control'})

class buscaAgendaConsultaForm(forms.ModelForm):
	class Meta:
		model   = agenda_consulta
		exclude = {'title', 'start', 'end','editable','overlap','color'}

	def __init__(self, *args, **kwargs):
		super(buscaAgendaConsultaForm, self).__init__(*args, **kwargs)
		self.fields['medico'].widget.attrs.update({'class' : 'form-control'})

class buscaAgendaProcedimientoForm(forms.ModelForm):
	class Meta:
		model   = agenda_procedimiento
		exclude = {'title', 'start', 'end','editable','overlap','color'}

	def __init__(self, *args, **kwargs):
		super(buscaAgendaProcedimientoForm, self).__init__(*args, **kwargs)
		self.fields['medico'].widget.attrs.update({'class' : 'form-control'})		