from django import forms
from mysite.apps.historias.models import orden,ordenesProducto,historia_clinica,test_altura,historia_procedimientos,posologias,remision,remisionlab

class addOrdenForm(forms.ModelForm):
	class Meta:
		model   = orden
		exclude = {'paciente','status','generadapor',}

	def __init__(self, *args, **kwargs):
		super(addOrdenForm, self).__init__(*args, **kwargs)
		self.fields['empresa'].widget.attrs.update({'class' : 'form-control'})
		self.fields['medico'].widget.attrs.update({'class' : 'form-control'})
		self.fields['institucion'].widget.attrs.update({'class' : 'form-control'})
		self.fields['fecha'].widget.attrs.update({'class' : 'form-control'})
		self.fields['fecha_atencion'].widget.attrs.update({'class' : 'form-control'})
		self.fields['autorizacion'].widget.attrs.update({'class' : 'form-control'})
		self.fields['observacion'].widget.attrs.update({'class' : 'form-control','rows' : '2'})
		self.fields['tipo'].widget.attrs.update({'class' : 'form-control'})
		self.fields['consulta'].widget.attrs.update({'class' : 'form-control'})
		self.fields['procedimiento'].widget.attrs.update({'class' : 'form-control'})
		self.fields['valor'].widget.attrs.update({'class' : 'form-control'})
		self.fields['afiliado'].widget.attrs.update({'class' : 'form-control'})
		self.fields['tipo_usuario'].widget.attrs.update({'class' : 'form-control'})
		self.fields['rango'].widget.attrs.update({'class' : 'form-control'})
		self.fields['copago'].widget.attrs.update({'class' : 'form-control'})
		self.fields['couta'].widget.attrs.update({'class' : 'form-control'})
		self.fields['total'].widget.attrs.update({'class' : 'form-control'})
		self.fields['valor_sedacion'].widget.attrs.update({'class' : 'form-control'})
		self.fields['anestesiologo'].widget.attrs.update({'class' : 'form-control'})

class addOrdenSiomForm(forms.ModelForm):
	class Meta:
		model   = orden
		exclude = {'paciente','status','generadapor',}

	def __init__(self, *args, **kwargs):
		super(addOrdenSiomForm, self).__init__(*args, **kwargs)
		self.fields['empresa'].widget.attrs.update({'class' : 'form-control'})
		self.fields['medico'].widget.attrs.update({'class' : 'form-control'})
		self.fields['institucion'].widget.attrs.update({'class' : 'form-control'})
		self.fields['fecha'].widget.attrs.update({'class' : 'form-control'})
		self.fields['fecha_atencion'].widget.attrs.update({'class' : 'form-control'})
		self.fields['examen'].widget.attrs.update({'class' : 'form-control'})
		self.fields['examen_adicional'].widget.attrs.update({'class' : 'form-control'})
		self.fields['empresa_cliente'].widget.attrs.update({'class' : 'form-control'})
		self.fields['cargo'].widget.attrs.update({'class' : 'form-control'})
		self.fields['seccion'].widget.attrs.update({'class' : 'form-control'})

class addOrdenAnulaForm(forms.ModelForm):
	class Meta:
		model   = orden
		fields = ['anulada','razon_anulacion']

	def __init__(self, *args, **kwargs):
		super(addOrdenAnulaForm, self).__init__(*args, **kwargs)
		self.fields['anulada'].widget.attrs.update({'class' : 'form-control'})
		self.fields['razon_anulacion'].widget.attrs.update({'class' : 'form-control'})

class filtroOrdenForm(forms.ModelForm):
	class Meta:
		model   = orden
		fields = ['empresa','institucion']

	def __init__(self, *args, **kwargs):
		super(filtroOrdenForm, self).__init__(*args, **kwargs)
		self.fields['empresa'].widget.attrs.update({'class' : 'form-control'})
		self.fields['institucion'].widget.attrs.update({'class' : 'form-control'})

class addOrdenProductoForm(forms.ModelForm):
	class Meta:
		model   = ordenesProducto
		fields = ['servicio']

	def __init__(self, *args, **kwargs):
		super(addOrdenProductoForm, self).__init__(*args, **kwargs)
		self.fields['servicio'].widget.attrs.update({'class' : 'form-control'})

class addhistoria_clinicaForm(forms.ModelForm):
	class Meta:
		model   = historia_clinica
		exclude = {'paciente','primera_vez','orden',}

	def __init__(self, *args, **kwargs):
		super(addhistoria_clinicaForm, self).__init__(*args, **kwargs)
		self.fields['hijos'].widget.attrs.update({'class' : 'form-control'})
		self.fields['num_hijos'].widget.attrs.update({'class' : 'form-control numerico'})
		self.fields['turno'].widget.attrs.update({'class' : 'form-control'})
		self.fields['actividad'].widget.attrs.update({'class' : 'form-control'})
		self.fields['eps'].widget.attrs.update({'class' : 'form-control'})
		self.fields['arl'].widget.attrs.update({'class' : 'form-control'})
		self.fields['afp'].widget.attrs.update({'class' : 'form-control'})
		#Antecedentes de Trabajos u oficios
		self.fields['a_empresa1'].widget.attrs.update({'class' : 'form-control'})
		self.fields['a_ocupacion1'].widget.attrs.update({'class' : 'form-control'})
		self.fields['a_tiempo1'].widget.attrs.update({'class' : 'form-control'})
		self.fields['a_biolog1'].widget.attrs.update({'class' : 'form-control'})
		self.fields['a_mec1'].widget.attrs.update({'class' : 'form-control'})
		self.fields['a_fis1'].widget.attrs.update({'class' : 'form-control'})
		self.fields['a_erg1'].widget.attrs.update({'class' : 'form-control'})
		self.fields['a_psi1'].widget.attrs.update({'class' : 'form-control'})
		self.fields['a_qui1'].widget.attrs.update({'class' : 'form-control'})
		self.fields['a_prot1'].widget.attrs.update({'class' : 'form-control'})
		self.fields['a_empresa2'].widget.attrs.update({'class' : 'form-control'})
		self.fields['a_ocupacion2'].widget.attrs.update({'class' : 'form-control'})
		self.fields['a_tiempo2'].widget.attrs.update({'class' : 'form-control'})
		self.fields['a_biolog2'].widget.attrs.update({'class' : 'form-control'})
		self.fields['a_mec2'].widget.attrs.update({'class' : 'form-control'})
		self.fields['a_fis2'].widget.attrs.update({'class' : 'form-control'})
		self.fields['a_erg2'].widget.attrs.update({'class' : 'form-control'})
		self.fields['a_psi2'].widget.attrs.update({'class' : 'form-control'})
		self.fields['a_qui2'].widget.attrs.update({'class' : 'form-control'})
		self.fields['a_prot2'].widget.attrs.update({'class' : 'form-control'})
		self.fields['accidente'].widget.attrs.update({'class' : 'form-control'})
		self.fields['enfermedad_profesional'].widget.attrs.update({'class' : 'form-control'})
		self.fields['detalle'].widget.attrs.update({'class' : 'form-control','rows' : '2'})
		#Antecedentes(Todos estos: Negativos)
		self.fields['quirurgicos'].widget.attrs.update({'class' : 'form-control'})
		self.fields['hospitalizacion'].widget.attrs.update({'class' : 'form-control'})
		self.fields['accidente_p'].widget.attrs.update({'class' : 'form-control'})
		self.fields['fracturas'].widget.attrs.update({'class' : 'form-control'})
		self.fields['tabaquismo'].widget.attrs.update({'class' : 'form-control'})
		self.fields['intoxicaciones'].widget.attrs.update({'class' : 'form-control'})
		self.fields['alcoholismo'].widget.attrs.update({'class' : 'form-control'})
		self.fields['mentales'].widget.attrs.update({'class' : 'form-control'})
		self.fields['asma'].widget.attrs.update({'class' : 'form-control'})
		self.fields['tbc'].widget.attrs.update({'class' : 'form-control'})
		self.fields['alergias'].widget.attrs.update({'class' : 'form-control'})
		self.fields['gripas'].widget.attrs.update({'class' : 'form-control'})
		self.fields['enf_piel'].widget.attrs.update({'class' : 'form-control'})
		self.fields['otologicos'].widget.attrs.update({'class' : 'form-control'})
		self.fields['diabetes'].widget.attrs.update({'class' : 'form-control'})
		self.fields['hematologicos'].widget.attrs.update({'class' : 'form-control'})
		self.fields['epilepsia'].widget.attrs.update({'class' : 'form-control'})
		self.fields['cancer'].widget.attrs.update({'class' : 'form-control'})
		self.fields['hipertension'].widget.attrs.update({'class' : 'form-control'})
		self.fields['otros'].widget.attrs.update({'class' : 'form-control'})
		#Antecedentes Familiares
		self.fields['f_quirurgicos'].widget.attrs.update({'class' : 'form-control'})
		self.fields['f_hospitalizacion'].widget.attrs.update({'class' : 'form-control'})
		self.fields['f_accidente_p'].widget.attrs.update({'class' : 'form-control'})
		self.fields['f_fracturas'].widget.attrs.update({'class' : 'form-control'})
		self.fields['f_tabaquismo'].widget.attrs.update({'class' : 'form-control'})
		self.fields['f_intoxicaciones'].widget.attrs.update({'class' : 'form-control'})
		self.fields['f_alcoholismo'].widget.attrs.update({'class' : 'form-control'})
		self.fields['f_mentales'].widget.attrs.update({'class' : 'form-control'})
		self.fields['f_asma'].widget.attrs.update({'class' : 'form-control'})
		self.fields['f_tbc'].widget.attrs.update({'class' : 'form-control'})
		self.fields['f_alergias'].widget.attrs.update({'class' : 'form-control'})
		self.fields['f_gripas'].widget.attrs.update({'class' : 'form-control'})
		self.fields['f_enf_piel'].widget.attrs.update({'class' : 'form-control'})
		self.fields['f_otologicos'].widget.attrs.update({'class' : 'form-control'})
		self.fields['f_diabetes'].widget.attrs.update({'class' : 'form-control'})
		self.fields['f_hematologicos'].widget.attrs.update({'class' : 'form-control'})
		self.fields['f_epilepsia'].widget.attrs.update({'class' : 'form-control'})
		self.fields['f_cancer'].widget.attrs.update({'class' : 'form-control'})
		self.fields['f_hipertension'].widget.attrs.update({'class' : 'form-control'})
		self.fields['f_otros'].widget.attrs.update({'class' : 'form-control'})
		self.fields['descripcion_antecedente'].widget.attrs.update({'class' : 'form-control','rows' : '3'})
		#Habitos
		self.fields['alcohol'].widget.attrs.update({'class' : 'form-control'})
		self.fields['deportes'].widget.attrs.update({'class' : 'form-control'})
		self.fields['frecuencia'].widget.attrs.update({'class' : 'form-control','rows' : '1'})
		#Gineco
		self.fields['menarquia'].widget.attrs.update({'class' : 'form-control'})
		self.fields['hijos_vivos'].widget.attrs.update({'class' : 'form-control'})
		self.fields['ciclos'].widget.attrs.update({'class' : 'form-control'})
		self.fields['gravida'].widget.attrs.update({'class' : 'form-control numerico'})
		self.fields['partos'].widget.attrs.update({'class' : 'form-control numerico'})
		self.fields['abortos'].widget.attrs.update({'class' : 'form-control numerico'})
		self.fields['cesareas'].widget.attrs.update({'class' : 'form-control numerico'})
		self.fields['fum'].widget.attrs.update({'class' : 'form-control'})
		self.fields['fup'].widget.attrs.update({'class' : 'form-control'})
		self.fields['dismenorrea'].widget.attrs.update({'class' : 'form-control'})
		self.fields['metrorragias'].widget.attrs.update({'class' : 'form-control'})
		self.fields['trastorno_ciclo'].widget.attrs.update({'class' : 'form-control'})
		self.fields['citologias'].widget.attrs.update({'class' : 'form-control'})
		self.fields['transtorno_otros'].widget.attrs.update({'class' : 'form-control'})
		self.fields['planificacion'].widget.attrs.update({'class' : 'form-control'})
		self.fields['sintomas'].widget.attrs.update({'class' : 'form-control','rows' : '2'})
		#Signos Vitales
		self.fields['peso'].widget.attrs.update({'class' : 'form-control numerico'})
		self.fields['talla'].widget.attrs.update({'class' : 'form-control numerico'})
		self.fields['pulso'].widget.attrs.update({'class' : 'form-control'})
		self.fields['temperatura'].widget.attrs.update({'class' : 'form-control numerico'})
		self.fields['presion_arterial'].widget.attrs.update({'class' : 'form-control presion'})
		self.fields['masa_corporal'].widget.attrs.update({'class' : 'form-control numerico'})
		#Estado General
		self.fields['estado'].widget.attrs.update({'class' : 'form-control'})
		self.fields['escribe'].widget.attrs.update({'class' : 'form-control'})
		#Exploracion Osea Muscular
		self.fields['cabeza'].widget.attrs.update({'class' : 'form-control'})
		self.fields['cuello'].widget.attrs.update({'class' : 'form-control'})
		self.fields['torax'].widget.attrs.update({'class' : 'form-control'})
		self.fields['abdomen'].widget.attrs.update({'class' : 'form-control'})
		self.fields['columna_cervical'].widget.attrs.update({'class' : 'form-control'})
		self.fields['columna_dorsal'].widget.attrs.update({'class' : 'form-control'})
		self.fields['columna_lumbo'].widget.attrs.update({'class' : 'form-control'})
		self.fields['m_superiores'].widget.attrs.update({'class' : 'form-control'})
		self.fields['m_inferiores'].widget.attrs.update({'class' : 'form-control'})
		self.fields['descripcion_osteomuscular'].widget.attrs.update({'class' : 'form-control','rows' : '3'})
		#Dinamica (Movimientos Articulares)
		self.fields['d_cuello'].widget.attrs.update({'class' : 'form-control'})
		self.fields['d_hombros'].widget.attrs.update({'class' : 'form-control'})
		self.fields['d_codo'].widget.attrs.update({'class' : 'form-control'})
		self.fields['d_muneca'].widget.attrs.update({'class' : 'form-control'})
		self.fields['d_cadera'].widget.attrs.update({'class' : 'form-control'})
		self.fields['d_rodilla'].widget.attrs.update({'class' : 'form-control'})
		self.fields['d_tobillo'].widget.attrs.update({'class' : 'form-control'})
		self.fields['d_cuello_o'].widget.attrs.update({'class' : 'form-control','rows' : '1'})
		self.fields['d_hombros_o'].widget.attrs.update({'class' : 'form-control','rows' : '1'})
		self.fields['d_codo_o'].widget.attrs.update({'class' : 'form-control','rows' : '1'})
		self.fields['d_muneca_o'].widget.attrs.update({'class' : 'form-control','rows' : '1'})
		self.fields['d_cadera_o'].widget.attrs.update({'class' : 'form-control','rows' : '1'})
		self.fields['d_rodilla_o'].widget.attrs.update({'class' : 'form-control','rows' : '1'})
		self.fields['d_tobillo_o'].widget.attrs.update({'class' : 'form-control','rows' : '1'})
		#Organos o Sistemas
		self.fields['cicatrices'].widget.attrs.update({'class' : 'form-control'})
		self.fields['piel'].widget.attrs.update({'class' : 'form-control'})
		self.fields['craneo'].widget.attrs.update({'class' : 'form-control'})
		#Ojos
		self.fields['conjuntivas'].widget.attrs.update({'class' : 'form-control'})
		self.fields['pupilas'].widget.attrs.update({'class' : 'form-control'})
		self.fields['anexos'].widget.attrs.update({'class' : 'form-control'})
		self.fields['reflejos'].widget.attrs.update({'class' : 'form-control'})
		self.fields['fondo'].widget.attrs.update({'class' : 'form-control'})
		#Oidos
		self.fields['pabellones'].widget.attrs.update({'class' : 'form-control'})
		self.fields['ostocopia'].widget.attrs.update({'class' : 'form-control'})
		#Nariz
		self.fields['tabique'].widget.attrs.update({'class' : 'form-control'})
		self.fields['cornetes'].widget.attrs.update({'class' : 'form-control'})
		#Boca
		self.fields['labios'].widget.attrs.update({'class' : 'form-control'})
		self.fields['faringe'].widget.attrs.update({'class' : 'form-control'})
		#Otros
		self.fields['tiroides'].widget.attrs.update({'class' : 'form-control'})
		self.fields['o_torax'].widget.attrs.update({'class' : 'form-control'})
		self.fields['pulmones'].widget.attrs.update({'class' : 'form-control'})
		self.fields['corazon'].widget.attrs.update({'class' : 'form-control'})
		#Abdomen
		self.fields['pared'].widget.attrs.update({'class' : 'form-control'})
		self.fields['viseras'].widget.attrs.update({'class' : 'form-control'})
		self.fields['hernias'].widget.attrs.update({'class' : 'form-control'})
		self.fields['genitales'].widget.attrs.update({'class' : 'form-control'})
		self.fields['vascular'].widget.attrs.update({'class' : 'form-control'})
		#Sistema Nervioso
		self.fields['o_reflejos'].widget.attrs.update({'class' : 'form-control'})
		self.fields['marcha'].widget.attrs.update({'class' : 'form-control'})
		self.fields['coordinacion'].widget.attrs.update({'class' : 'form-control'})
		#Sistema Circulatorio
		self.fields['ruidos'].widget.attrs.update({'class' : 'form-control'})

		self.fields['extrasistoles'].widget.attrs.update({'class' : 'form-control'})
		self.fields['fibrilacion'].widget.attrs.update({'class' : 'form-control'})
		self.fields['soplos'].widget.attrs.update({'class' : 'form-control'})
		self.fields['sistolicos'].widget.attrs.update({'class' : 'form-control'})
		self.fields['diastolicos'].widget.attrs.update({'class' : 'form-control'})
		self.fields['presistolicos'].widget.attrs.update({'class' : 'form-control'})
		self.fields['vasos'].widget.attrs.update({'class' : 'form-control'})
		self.fields['varices'].widget.attrs.update({'class' : 'form-control'})
		self.fields['observaciones'].widget.attrs.update({'class' : 'form-control','rows' : '5'})
		self.fields['tunel'].widget.attrs.update({'class' : 'form-control','rows' : '5'})
		self.fields['phannel'].widget.attrs.update({'class' : 'form-control'})
		self.fields['tinnel'].widget.attrs.update({'class' : 'form-control'})
		self.fields['pre_concepto'].widget.attrs.update({'class' : 'form-control'})
		#Examenes de Diagnosticos
		self.fields['f_imagen'].widget.attrs.update({'class' : 'form-control'})
		self.fields['r_imagen'].widget.attrs.update({'class' : 'form-control','rows' : '1'})
		self.fields['f_audiometria'].widget.attrs.update({'class' : 'form-control'})
		self.fields['r_audiometria'].widget.attrs.update({'class' : 'form-control','rows' : '1'})
		self.fields['f_visiometria'].widget.attrs.update({'class' : 'form-control'})
		self.fields['r_visiometria'].widget.attrs.update({'class' : 'form-control','rows' : '1'})
		self.fields['f_espirometria'].widget.attrs.update({'class' : 'form-control'})
		self.fields['r_espirometria'].widget.attrs.update({'class' : 'form-control','rows' : '1'})
		self.fields['f_laboratorio'].widget.attrs.update({'class' : 'form-control'})
		self.fields['r_laboratorio'].widget.attrs.update({'class' : 'form-control','rows' : '1'})
		self.fields['concepto'].widget.attrs.update({'class' : 'form-control'})
		self.fields['remitir'].widget.attrs.update({'class' : 'form-control'})
		self.fields['valoracion'].widget.attrs.update({'class' : 'form-control','rows' : '3'})
		self.fields['recomendacion'].widget.attrs.update({'class' : 'form-control','rows' : '3'})			

class addtest_alturaForm(forms.ModelForm):
	class Meta:
		model   = test_altura
		exclude = {'orden',}

	def __init__(self, *args, **kwargs):
		super(addtest_alturaForm, self).__init__(*args, **kwargs)
		self.fields['convulsiones_p'].widget.attrs.update({'class' : 'form-control'})
		self.fields['diabetes'].widget.attrs.update({'class' : 'form-control'})
		self.fields['reacciones'].widget.attrs.update({'class' : 'form-control'})
		self.fields['claustrofobia'].widget.attrs.update({'class' : 'form-control'})
		self.fields['acrofobia'].widget.attrs.update({'class' : 'form-control'})
		self.fields['vertigos'].widget.attrs.update({'class' : 'form-control'})
		self.fields['epilepsia'].widget.attrs.update({'class' : 'form-control'})
		self.fields['enfermedad_mental'].widget.attrs.update({'class' : 'form-control'})
		self.fields['a_cardiaco'].widget.attrs.update({'class' : 'form-control'})
		self.fields['a_cerebro_v'].widget.attrs.update({'class' : 'form-control'})
		self.fields['angina_pecho'].widget.attrs.update({'class' : 'form-control'})
		self.fields['insuficiencia_cardiaca'].widget.attrs.update({'class' : 'form-control'})
		self.fields['hinchazon_pies'].widget.attrs.update({'class' : 'form-control'})
		self.fields['latidos'].widget.attrs.update({'class' : 'form-control'})
		self.fields['presion'].widget.attrs.update({'class' : 'form-control'})
		self.fields['otro'].widget.attrs.update({'class' : 'form-control'})
		self.fields['dolor_pecho1'].widget.attrs.update({'class' : 'form-control'})
		self.fields['dolor_pecho2'].widget.attrs.update({'class' : 'form-control'})
		self.fields['dolor_pecho3'].widget.attrs.update({'class' : 'form-control'})
		self.fields['late_irregularmente'].widget.attrs.update({'class' : 'form-control'})
		self.fields['dolor_pecho_indigestion'].widget.attrs.update({'class' : 'form-control'})
		self.fields['otros_sintomas'].widget.attrs.update({'class' : 'form-control'})
		self.fields['lentes_contacto'].widget.attrs.update({'class' : 'form-control'})
		self.fields['lentes'].widget.attrs.update({'class' : 'form-control'})
		self.fields['daltonismo'].widget.attrs.update({'class' : 'form-control'})
		self.fields['problema_ojos'].widget.attrs.update({'class' : 'form-control'})
		self.fields['ob_problema'].widget.attrs.update({'class' : 'form-control'})
		self.fields['prob_pulmonares'].widget.attrs.update({'class' : 'form-control'})
		self.fields['prob_circulacion'].widget.attrs.update({'class' : 'form-control'})
		self.fields['presion_alta'].widget.attrs.update({'class' : 'form-control'})
		self.fields['convulsiones'].widget.attrs.update({'class' : 'form-control'})
		self.fields['enf_mental'].widget.attrs.update({'class' : 'form-control'})
		self.fields['perdida_vista'].widget.attrs.update({'class' : 'form-control'})
		self.fields['dano_oidos'].widget.attrs.update({'class' : 'form-control'})
		self.fields['dificultad_oir'].widget.attrs.update({'class' : 'form-control'})
		self.fields['aparato_oir'].widget.attrs.update({'class' : 'form-control'})
		self.fields['prob_audicion'].widget.attrs.update({'class' : 'form-control'})
		self.fields['d_prob_audicion'].widget.attrs.update({'class' : 'form-control'})
		self.fields['debilidad_brazos'].widget.attrs.update({'class' : 'form-control'})
		self.fields['dolor_espalda'].widget.attrs.update({'class' : 'form-control'})
		self.fields['dificultad_extremidades'].widget.attrs.update({'class' : 'form-control'})
		self.fields['dolor_rigidez'].widget.attrs.update({'class' : 'form-control'})
		self.fields['dif_cabeza_arriba'].widget.attrs.update({'class' : 'form-control'})
		self.fields['dif_cabeza_lado'].widget.attrs.update({'class' : 'form-control'})
		self.fields['dif_agacharse'].widget.attrs.update({'class' : 'form-control'})
		self.fields['dif_agacharse_piso'].widget.attrs.update({'class' : 'form-control'})
		self.fields['dif_escalera'].widget.attrs.update({'class' : 'form-control'})
		self.fields['lesion_espalda'].widget.attrs.update({'class' : 'form-control'})
		self.fields['d_lesion'].widget.attrs.update({'class' : 'form-control'})
		self.fields['romberg'].widget.attrs.update({'class' : 'form-control'})
		self.fields['ob_romberg'].widget.attrs.update({'class' : 'form-control'})
		self.fields['baranay'].widget.attrs.update({'class' : 'form-control'})
		self.fields['ob_baranay'].widget.attrs.update({'class' : 'form-control'})
		self.fields['hallpike'].widget.attrs.update({'class' : 'form-control'})
		self.fields['ob_hallpike'].widget.attrs.update({'class' : 'form-control'})
		self.fields['babinski_m_d'].widget.attrs.update({'class' : 'form-control'})
		self.fields['ob_babinski_m_d'].widget.attrs.update({'class' : 'form-control'})
		self.fields['babinski_m_i'].widget.attrs.update({'class' : 'form-control'})
		self.fields['ob_babinski_m_i'].widget.attrs.update({'class' : 'form-control'})
		self.fields['babinski_m_n'].widget.attrs.update({'class' : 'form-control'})
		self.fields['ob_babinski_m_n'].widget.attrs.update({'class' : 'form-control'})
		self.fields['unterberger_m_d'].widget.attrs.update({'class' : 'form-control'})
		self.fields['ob_unterberger_m_d'].widget.attrs.update({'class' : 'form-control'})
		self.fields['unterberger_m_c'].widget.attrs.update({'class' : 'form-control'})
		self.fields['ob_unterberger_m_c'].widget.attrs.update({'class' : 'form-control'})
		self.fields['unterberger_m_i'].widget.attrs.update({'class' : 'form-control'})
		self.fields['ob_unterberger_m_i'].widget.attrs.update({'class' : 'form-control'})
		self.fields['neg_vert_per'].widget.attrs.update({'class' : 'form-control'})
		self.fields['ob_neg_vert_per'].widget.attrs.update({'class' : 'form-control'})
		self.fields['pos_vert_per'].widget.attrs.update({'class' : 'form-control'})
		self.fields['ob_pos_vert_per'].widget.attrs.update({'class' : 'form-control'})
		self.fields['post_vert_cent'].widget.attrs.update({'class' : 'form-control'})
		self.fields['ob_post_vert_cent'].widget.attrs.update({'class' : 'form-control'})

class addhistoria_procedimientosForm(forms.ModelForm):
	class Meta:
		model   = historia_procedimientos
		exclude = {'orden','paciente','procedimiento','diagnostico','diagnostico1','complicacion',}

	def __init__(self, *args, **kwargs):
		super(addhistoria_procedimientosForm, self).__init__(*args, **kwargs)
		self.fields['hallazgos'].widget.attrs.update({'class' : 'form-control','rows' : '12'})
		self.fields['impresion'].widget.attrs.update({'class' : 'form-control','rows' : '3'})
		self.fields['remision'].widget.attrs.update({'class' : 'form-control','rows' : '3'})
		self.fields['ambito'].widget.attrs.update({'class' : 'form-control'})
		self.fields['finalidad'].widget.attrs.update({'class' : 'form-control'})	
		self.fields['personal'].widget.attrs.update({'class' : 'form-control'})	
		self.fields['forma'].widget.attrs.update({'class' : 'form-control'})		

class addposologiaForm(forms.ModelForm):
	class Meta:
		model   = posologias
		exclude = {'orden',}

	def __init__(self, *args, **kwargs):
		super(addposologiaForm, self).__init__(*args, **kwargs)
		self.fields['medicamento'].widget.attrs.update({'class' : 'form-control mayuscula'})
		self.fields['uso'].widget.attrs.update({'class' : 'form-control mayuscula','rows' : '2'})

class addremisionForm(forms.ModelForm):
	class Meta:
		model   = remision
		exclude = {'orden',}

	def __init__(self, *args, **kwargs):
		super(addremisionForm, self).__init__(*args, **kwargs)
		self.fields['ordenado'].widget.attrs.update({'class' : 'form-control mayuscula'})
		self.fields['descripcion_orden'].widget.attrs.update({'class' : 'form-control mayuscula','rows' : '2'})
		self.fields['entidad'].widget.attrs.update({'class' : 'form-control'})

class addremisionlabForm(forms.ModelForm):
	class Meta:
		model   = remisionlab
		exclude = {'orden',}

	def __init__(self, *args, **kwargs):
		super(addremisionlabForm, self).__init__(*args, **kwargs)
		self.fields['laboratorio'].widget.attrs.update({'class' : 'form-control mayuscula'})

class fechaRipsForm(forms.Form):
    fechai = forms.DateField(label='Fecha Inicial', required=True)
    fechaf = forms.DateField(label='Fecha Final', required=True)
    fecha_r = forms.DateField(label='Fecha Remision', required=True)

    def __init__(self, *args, **kwargs):
		super(fechaRipsForm, self).__init__(*args, **kwargs)
		self.fields['fechai'].widget.attrs.update({'class' : 'form-control', 'placeholder':'aaaa-mm-dd'})
		self.fields['fechaf'].widget.attrs.update({'class' : 'form-control', 'placeholder':'aaaa-mm-dd'})
		self.fields['fecha_r'].widget.attrs.update({'class' : 'form-control', 'placeholder':'aaaa-mm-dd'})															