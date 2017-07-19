# -*- coding: utf-8 -*- 
from reportlab.lib.enums import TA_JUSTIFY,TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from reportlab.lib import colors
from mysite.apps.historias.models import orden,historia_clinica,ordenesProducto
from mysite.apps.datos.models import medico
from mysite.apps.organizaciones.models import instituciones
from mysite.settings import MEDIA_URL

PAGE_HEIGHT=defaultPageSize[1]/2
PAGE_WIDTH=defaultPageSize[0]
pagina_alto = defaultPageSize[1]
pagina_ancho = defaultPageSize[0]
t_orden = None
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
raya = "_____________________________________________________________________________________________"
rayaOrden = "___________________________________________________________________________________________________________________"

def myFirstPage(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Bold',16)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, doc.titulo)
    canvas.setFont('Times-Bold',10)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-126, doc.nit)
    canvas.drawString(inch, PAGE_HEIGHT-150, "Orden No: %s" % doc.no_orden)
    canvas.drawString(4.5*inch, PAGE_HEIGHT-150, "Fecha Orden: %s" % doc.fecha)
    canvas.drawString(inch, PAGE_HEIGHT-168, "Paciente: %s" % doc.cedula)
    canvas.drawString(4.5*inch, PAGE_HEIGHT-168, "Empresa: %s" % doc.empresa)
    canvas.drawString(inch, PAGE_HEIGHT-186, "Procedimiento: %s" % doc.procedimiento)
    canvas.drawString(inch, PAGE_HEIGHT-196, raya)
    canvas.setFont('Times-Roman',9)
    canvas.drawString(inch, 0.75 * inch,"%s / %s" % (doc.pageinfo,doc.telefono))
    canvas.drawString(4.5*inch, 0.75 * inch,"Generada por: %s" % doc.generadapor)
    canvas.restoreState()
    
def myLaterPages(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman', 8)
    pageinfo = "Gretel"
    canvas.drawString(inch, 0.75 * inch,"Page %d %s" % (doc.page, pageinfo))
    canvas.restoreState()

class ImprimeRecibo(SimpleDocTemplate):
	def __init__(self, filename, titulo, nit, no_orden, pageinfo, telefono, fecha, cedula, procedimiento, empresa, cancela, particular, sala, generadapor, **kw):
		SimpleDocTemplate.__init__(self, filename, pagesize=(612.0, 366.0), **kw)

		self.titulo = titulo
		self.nit = nit
		self.no_orden = no_orden
		self.pageinfo = pageinfo
		self.telefono = telefono
		self.fecha = fecha
		self.cedula = cedula
		self.procedimiento = procedimiento
		self.empresa = empresa
		self.generadapor = generadapor
		suma_total = cancela + particular + sala

		Story = [Spacer(1,1.1*inch)]
		style = styles["Normal"]  #Normal
		style.fontSize = 9

		t_orden = orden.objects.get(pk = no_orden)
		ordenes = ordenesProducto.objects.filter(orden = t_orden)
		servicios = ""
		for t in ordenes:
			servicios = "%s %s |" % (servicios,t.servicio.nombre)

		bogustext = ("%s" % servicios)
		style.fontName = 'Helvetica'
		p = Paragraph(bogustext, style)
		Story.append(p)
		Story.append(Spacer(1,0.2*inch))

		Story.append(Spacer(1,0.2*inch))

		self.build(Story, onFirstPage=myFirstPage, onLaterPages=myLaterPages)

def encabezado(canvas, doc):
	canvas.saveState()
	if doc.has_logo:
		canvas.drawImage(doc.logo.path, inch, pagina_alto-260, width=6.5*inch,height=2*inch,mask=None)
	else:	
		canvas.setFont('Times-Bold',18)
		canvas.drawCentredString(pagina_ancho/2.0, pagina_alto-180, doc.institucion)
		canvas.setFont('Times-Roman',11)
		canvas.drawCentredString(pagina_ancho/2.0, pagina_alto-190, "%s / %s" % (doc.direccion,doc.telefono))
		canvas.drawCentredString(pagina_ancho/2.0, pagina_alto-200, "BARRANQUILLA - COLOMBIA")

	#canvas.setFont('Times-Bold',16)
	#if doc.primera_vez:
	#	canvas.drawCentredString(pagina_ancho/2.0, pagina_alto-250, "HISTORIA CLINICA")
	#else:
	#	canvas.drawCentredString(pagina_ancho/2.0, pagina_alto-250, "HISTORIA CLINICA DE EVOLUCION")	

	canvas.setFont('Times-Bold',10)
	canvas.drawString(inch, pagina_alto-195, raya)
	canvas.drawString(inch, pagina_alto-210, "Nombres: %s" % doc.paciente)
	canvas.drawString(6*inch, pagina_alto-210, "Historia #: %s" % doc.no_orden)

	canvas.drawString(inch, pagina_alto-222, "Empresa: %s" % doc.empresa)
	canvas.drawString(6*inch, pagina_alto-222, "Edad: %s" % doc.edad)

	canvas.drawString(inch, pagina_alto-234, "Fecha: %s" % doc.fecha)
	canvas.drawString(6*inch, pagina_alto-234, "Genero: %s" % doc.genero)

	canvas.drawString(inch, pagina_alto-246, u"Cargo a Desempeñar: %s" % doc.cargo)

	canvas.drawString(inch, pagina_alto-252, raya)
	canvas.restoreState()

	'''
	canvas.setFont('Times-Bold',10)
	canvas.drawString(inch, pagina_alto-255, raya)
	canvas.drawString(inch, pagina_alto-270, "Nombres: %s" % doc.paciente)
	canvas.drawString(6*inch, pagina_alto-270, "Historia #: %s" % doc.no_orden)

	canvas.drawString(inch, pagina_alto-282, "Empresa: %s" % doc.empresa)
	canvas.drawString(6*inch, pagina_alto-282, "Edad: %s" % doc.edad)

	canvas.drawString(inch, pagina_alto-294, "Fecha: %s" % doc.fecha)
	canvas.drawString(6*inch, pagina_alto-294, "Genero: %s" % doc.genero)

	canvas.drawString(inch, pagina_alto-306, u"Cargo a Desempeñar: %s" % doc.cargo)

	canvas.drawString(inch, pagina_alto-312, raya)
	canvas.restoreState()
	'''
    
def cuerpo(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman', 8)
    canvas.drawString(inch, 0.75 * inch,"Pagina %d.  Historia #: %s.  Paciente: %s." % (doc.page, doc.no_orden, doc.paciente))
    canvas.restoreState()

class ImprimeHistoria(SimpleDocTemplate):
	def __init__(self, filename, no_orden, **kw):
		SimpleDocTemplate.__init__(self, filename, pagesize=(612.0, 732.0), **kw)

		ips = instituciones.objects.get(pk='1')

		t_orden = orden.objects.get(pk = no_orden)
		h = historia_clinica.objects.get(orden = t_orden)
		self.no_orden = h.id
		self.institucion = ips.razon
		self.direccion = ips.direccion
		self.telefono = ips.telefono
		self.empresa = t_orden.empresa.razon
		self.edad = t_orden.paciente.edad
		self.fecha = t_orden.fecha_atencion
		self.paciente = t_orden.paciente
		self.genero = t_orden.paciente.genero
		self.primera_vez = h.primera_vez
		self.cargo = t_orden.cargo

		if ips.logo_historia != "":
			self.has_logo = True
			self.logo = ips.logo_historia
		else:
			self.has_logo = False
			self.logo = ""			

		Story = [Spacer(1,1.2*inch)]

		style = styles["Normal"]  #Normal
		style.fontSize = 9
		style.fontName = 'Helvetica'

		bogustext = ("<strong>FECHA DE NACIMIENTO:</strong> %s" % h.paciente.fecha_nacimiento)
		p = Paragraph(bogustext, styles["Justify"])
		Story.append(p)
		Story.append(Spacer(1,0.08*inch))

		bogustext = ("<strong>EXAMEN DE:</strong> %s" % t_orden.get_examen_display())
		p = Paragraph(bogustext, styles["Justify"])
		Story.append(p)
		Story.append(Spacer(1,0.08*inch))

		bogustext = ("<strong>ESCALONARIDAD:</strong> %s" % h.paciente.get_escolaridad_display())
		p = Paragraph(bogustext, styles["Justify"])
		Story.append(p)
		Story.append(Spacer(1,0.08*inch))

		bogustext = ("<strong>ESTADO CIVIL:</strong> %s" % h.paciente.get_estadoCivil_display())
		p = Paragraph(bogustext, styles["Justify"])
		Story.append(p)
		Story.append(Spacer(1,0.08*inch))

		bogustext = ("<strong>DATOS DE CONTACTO:</strong> DIRECCION: %s , BARRIO: ,"
					" CIUDAD: %s, DEPARTAMENTO: %s, ESTRATO: "
					% (h.paciente.direccion,h.paciente.ciudad,h.paciente.ciudad.nombre_depto))
		p = Paragraph(bogustext, styles["Justify"])
		Story.append(p)
		Story.append(Spacer(1,0.08*inch))

		bogustext = ("<strong>INFORMACION DEL ASPIRANTE:</strong> HIJOS: %s , NUMERO DE HIJOS: %s,"
					" CARGO: %s, SECCION: %s, TURNO: %s, ACTIVIDAD: %s"
					% (h.get_hijos_display(),h.num_hijos,t_orden.cargo,t_orden.seccion,h.get_turno_display(),h.get_actividad_display()))
		p = Paragraph(bogustext, styles["Justify"])
		Story.append(p)
		Story.append(Spacer(1,0.08*inch))

		if h.a_empresa1 != "":
			bogustext = ("<strong>ANTECEDENTES DE TRABAJO U OFICIO:</strong> EMPRESA: %s , OCUPACION: %s,"
					" TIEMPO: %s, R.BIOLOG: %s, R.MECAN: %s, R.FISICO: %s, R.ERGON: %s, R.PSICOL: %s,"
					" R.QUIMICO: %s, PROTECCION EMPLEADA: %s"
					% (h.a_empresa1,h.a_ocupacion1,h.a_tiempo1,h.get_a_biolog1_display(),h.get_a_mec1_display(),h.get_a_fis1_display(),h.get_a_erg1_display(),h.get_a_psi1_display(),h.get_a_qui1_display(),h.get_a_prot1_display()))
			p = Paragraph(bogustext, styles["Justify"])
			Story.append(p)
			Story.append(Spacer(1,0.08*inch))

		if h.a_empresa2 != "":
			bogustext = ("<strong>ANTECEDENTES DE TRABAJO U OFICIO:</strong> EMPRESA: %s , OCUPACION: %s,"
					" TIEMPO: %s, R.BIOLOG: %s, R.MECAN: %s, R.FISICO: %s, R.ERGON: %s, R.PSICOL: %s,"
					" R.QUIMICO: %s, PROTECCION EMPLEADA: %s"
					% (h.a_empresa2,h.a_ocupacion2,h.a_tiempo2,h.get_a_biolog2_display(),h.get_a_mec2_display(),h.get_a_fis2_display(),h.get_a_erg2_display(),h.get_a_psi2_display(),h.get_a_qui2_display(),h.get_a_prot2_display()))
			p = Paragraph(bogustext, styles["Justify"])
			Story.append(p)
			Story.append(Spacer(1,0.08*inch))	

		bogustext = ("<strong>ACCIDENTE DE TRABAJO:</strong> ACCIDENTES: %s , ENFERMEDAD PROFESIONAL: %s. <strong>OBSERVACIONES:</strong> %s"
					% (h.get_accidente_display(),h.get_enfermedad_profesional_display(),h.detalle))
		p = Paragraph(bogustext, styles["Justify"])
		Story.append(p)
		Story.append(Spacer(1,0.08*inch))

		bogustext = ("<strong>ANTECEDENTES PATOLOGICOS PERSONALES:</strong> CIRUGIA: %s , HOSPITALIZACION: %s,"
					" FRACTURAS: %s, TABAQUISMO: %s, INTOXICACIONES: %s, ALCOHOLISMO: %s, MENTALES: %s, ASMA: %s,"
					" TBC: %s, ALERGIAS: %s, GRIPAS: %s, ENFERMEDADES DE LA PIEL: %s, OTOLOGICOS: %s, DIABETES: %s,"
					" HEMATOLOGICOS: %s, EPILEPSIA: %s, CANCER: %s, HIPERTENSION: %s, OTROS: %s"
					% (h.get_quirurgicos_display(),h.get_hospitalizacion_display(),h.get_fracturas_display(),h.get_tabaquismo_display(),h.get_intoxicaciones_display(),h.get_alcoholismo_display(),h.get_mentales_display(),h.get_asma_display(),h.get_tbc_display(),h.get_alergias_display(),h.get_gripas_display(),h.get_enf_piel_display(),h.get_otologicos_display(),h.get_diabetes_display(),h.get_hematologicos_display(),h.get_epilepsia_display(),h.get_cancer_display(),h.get_hipertension_display(),h.get_otros_display()))
		p = Paragraph(bogustext, styles["Justify"])
		Story.append(p)
		Story.append(Spacer(1,0.08*inch))

		bogustext = ("<strong>ANTECEDENTES PATOLOGICOS FAMILIARES:</strong> CIRUGIA: %s , HOSPITALIZACION: %s,"
					" FRACTURAS: %s, TABAQUISMO: %s, INTOXICACIONES: %s, ALCOHOLISMO: %s, MENTALES: %s, ASMA: %s,"
					" TBC: %s, ALERGIAS: %s, GRIPAS: %s, ENFERMEDADES DE LA PIEL: %s, OTOLOGICOS: %s, DIABETES: %s,"
					" HEMATOLOGICOS: %s, EPILEPSIA: %s, CANCER: %s, HIPERTENSION: %s, OTROS: %s"
					% (h.get_f_quirurgicos_display(),h.get_f_hospitalizacion_display(),h.get_f_fracturas_display(),h.get_f_tabaquismo_display(),h.get_f_intoxicaciones_display(),h.get_f_alcoholismo_display(),h.get_f_mentales_display(),h.get_f_asma_display(),h.get_f_tbc_display(),h.get_f_alergias_display(),h.get_f_gripas_display(),h.get_f_enf_piel_display(),h.get_f_otologicos_display(),h.get_f_diabetes_display(),h.get_f_hematologicos_display(),h.get_f_epilepsia_display(),h.get_f_cancer_display(),h.get_f_hipertension_display(),h.get_f_otros_display()))
		p = Paragraph(bogustext, styles["Justify"])
		Story.append(p)
		Story.append(Spacer(1,0.08*inch))

		if h.descripcion_antecedente != "":
			bogustext = ("<strong>DESCRIPCION ANTECEDENTES PATOLOGICOS FAMILIARES Y PERSONALES:</strong> %s"
						% (h.descripcion_antecedente))
			p = Paragraph(bogustext, styles["Justify"])
			Story.append(p)
			Story.append(Spacer(1,0.08*inch))
		else:
			bogustext = ("<strong>DESCRIPCION ANTECEDENTES PATOLOGICOS FAMILIARES Y PERSONALES:</strong> Ninguna")
			p = Paragraph(bogustext, styles["Justify"])
			Story.append(p)
			Story.append(Spacer(1,0.08*inch))			


		bogustext = ("<strong>HABITOS:</strong> ALCOHOL: %s , DEPORTES: %s, FRECUENCIA: %s"
					% (h.get_alcohol_display(),h.get_deportes_display(),h.frecuencia))
		p = Paragraph(bogustext, styles["Justify"])
		Story.append(p)
		Story.append(Spacer(1,0.08*inch))

		if t_orden.paciente.genero == 'F':
			bogustext = ("<strong>ANTECEDENTES GINECO-OBSTETRICOS:</strong> MENARQUIA: %s , CICLOS: %s,"
					" GRAVIDA: %s, PARTOS: %s, ABORTOS: %s, CESAREAS: %s, FUM: %s, FUP: %s,"
					" DISMENORREA: %s, METRORRAGIAS: %s, TRASTORNOS DEL CICLO: %s, CITOLOGIAS: %s, OTROS TRANSTORNOS: %s,"
					" METODOS DE PLANIFICACION: %s"
					% (h.menarquia,h.ciclos,h.gravida,h.partos,h.abortos,h.cesareas,h.fum,h.fup,h.dismenorrea,h.metrorragias,h.trastorno_ciclo,h.citologias,h.transtorno_otros,h.planificacion))
			p = Paragraph(bogustext, styles["Justify"])
			Story.append(p)
			Story.append(Spacer(1,0.08*inch))

		if h.sintomas != '':	
			bogustext = ("<strong>REVISION DE SINTOMAS POR SISTEMAS:</strong> %s" % h.sintomas)
			p = Paragraph(bogustext, styles["Justify"])
			Story.append(p)
			Story.append(Spacer(1,0.08*inch))

		bogustext = ("<strong>SIGNOS VITALES:</strong> PA (mmHg): %s ,"
			" T (C): %s, TALLA (Cm): %s, PESO (Kg): %s, PULSO (min): %s, MASA CORP (Kg/mt2): %s"
			% (h.presion_arterial,h.temperatura,h.talla,h.peso,
				h.pulso,h.masa_corporal))
		p = Paragraph(bogustext, styles["Justify"])
		Story.append(p)
		Story.append(Spacer(1,0.08*inch))

		bogustext = ("<strong>ESTADO GENERAL:</strong> %s, HABILIDAD PARA ESCRIBIR: %s"
			% (h.get_estado_display(),h.get_escribe_display()))
		p = Paragraph(bogustext, styles["Justify"])
		Story.append(p)
		Story.append(Spacer(1,0.08*inch))

		bogustext = ("<strong>EXPLORACION OSEA MUSCULAR:</strong> CABEZA: %s ,"
			" CUELLO: %s, TORAX: %s, ABDOMEN: %s, COLUMNA CERVICAL: %s, COLUMNA DORSAL: %s, COLUMNA LUMBOSACRA: %s, MIEMBROS SUPERIORES: %s, MIEMBROS INFERIORES: %s"
			% (h.get_cabeza_display(),h.get_cuello_display(),h.get_torax_display(),h.get_abdomen_display(),
				h.get_columna_cervical_display(),h.get_columna_dorsal_display(),h.get_columna_lumbo_display(),h.get_m_superiores_display(),h.get_m_inferiores_display()))
		p = Paragraph(bogustext, styles["Justify"])
		Story.append(p)
		Story.append(Spacer(1,0.08*inch))


		if h.descripcion_osteomuscular != "":
			bogustext = ("<strong>OBSERVACIONES:</strong> %s"
						% (h.descripcion_osteomuscular))
			p = Paragraph(bogustext, styles["Justify"])
			Story.append(p)
			Story.append(Spacer(1,0.08*inch))
		else:
			bogustext = ("<strong>OBSERVACIONES:</strong> Ninguna")
			p = Paragraph(bogustext, styles["Justify"])
			Story.append(p)
			Story.append(Spacer(1,0.08*inch))	


		Story.append(Spacer(1,0.08*inch))
		Story.append(Spacer(1,0.08*inch))
		Story.append(Spacer(1,0.08*inch))

		bogustext = ("<strong>DINAMICA (MOVIMIENTOS ARTICULARES)</strong>")
		p = Paragraph(bogustext, styles["Center"])
		Story.append(p)
		Story.append(Spacer(1,0.08*inch))

		bogustext = ("<strong>CUELLO:</strong> %s. OBSERVACIONES: %s "
			% (h.get_d_cuello_display(),h.d_cuello_o))
		p = Paragraph(bogustext, styles["Justify"])
		Story.append(p)
		Story.append(Spacer(1,0.08*inch))

		bogustext = ("<strong>HOMBROS:</strong> %s. OBSERVACIONES: %s "
			% (h.get_d_hombros_display(),h.d_hombros_o))
		p = Paragraph(bogustext, styles["Justify"])
		Story.append(p)
		Story.append(Spacer(1,0.08*inch))

		bogustext = ("<strong>CODO:</strong> %s. OBSERVACIONES: %s "
			% (h.get_d_codo_display(),h.d_codo_o))
		p = Paragraph(bogustext, styles["Justify"])
		Story.append(p)
		Story.append(Spacer(1,0.08*inch))

		cadena = u"MUÑECA"
		bogustext = ("<strong>%s:</strong> %s. OBSERVACIONES: %s "
			% (cadena,h.get_d_muneca_display(),h.d_muneca_o))
		p = Paragraph(bogustext, styles["Justify"])
		Story.append(p)
		Story.append(Spacer(1,0.08*inch))

		bogustext = ("<strong>CADERA:</strong> %s. OBSERVACIONES: %s "
			% (h.get_d_cadera_display(),h.d_cadera_o))
		p = Paragraph(bogustext, styles["Justify"])
		Story.append(p)
		Story.append(Spacer(1,0.08*inch))

		bogustext = ("<strong>RODILLA:</strong> %s. OBSERVACIONES: %s "
			% (h.get_d_rodilla_display(),h.d_rodilla_o))
		p = Paragraph(bogustext, styles["Justify"])
		Story.append(p)
		Story.append(Spacer(1,0.08*inch))

		bogustext = ("<strong>TOBILLO:</strong> %s. OBSERVACIONES: %s "
			% (h.get_d_tobillo_display(),h.d_tobillo_o))
		p = Paragraph(bogustext, styles["Justify"])
		Story.append(p)
		Story.append(Spacer(1,0.08*inch))

		bogustext = ("<strong>ORGANOS O SISTEMAS:</strong> CICATRICES: %s, PIEL: %s, CRANEO: %s "
			% (h.get_cicatrices_display(),	h.get_piel_display(), h.get_craneo_display()))
		p = Paragraph(bogustext, styles["Justify"])
		Story.append(p)
		Story.append(Spacer(1,0.08*inch))

		bogustext = ("<strong>OJOS:</strong> CONJUNTIVAS: %s, PUPILAS: %s, ANEXOS: %s, REFLEJOS: %s, FONDO: %s "
			% (h.get_conjuntivas_display(),h.get_pupilas_display(),h.get_anexos_display(),
			 h.get_reflejos_display(),h.get_fondo_display()))
		p = Paragraph(bogustext, styles["Justify"])
		Story.append(p)
		Story.append(Spacer(1,0.08*inch))

		bogustext = ("<strong>OIDOS:</strong> PABELLONES: %s, OSTOCOPIA: %s"
			% (h.get_pabellones_display(),	h.get_ostocopia_display()))
		p = Paragraph(bogustext, styles["Justify"])
		Story.append(p)
		Story.append(Spacer(1,0.08*inch))

		bogustext = ("<strong>NARIZ:</strong> TABIQUE: %s, CORNETES: %s"
			% (h.get_tabique_display(),h.get_cornetes_display()))
		p = Paragraph(bogustext, styles["Justify"])
		Story.append(p)
		Story.append(Spacer(1,0.08*inch))

		bogustext = ("<strong>BOCA:</strong> LABIOS-LENGUA: %s, FARINGEAMIGDALAS: %s"
			% (h.get_labios_display(),	h.get_faringe_display()))
		p = Paragraph(bogustext, styles["Justify"])
		Story.append(p)
		Story.append(Spacer(1,0.08*inch))

		bogustext = ("<strong>TORAX:</strong> CUELLO-TIROIDES: %s, TORAX: %s, PULMONES: %s, CORAZON: %s"
			% (h.get_tiroides_display(),h.get_o_torax_display(),h.get_pulmones_display(),h.get_corazon_display()))
		p = Paragraph(bogustext, styles["Justify"])
		Story.append(p)
		Story.append(Spacer(1,0.08*inch))

		bogustext = ("<strong>ABDOMEN:</strong> PARED: %s, VISERAS (MEGALIAS): %s, HERNIAS: %s, "
			"GENITALES EXTERNOS: %s, VASCULAR PERIFERICO: %s"
			% (h.get_pared_display(),h.get_viseras_display(),h.get_hernias_display(),h.get_genitales_display(),h.get_vascular_display()))
		p = Paragraph(bogustext, styles["Justify"])
		Story.append(p)
		Story.append(Spacer(1,0.08*inch))

		bogustext = ("<strong>SISTEMA NERVIOSO:</strong> REFLEJOS: %s, MARCHA: %s, COORDINACION: %s"
			% (h.get_o_reflejos_display(),	h.get_marcha_display(),	h.get_coordinacion_display()))
		p = Paragraph(bogustext, styles["Justify"])
		Story.append(p)
		Story.append(Spacer(1,0.08*inch))

		bogustext = ("<strong>SISTEMA CIRCULATORIO:</strong> RUIDOS CARDIACOS: %s, EXTRASISTOLES: %s, "
			"FIBRILACION: %s, SOPLOS: %s, SISTOLICOS: %s, DIASTOLICOS: %s, PRESISTOLICOS: %s, "
			"VASOS PERIFERICOS (RADIAL, DORSAL, PIE, TIBIA, POSTERIOR): %s, VARICES (GRADOS): %s, OBSERVACIONES ADICIONALES: %s"
			% (h.get_ruidos_display(),h.get_extrasistoles_display(),h.get_fibrilacion_display(),h.get_soplos_display(),h.get_sistolicos_display(),h.get_diastolicos_display(),	
				h.get_presistolicos_display(),h.get_vasos_display(),h.get_varices_display(),h.observaciones))
		p = Paragraph(bogustext, styles["Justify"])
		Story.append(p)
		Story.append(Spacer(1,0.08*inch))

		bogustext = ("<strong>SIGNOS CLINICOS DEL TUNEL CARPIANO:</strong> %s" % (h.tunel))
		p = Paragraph(bogustext, styles["Justify"])
		Story.append(p)
		Story.append(Spacer(1,0.08*inch))

		bogustext = ("<strong>PHANNEL:</strong> %s. <strong>TINNEL:</strong> %s." % (h.get_phannel_display(), h.get_tinnel_display()))
		p = Paragraph(bogustext, styles["Justify"])
		Story.append(p)
		Story.append(Spacer(1,0.08*inch))

		if h.f_imagen != None:
			bogustext = ("<strong>IMAGENOLOGIA (RX):</strong> FECHA: %s, RESULTADOS: %s." % (h.f_imagen, h.r_imagen))
			p = Paragraph(bogustext, styles["Justify"])
			Story.append(p)
			Story.append(Spacer(1,0.08*inch))

		if h.f_audiometria != None:
			bogustext = ("<strong>AUDIOMETRIA:</strong> FECHA: %s, RESULTADOS: %s." % (h.f_audiometria, h.r_audiometria))
			p = Paragraph(bogustext, styles["Justify"])
			Story.append(p)
			Story.append(Spacer(1,0.08*inch))
			
		if h.f_visiometria != None:
			bogustext = ("<strong>VISIOMETRIA:</strong> FECHA: %s, RESULTADOS: %s." % (h.f_visiometria, h.r_visiometria))
			p = Paragraph(bogustext, styles["Justify"])
			Story.append(p)
			Story.append(Spacer(1,0.08*inch))

		if h.f_espirometria != None:
			bogustext = ("<strong>ESPIROMETRIA:</strong> FECHA: %s, RESULTADOS: %s." % (h.f_espirometria, h.r_espirometria))
			p = Paragraph(bogustext, styles["Justify"])
			Story.append(p)
			Story.append(Spacer(1,0.08*inch))

		if h.f_laboratorio != None:
			bogustext = ("<strong>LABORATORIO:</strong> FECHA: %s, RESULTADOS: %s." % (h.f_laboratorio, h.r_laboratorio))
			p = Paragraph(bogustext, styles["Justify"])
			Story.append(p)
			Story.append(Spacer(1,0.08*inch))				
	
		bogustext = ("<strong>CONCEPTO MEDICO:</strong> %s" % h.get_concepto_display())
		p = Paragraph(bogustext, styles["Justify"])
		Story.append(p)
		Story.append(Spacer(1,0.08*inch))


		if h.recomendacion != "":
			bogustext = ("<strong>RECOMENDACIONES:</strong> %s"
						% (h.recomendacion))
			p = Paragraph(bogustext, styles["Justify"])
			Story.append(p)
			Story.append(Spacer(1,0.08*inch))
		else:
			bogustext = ("<strong>RECOMENDACIONES:</strong> Ninguna")
			p = Paragraph(bogustext, styles["Justify"])
			Story.append(p)
			Story.append(Spacer(1,0.08*inch))	


		bogustext = ("<strong>REMITIR A:</strong> %s" % h.get_remitir_display())
		p = Paragraph(bogustext, styles["Justify"])
		Story.append(p)
		Story.append(Spacer(1,0.08*inch))

		Story.append(Spacer(1,0.5*inch))

		if t_orden.medico.especialidad.id == 164 or t_orden.medico.especialidad.id == 165:
			doctor = t_orden.medico
		else:
			doctor = medico.objects.get(cedula='8701712')
		
		Story.append(Spacer(1,0.3*inch))

		if doctor.imagen != "":
			im = Image(doctor.imagen, width=2.3*inch, height=0.5*inch)
			im.hAlign = 'LEFT'
			Story.append(im)		


		Story.append(Spacer(1,0.1*inch))
		bogustext = ("<strong>Dr. %s %s %s </strong>" % (doctor.nombre,doctor.papellido,doctor.sapellido))
		p = Paragraph(bogustext, style)
		Story.append(p)

		Story.append(Spacer(1,0.01*inch))
		bogustext = ("<strong>Médico General</strong>")
		p = Paragraph(bogustext, style)
		Story.append(p)

		Story.append(Spacer(1,0.01*inch))
		bogustext = ("<strong>Especialista en: %s</strong>" % doctor.especialidad)
		p = Paragraph(bogustext, style)
		Story.append(p)	

		Story.append(Spacer(1,0.01*inch))
		bogustext = ("<strong>%s</strong>" % doctor.registro)
		p = Paragraph(bogustext, style)
		Story.append(p)

		Story.append(Spacer(1,0.8*inch))

		if t_orden.paciente.firma != "":
			im = Image(t_orden.paciente.firma, width=2.3*inch, height=0.5*inch)
			im.hAlign = 'LEFT'
			Story.append(im)

		Story.append(Spacer(1,0.08*inch))
		bogustext = ("<strong>%s %s %s %s</strong>" % (t_orden.paciente.pnombre,t_orden.paciente.snombre,t_orden.paciente.papellido,t_orden.paciente.sapellido))
		p = Paragraph(bogustext, style)
		Story.append(p)
		Story.append(Spacer(1,0.03*inch))
		bogustext = ("FIRMA DEL TRABAJADOR")
		p = Paragraph(bogustext, style)
		Story.append(p)
		Story.append(Spacer(1,0.03*inch))

		self.build(Story, onFirstPage=encabezado, onLaterPages=cuerpo)		


def encabezadoConcepto(canvas, doc):
	canvas.saveState()
	if doc.has_logo:
		canvas.drawImage(doc.logo.path, inch, pagina_alto-260, width=6.5*inch,height=2*inch,mask=None)
	else:	
		canvas.setFont('Times-Bold',18)
		canvas.drawCentredString(pagina_ancho/2.0, pagina_alto-180, doc.institucion)
		canvas.setFont('Times-Roman',11)
		canvas.drawCentredString(pagina_ancho/2.0, pagina_alto-190, "%s / %s" % (doc.direccion,doc.telefono))
		canvas.drawCentredString(pagina_ancho/2.0, pagina_alto-200, "BARRANQUILLA - COLOMBIA")

	if doc.has_foto:
		canvas.drawImage(doc.foto.path, 6*inch, pagina_alto-420, width=1.3*inch,height=1.3*inch,mask=None)

	canvas.setFont('Times-Bold',10)

	canvas.drawString(inch, pagina_alto-210, "FECHA: %s" % doc.fecha)
	canvas.drawString(4*inch, pagina_alto-210, "CIUDAD: %s" % doc.ciudad)

	canvas.roundRect(3*inch, pagina_alto-245, 0.5*inch, 0.23*inch, 5, stroke=1, fill=0)
	canvas.roundRect(4.5*inch, pagina_alto-245, 0.5*inch, 0.23*inch, 5, stroke=1, fill=0)
	canvas.roundRect(6.18*inch, pagina_alto-245, 0.5*inch, 0.23*inch, 5, stroke=1, fill=0)
	canvas.roundRect(3*inch, pagina_alto-270, 0.5*inch, 0.23*inch, 5, stroke=1, fill=0)

	if doc.examen == '1': #Pre-empleo
		canvas.drawString(inch, pagina_alto-240, "EXAMEN MEDICO:  EGRESO   %s" % "      ")
		canvas.drawString(3.8*inch, pagina_alto-240, "INGRESO   %s" % "     X")
		canvas.drawString(5.3*inch, pagina_alto-240, "PERIODICO   %s" % "      ")
		canvas.drawString(2.37*inch, pagina_alto-265, "OTRO   %s" % "          ")	
	elif doc.examen == '2': #Periodico
		canvas.drawString(inch, pagina_alto-240, "EXAMEN MEDICO:  EGRESO   %s" % "      ")
		canvas.drawString(3.8*inch, pagina_alto-240, "INGRESO   %s" % "      ")
		canvas.drawString(5.3*inch, pagina_alto-240, "PERIODICO   %s" % "     X")
		canvas.drawString(2.37*inch, pagina_alto-265, "OTRO   %s" % "          ")
	elif doc.examen == '3': #Retiro
		canvas.drawString(inch, pagina_alto-240, "EXAMEN MEDICO:  EGRESO   %s" % "     X")
		canvas.drawString(3.8*inch, pagina_alto-240, "INGRESO   %s" % "      ")
		canvas.drawString(5.3*inch, pagina_alto-240, "PERIODICO   %s" % "      ")
		canvas.drawString(2.37*inch, pagina_alto-265, "OTRO   %s" % "          ")
	else:	#Otros
		canvas.drawString(inch, pagina_alto-240, "EXAMEN MEDICO:  EGRESO   %s" % "      ")
		canvas.drawString(3.8*inch, pagina_alto-240, "INGRESO   %s" % "      ")
		canvas.drawString(5.3*inch, pagina_alto-240, "PERIODICO   %s" % "      ")
		canvas.drawString(2.37*inch, pagina_alto-265, "OTRO   %s" % "         X")

	canvas.drawString(3.8*inch, pagina_alto-265, "Cual %s" % "_____________________________________")

	canvas.drawString(inch, pagina_alto-300, u"Me permito certificar que el señor (a): %s" % doc.nombre)
	canvas.drawString(inch, pagina_alto-320, u"Cargo: %s" % doc.cargo )
	canvas.drawString(4*inch, pagina_alto-320, u"Empresa: %s" % doc.empresa )
	canvas.drawString(inch, pagina_alto-340, u"Cliente: %s" % doc.cliente )
	canvas.drawString(inch, pagina_alto-360, u"Identificado con cédula de ciudadanía: %s" % doc.cedula )

	if doc.servicios == "":
		canvas.drawString(inch, pagina_alto-440, u"Una vez practicado el %s: " % doc.enfasis)
	else:
		canvas.drawString(inch, pagina_alto-440, u"Una vez practicado el %s y los siguientes paraclinicos:" % doc.enfasis)
	
	canvas.setFont('Times-Roman',9)
	canvas.drawString(inch, 0.7 * inch,"IPS SIOM")
	canvas.drawString(inch, 0.5 * inch,"Services Integral Occupational Medical. Carrera 48 N° 74 - 156 Loc. 03 Edificio Valentina. Tel: 3688151, Cel: 3013205553 - 3042054787")

	canvas.restoreState()
    
def cuerpoConcepto(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman', 8)
    canvas.drawString(inch, 0.75 * inch,"Pagina %d.  Historia #: %s.  Paciente: %s." % (doc.page, doc.no_orden, doc.paciente))
    canvas.restoreState()

class ImprimeConcepto(SimpleDocTemplate):
	def __init__(self, filename, no_orden, **kw):
		SimpleDocTemplate.__init__(self, filename, pagesize=(612.0, 732.0), **kw)

		ips = instituciones.objects.get(pk='1')

		t_orden = orden.objects.get(pk = no_orden)
		h = historia_clinica.objects.get(orden = t_orden)
		self.no_orden = h.id
		self.institucion = ips.razon
		self.direccion = ips.direccion
		self.telefono = ips.telefono
		self.empresa = t_orden.empresa.razon
		self.cliente = t_orden.empresa_cliente
		self.nombre = "%s %s %s %s" % (t_orden.paciente.pnombre,t_orden.paciente.snombre,t_orden.paciente.papellido,t_orden.paciente.sapellido)
		self.cedula = t_orden.paciente.cedula

		self.edad = t_orden.paciente.edad
		self.fecha = t_orden.fecha_atencion
		self.paciente = t_orden.paciente
		self.genero = t_orden.paciente.genero
		self.primera_vez = h.primera_vez
		self.cargo = t_orden.cargo
		self.examen = t_orden.examen
		self.ciudad= t_orden.paciente.ciudad

		ordenes = ordenesProducto.objects.filter(orden = t_orden,servicio__nombre__historia = False)
		#hecho 19 septiembre 2016
		enfasis = ordenesProducto.objects.filter(orden = t_orden,servicio__nombre__historia = True).first()
		self.enfasis = enfasis.servicio.nombre
		#fin
		
		style = styles["Normal"]  #Normal
		style.fontSize = 9

		servicios = ""
		for t in ordenes:
			servicios = "%s %s |" % (servicios,t.servicio.nombre)

		self.servicios = servicios	

		if t_orden.paciente.foto != "":
			self.has_foto = True
			self.foto = t_orden.paciente.foto
		else:
			self.has_foto = False
			self.foto = ""	

		v_concepto = h.concepto

		if t_orden.examen_adicional == '1': #Altura
			if ips.altura != "":
				self.has_logo = True
				self.logo = ips.altura
			else:
				self.has_logo = False
				self.logo = ""		
		elif t_orden.examen_adicional == '4': #Alimentos
			if ips.alimentos != "":
				self.has_logo = True
				self.logo = ips.alimentos
			else:
				self.has_logo = False
				self.logo = ""		
		else:	
			if v_concepto == '2':
				if ips.altura != "":
					self.has_logo = True
					self.logo = ips.altura
				else:
					self.has_logo = False
					self.logo = ""	
			elif v_concepto == '3':
				if ips.alimentos != "":
					self.has_logo = True
					self.logo = ips.alimentos
				else:
					self.has_logo = False
					self.logo = ""			
			else:
				if ips.apto != "":
					self.has_logo = True
					self.logo = ips.apto
				else:
					self.has_logo = False
					self.logo = ""					


		Story = [Spacer(1,3.65*inch)]

		style = styles["Normal"]  #Normal
		style.fontSize = 8
		style.fontName = 'Helvetica'

#*********************************************************************************************************
		bogustext = ("%s" % servicios)
		p = Paragraph(bogustext, style)
		Story.append(p)

		style = styles["Normal"]  #Normal
		style.fontSize = 9
		style.fontName = 'Helvetica'

		Story.append(Spacer(1,0.1*inch))
		bogustext = ("<strong>Se encuentra:</strong>")
		p = Paragraph(bogustext, style)
		Story.append(p)		

		style = styles["Normal"]  #Normal
		style.fontSize = 10
		style.fontName = 'Helvetica'

		if v_concepto == '1':
			data = [['APTO','X'],
					]
		elif v_concepto == '2':
			data = [['APTO','X'],
					]
		elif v_concepto == '3':
			data = [['APTO','X'],
					]		
		elif v_concepto == '4':
			data = [['APTO CON RECOMENDACIONES DE SEGUIMIENTO','X'],
					]
		elif v_concepto == '5':
			data = [['APTO CON PATOLOGIA QUE NO INTERFIERE EN EL CARGO','X'],
					]
		elif v_concepto == '6':	
			data = [['APTO CON RESTRICCIONES PARA EL CARGO','X'],
					]		
		else:
			data = [['APLAZADO','X'],
					]	
	
		table = Table(data)
		table_style = [('BACKGROUND', (0,0), (-1,0), None),
		    ('ALIGN', (1,1), (-1,-1), 'CENTER'),
		    ('FONTSIZE', (0,0), (-1, -1), 9),
		    ('GRID', (0,0), (-1,-1), 1, colors.black)]
		table.setStyle(TableStyle(table_style))			
		Story.append(table)

		if t_orden.examen_adicional == '4':
			Story.append(Spacer(1,0.3*inch))
			bogustext = ("Para manipular alimentos y/o productos de aseo, higiene y limpieza de uso doméstico según la resolución 765 de 2010 al examen médico realizado y pruebas complementarias.")
			p = Paragraph(bogustext, style)
			Story.append(p)	

		if h.recomendacion != "":
			Story.append(Spacer(1,0.3*inch))
			bogustext = ("<strong>Recomendaciones:</strong>")
			p = Paragraph(bogustext, style)
			Story.append(p)	

			Story.append(Spacer(1,0.01*inch))
			bogustext = (u"%s" % h.recomendacion)
			p = Paragraph(bogustext, style)
			Story.append(p)

		if h.remitir != "N":
			Story.append(Spacer(1,0.3*inch))
			bogustext = ("<strong>Valoracion por:</strong>")
			p = Paragraph(bogustext, style)
			Story.append(p)	

			Story.append(Spacer(1,0.01*inch))
			bogustext = (u"%s" % h.valoracion)
			p = Paragraph(bogustext, style)
			Story.append(p)			


		if t_orden.medico.especialidad.id == 164 or t_orden.medico.especialidad.id == 165:
			doctor = t_orden.medico
		else:
			doctor = medico.objects.get(cedula='8701712')

		Story.append(Spacer(1,0.3*inch))

		if doctor.imagen != "":
			im = Image(doctor.imagen, width=2.3*inch, height=0.5*inch)
			im.hAlign = 'LEFT'
			Story.append(im)		

		Story.append(Spacer(1,0.1*inch))
		bogustext = ("<strong>Dr. %s %s %s </strong>" % (doctor.nombre,doctor.papellido,doctor.sapellido))
		p = Paragraph(bogustext, style)
		Story.append(p)

		Story.append(Spacer(1,0.01*inch))
		bogustext = ("<strong>Médico General</strong>")
		p = Paragraph(bogustext, style)
		Story.append(p)

		Story.append(Spacer(1,0.01*inch))
		bogustext = ("<strong>Especialista en: %s</strong>" % doctor.especialidad)
		p = Paragraph(bogustext, style)
		Story.append(p)	

		Story.append(Spacer(1,0.01*inch))
		bogustext = ("<strong>%s</strong>" % doctor.registro)
		p = Paragraph(bogustext, style)
		Story.append(p)				
#*********************************************************************************************************
 
		self.build(Story, onFirstPage=encabezadoConcepto, onLaterPages=cuerpoConcepto)		

def encabezadoOrden(canvas, doc):
	canvas.saveState()
	if doc.has_logo:
		canvas.drawImage(doc.logo.path, inch, PAGE_HEIGHT-110, width=6.5*inch,height=0.7*inch,mask=None)
	else:	
		canvas.setFont('Times-Bold',18)
		canvas.drawCentredString(pagina_ancho/2.0, PAGE_HEIGHT-80, doc.institucion)
		canvas.setFont('Times-Roman',11)
		canvas.drawCentredString(pagina_ancho/2.0, PAGE_HEIGHT-90, "%s / %s" % (doc.direccion,doc.telefono))
		canvas.drawCentredString(pagina_ancho/2.0, PAGE_HEIGHT-100, "BARRANQUILLA - COLOMBIA")
	
	margen_izq = inch / 4
	canvas.setFont('Times-Bold',10)
	canvas.drawString(margen_izq, PAGE_HEIGHT-115, rayaOrden)
	canvas.setFont('Times-Bold',9)
	canvas.drawString(margen_izq, PAGE_HEIGHT-130, "Nombres: %s" % doc.paciente)
	canvas.drawString(4*inch, PAGE_HEIGHT-130, "Edad: %s" % doc.edad)
	canvas.drawString(6*inch, PAGE_HEIGHT-130, "Genero: %s" % doc.genero)

	canvas.drawString(margen_izq, PAGE_HEIGHT-140, "Empresa: %s" % doc.empresa)
	canvas.drawString(4*inch, PAGE_HEIGHT-140, "Historia #: %s" % doc.no_orden)
	canvas.drawString(6*inch, PAGE_HEIGHT-140, "Fecha: %s" % doc.fecha)
	
	if doc.tipo:
		canvas.drawString(margen_izq, PAGE_HEIGHT-150, "De: %s" % doc.de)
		canvas.drawString(4*inch, PAGE_HEIGHT-150, "Para: %s" % doc.para)
		canvas.setFont('Times-Bold',10)
		canvas.drawString(margen_izq, PAGE_HEIGHT-155, rayaOrden)
	else:	
		canvas.setFont('Times-Bold',10)
		canvas.drawString(margen_izq, PAGE_HEIGHT-145, rayaOrden)

	canvas.restoreState()
    
def cuerpoOrden(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman', 8)
    canvas.drawString(inch, 0.3 * inch,"Pagina %d.  Historia #: %s.  Paciente: %s." % (doc.page, doc.no_orden, doc.paciente))
    canvas.restoreState()

class ImprimeOrden(SimpleDocTemplate):
	def __init__(self, filename, no_orden, tipo, **kw):
		SimpleDocTemplate.__init__(self, filename, pagesize=(612.0, 366.0), rightMargin=18, leftMargin=18, bottomMargin=18, **kw)

		t_orden = orden.objects.get(pk = no_orden)
		h = historia_clinica.objects.get(orden = t_orden)
		self.no_orden = h.id
		self.institucion = t_orden.institucion.razon
		self.direccion = t_orden.institucion.direccion
		self.telefono = t_orden.institucion.telefono
		self.empresa = t_orden.empresa.razon
		self.edad = t_orden.paciente.edad
		self.fecha = t_orden.fecha_atencion
		self.paciente = t_orden.paciente
		self.genero = t_orden.paciente.genero
		self.tipo = False

		if t_orden.institucion.imagen != "":
			self.has_logo = True
			self.logo = t_orden.institucion.imagen
		else:
			self.has_logo = False
			self.logo = ""		

		Story = [Spacer(1,0.3*inch)]

		style = styles["Normal"]  #Normal
		style.fontSize = 7
		style.fontName = 'Helvetica'
		styleJustify = styles["Justify"]
		styleJustify.fontSize = 7
		styleJustify.fontName = 'Helvetica'

		if tipo == 1:	#Posologias
			lista_p = posologias.objects.filter(orden = t_orden)
			for q in lista_p:	
				bogustext = ("<strong>%s:</strong> %s" % (q.medicamento,q.uso))
				p = Paragraph(bogustext, styleJustify)
				Story.append(p)
				Story.append(Spacer(1,0.005*inch))
		elif tipo == 2: #Ordenamiento de procedimientos
			lista_p = remision.objects.filter(orden = t_orden)
			for q in lista_p:	
				bogustext = ("<strong>%s:</strong> %s. Entidad: %s." % (q.ordenado,q.descripcion_orden,q.entidad))
				p = Paragraph(bogustext, styleJustify)
				Story.append(p)
				Story.append(Spacer(1,0.005*inch))
		elif tipo == 3:	 # Remision de Laboratorios
			lista_p = remisionlab.objects.filter(orden = t_orden)
			for q in lista_p:	
				bogustext = ("<strong>%s:</strong>" % q.laboratorio)
				p = Paragraph(bogustext, styleJustify)
				Story.append(p)
				Story.append(Spacer(1,0.005*inch))
		elif tipo == 4:
			self.tipo = True
			self.de = "GASTROENTEROLOGIA"
			self.para = h.para
			Story.append(Spacer(1,0.1*inch))
			bogustext = ("<strong>MC: </strong>%s  <strong>EA: </strong>%s" % (h.motivo,h.enfermedad_actual))
			p = Paragraph(bogustext, styleJustify)
			Story.append(p)
			bogustext = ("<strong>EXAMEN FISICO:</strong> PA (mmHg): %s , FC (min): %s, FR (min): %s,"
				" T (C): %s, TALLA (Cm): %s, PESO (Kg): %s, PULSO (min): %s, MASA CORP (Kg/mt2): %s,"
				" DESCRIPCION: %s, CABEZA, CARA Y CUELLO: %s, ORL: %s, SIST. RESPIRATORIO: %s, SIST. CARDIO VASCULAR: %s,"
				" SIST. DIGESTIVO: %s, SIST. GENITOURINARIO: %s, TACTO RECTAL: %s" 
				% (h.presion_arterial,h.frecuencia_cardiaca,h.frecuencia_respiratoria,h.temperatura,h.talla,h.peso,
					h.pulso,h.masa_corporal,h.descripcion,h.cabeza,h.orl,h.sist_respiratorio,h.sist_cardiovascular,
					h.sist_digestivo,h.sist_genitourinario,h.tacto))
			p = Paragraph(bogustext, styles["Justify"])
			Story.append(p)
			bogustext = ("<strong>DIAGNOSTICO PROVISIONAL: </strong>%s." % h.diagnostico)
			p = Paragraph(bogustext, styleJustify)
			bogustext = ("<strong>MOTIVO: </strong>%s." % h.remisiones)
			p = Paragraph(bogustext, styleJustify)
			Story.append(p)
			Story.append(Spacer(1,0.008*inch))
										
		Story.append(Spacer(1,0.08*inch))	
		if t_orden.medico.imagen != "":
			im = Image(t_orden.medico.imagen, width=2.3*inch, height=0.3*inch)
			im.hAlign = 'LEFT'
			Story.append(im)

		Story.append(Spacer(1,0.08*inch))
		bogustext = ("<strong>%s %s %s</strong>" % (t_orden.medico.nombre,t_orden.medico.papellido,t_orden.medico.sapellido))
		p = Paragraph(bogustext, style)
		Story.append(p)
		Story.append(Spacer(1,0.01*inch))
		bogustext = ("ESPECIALISTA EN %s" % (t_orden.medico.especialidad))
		p = Paragraph(bogustext, style)
		Story.append(p)
		Story.append(Spacer(1,0.01*inch))
		bogustext = ("%s" % (t_orden.medico.registro))
		p = Paragraph(bogustext, style)
		Story.append(p)
		Story.append(Spacer(1,0.01*inch))

		self.build(Story, onFirstPage=encabezadoOrden, onLaterPages=cuerpoOrden)		

def encabezadoProc(canvas, doc):
	canvas.saveState()
	if doc.has_logo:
		canvas.drawImage(doc.logo.path, inch, pagina_alto-200, width=6.5*inch,height=inch,mask=None)
	else:	
		canvas.setFont('Times-Bold',18)
		canvas.drawCentredString(pagina_ancho/2.0, pagina_alto-180, doc.institucion)
		canvas.setFont('Times-Roman',11)
		canvas.drawCentredString(pagina_ancho/2.0, pagina_alto-190, "%s / %s" % (doc.direccion,doc.telefono))
		canvas.drawCentredString(pagina_ancho/2.0, pagina_alto-200, "BARRANQUILLA - COLOMBIA")

	canvas.setFont('Times-Bold',13)
	canvas.drawCentredString(pagina_ancho/2.0, pagina_alto-250, doc.procedimiento)	
	
	canvas.setFont('Times-Bold',10)
	canvas.drawString(inch, pagina_alto-255, raya)
	canvas.drawString(inch, pagina_alto-270, "Nombres: %s" % doc.paciente)
	canvas.drawString(6*inch, pagina_alto-270, "Historia #: %s" % doc.no_orden)

	canvas.drawString(inch, pagina_alto-282, "Empresa: %s" % doc.empresa)
	canvas.drawString(6*inch, pagina_alto-282, "Edad: %s" % doc.edad)

	canvas.drawString(inch, pagina_alto-294, "Fecha: %s" % doc.fecha)
	canvas.drawString(6*inch, pagina_alto-294, "Genero: %s" % doc.genero)

	canvas.drawString(inch, pagina_alto-306, "Responsable: %s" % doc.responsable)
	canvas.drawString(6*inch, pagina_alto-306, "Parentesco: %s" % doc.parentesco)
	canvas.drawString(inch, pagina_alto-311, raya)
	canvas.restoreState()
    
def cuerpoProc(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman', 8)
    canvas.drawString(inch, 0.75 * inch,"Pagina %d.  Historia #: %s.  Paciente: %s." % (doc.page, doc.no_orden, doc.paciente))
    canvas.restoreState()

class ImprimeProcedimiento(SimpleDocTemplate):
	def __init__(self, filename, no_orden, **kw):
		SimpleDocTemplate.__init__(self, filename, pagesize=(612.0, 732.0), **kw)

		t_orden = orden.objects.get(pk = no_orden)
		h = historia_procedimientos.objects.get(orden = t_orden)
		self.no_orden = h.id
		self.institucion = t_orden.institucion.razon
		self.direccion = t_orden.institucion.direccion
		self.telefono = t_orden.institucion.telefono
		self.empresa = t_orden.empresa.razon
		self.edad = t_orden.paciente.edad
		self.fecha = t_orden.fecha_atencion
		self.paciente = t_orden.paciente
		self.genero = t_orden.paciente.genero
		self.logo = t_orden.institucion.imagen
		self.procedimiento = h.procedimiento.descripcion
		self.responsable = "%s %s" % (t_orden.paciente.responsable_nombre,t_orden.paciente.responsable_apellido)
		t_p = t_orden.paciente.responsable_parentesco
		if t_p == 'P':
			self.parentesco = 'Padre'
		elif t_p == 'M':
			self.parentesco = 'Madre'
		elif t_p == 'H':
			self.parentesco = 'Hermano'
		elif t_p == 'A':
			self.parentesco = 'Abuelo'
		elif t_p == 'T':
			self.parentesco = 'Tio'
		elif t_p == 'B':
			self.parentesco = 'Primo'
		elif t_p == 'C':
			self.parentesco = 'Conyugue'
		elif t_p == 'X':
			self.parentesco = 'Amigo'
		else:
			self.parentesco = 'Otro'

		if t_orden.institucion.imagen != "":
			self.has_logo = True
		else:
			self.has_logo = False		

		Story = [Spacer(1,2*inch)]

		style = styles["Normal"]  #Normal
		style.fontSize = 9
		style.fontName = 'Helvetica'
		
		bogustext = ("<strong>HALLAZGOS:</strong> %s" % h.hallazgos)
		p = Paragraph(bogustext, styles["Justify"])
		Story.append(p)
		Story.append(Spacer(1,0.08*inch))
		bogustext = ("<strong>DIAGNOSTICO:</strong> %s" % h.impresion)
		p = Paragraph(bogustext, styles["Justify"])
		Story.append(p)
		Story.append(Spacer(1,0.08*inch))


		Story.append(Spacer(1,0.5*inch))

		if t_orden.medico.imagen != "":
			im = Image(t_orden.medico.imagen, width=2.3*inch, height=0.5*inch)
			im.hAlign = 'LEFT'
			Story.append(im)

		Story.append(Spacer(1,0.08*inch))
		bogustext = ("<strong>%s %s %s</strong>" % (t_orden.medico.nombre,t_orden.medico.papellido,t_orden.medico.sapellido))
		p = Paragraph(bogustext, style)
		Story.append(p)
		Story.append(Spacer(1,0.03*inch))
		bogustext = ("ESPECIALISTA EN %s" % (t_orden.medico.especialidad))
		p = Paragraph(bogustext, style)
		Story.append(p)
		Story.append(Spacer(1,0.03*inch))
		bogustext = ("%s" % (t_orden.medico.registro))
		p = Paragraph(bogustext, style)
		Story.append(p)
		Story.append(Spacer(1,0.03*inch))

		self.build(Story, onFirstPage=encabezadoProc, onLaterPages=cuerpoProc)		