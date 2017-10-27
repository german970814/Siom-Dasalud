# -*- coding: utf-8 -*-
from django.db import models
from mysite.apps.datos.models import paciente,medico
from mysite.apps.home.models import departamentos
from mysite.apps.organizaciones.models import empresas,instituciones,eps,arp
from mysite.apps.parametros.models import serviciosEmpresa,procedimientos,consultas,cie
from django.contrib.auth.models import User
import datetime
from datetime import date

from .managers import OrdenManager


class orden(models.Model):
    opciones = (
        ('P', 'Pendiente'),
        ('R', 'Realizada'),
    )

    opciones2 = (
        ('S', 'Servicio'),
        ('L', 'Laboratorio'),
    )

    opExamen = (
        ('1', 'Ingreso'),
        ('2', 'Periodico'),
        ('3', 'Egreso'),
        ('4', 'Otros'),
        ('5', 'Ninguno'),
    )

    opExamen2 = (
        ('1', 'Examen de Altura'),
        ('2', 'Post Incapacidad'),
        ('3', 'Ninguno'),
        ('4', 'Manipulacion de Alimentos'),
    )

    #Datos de la Historia Clinica
    paciente	= models.ForeignKey(paciente,related_name='orden_paciente')
    empresa = models.ForeignKey(empresas,related_name='orden_empresa',verbose_name=u'Empresa que ordena')
    fecha	= models.DateTimeField(verbose_name="Fecha Orden",default=datetime.datetime.now)
    fecha_atencion	= models.DateField(verbose_name="Fecha Atencion",default=datetime.date.today)
    medico = models.ForeignKey(medico,related_name='orden_medico')
    institucion = models.ForeignKey(instituciones,related_name='ordeninstitucion_empresa',verbose_name=u'Institucion a la que Pertenece')
    status	= models.CharField(max_length=1, choices=opciones, default='P', verbose_name='Estado')
    generadapor = models.ForeignKey(User,null=True, blank=True)
    examen = models.CharField(max_length=2, choices=opExamen, default='5',verbose_name=u'Examen de')
    examen_adicional = models.CharField(max_length=2, choices=opExamen2, default='3',verbose_name=u'Examen Adicional')
    empresa_cliente = models.CharField(max_length=200, verbose_name='Empresa Cliente')
    cargo   = models.CharField(max_length=100)
    seccion = models.CharField(max_length=100)
    #Octubre 14 de 2015
    anulada = models.BooleanField(default=False)
    razon_anulacion = models.TextField(max_length=100, null=True, blank=True)

    objects = OrdenManager()

    def __unicode__(self):
        return "%s %s" %(self.paciente.pnombre,self.id)

    def get_class_by_status(self):
        CLASSES = {
            'warning': 'warning',
            'danger': 'danger',
            'success': 'success'
        }

        css_class = '';
        if self.anulada:
            css_class = CLASSES['warning']
        else:
            visiometria = getattr(self, 'visiometria', None)
            audiometria = getattr(self, 'audiometria', None)
            recepcion = getattr(self, 'recepcion', None)

            if visiometria is not None:
                if visiometria.estado == visiometria.__class__.PENDIENTE:
                    css_class = CLASSES['danger']
                else:
                    css_class = CLASSES['success']
            if audiometria is not None and css_class != CLASSES['danger']:
                if audiometria.estado == audiometria.__class__.PENDIENTE:
                    css_class = CLASSES['danger']
                else:
                    css_class = CLASSES['success']
            if recepcion is not None and css_class != CLASSES['danger']:
                if recepcion.estado == recepcion.__class__.RESULTADO_EMITIDO:
                    css_class = CLASSES['success']
                else:
                    css_class = CLASSES['danger']
            if self.status == 'P':
                css_class = CLASSES['danger']
            else:
                css_class = CLASSES['success']
        return css_class

class ordenesProducto(models.Model):
    orden = models.ForeignKey(orden,related_name='OrdenProducto_orden',verbose_name=u'Orden')
    servicio = models.ForeignKey(serviciosEmpresa,related_name='ordenProducto_servicio',verbose_name=u'Servicio')

    def __unicode__(self):
        return "Orden #:%s -- %s" % (self.orden.id,self.servicio.nombre.nombre)

class historia_clinica(models.Model):
    opcionesSiNo = (
        ('S', 'Si'),
        ('N', 'No'),
    )

    opcionesTurno = (
        ('D', 'Diurno'),
        ('N', 'Nocturno'),
        ('R', 'Rotatorio'),
    )

    opcionesActividad = (
        ('P', 'De Pie'),
        ('S', 'Sentado'),
        ('D', 'Deambulado'),
    )

    opEstado = (
        ('B', 'Bueno'),
        ('R', 'Regular'),
        ('M', 'Malo'),
    )

    opEscribe = (
        ('Z', 'Zurdo'),
        ('D', 'Diestro'),
        ('A', 'Ambidiestro'),
    )

    opNormal = (
        ('N', 'Normal'),
        ('A', 'Anormal'),
    )

    opGenitales = (
        ('N', 'No Explorado'),
        ('E', 'Explorado'),
    )

    opRuidos = (
        ('N', 'Normales'),
        ('F', 'Fuertes'),
        ('V', 'Velados'),
    )

    opVasos = (
        ('N', 'Normales'),
        ('E', 'Escleroticos'),
    )

    opGrados = (
        ('P', 'Primero'),
        ('S', 'Segundo'),
        ('T', 'Tercero'),
        ('N', 'Ninguno'),
    )

    opConcepto = (
        ('1', 'Apto'),
        ('2', 'Apto para trabajar en altura'),
        ('3', 'Apto para manipulacion de alimentos'),
        ('4', 'Apto con recomendaciones de seguimiento'),
        ('5', 'Apto con patologia que no interfieren con el cargo'),
        ('6', 'Apto con restricciones'),
        ('7', 'Aplazado'),
        ('8', 'Concepto NO emitido'),
    )

    opRemitir = (
        ('E', 'E.P.S'),
        ('A', 'A.R.S'),
        ('N', 'Ninguno'),
    )

    opBiologico = (
        ('1', 'Virus'),
        ('2', 'Bacteria'),
        ('3', 'Hongos'),
        ('4', 'Parasitos'),
        ('5', 'Otros'),
        ('6', 'Ninguno'),
    )

    opMecanicos = (
        ('1', 'Caídas'),
        ('2', 'Contusiones'),
        ('3', 'Torceduras'),
        ('4', 'Otros'),
        ('5', 'Ninguno'),
    )

    opFisicos = (
        ('1', 'Quemaduras por Electricidad 1er grado'),
        ('2', 'Quemaduras por Electricidad  2do grado'),
        ('3', 'Quemaduras por Electricidad  3er grado'),
        ('4', 'Altas temperaturas'),
        ('5', 'Bajas temperaturas'),
        ('6', 'Iluminación'),
        ('7', 'Radiaciones'),
        ('8', 'Vibraciones'),
        ('9', 'Ruido'),
        ('A', 'Otros'),
        ('B', 'Ninguno'),
    )

    opErgonomicos = (
        ('1', 'Posturas'),
        ('2', 'Reubicación de Puesto'),
        ('3', 'Otros'),
        ('4', 'Ninguno'),
    )

    opPsicologicos = (
        ('1', 'Estrés laboral'),
        ('2', 'Acoso laboral'),
        ('3', 'Otros'),
        ('4', 'Ninguno'),
    )

    opQuimicos = (
        ('1', 'Vapores'),
        ('2', 'Gases'),
        ('3', 'Quemaduras por corrosivo 1 2 y 3 grado'),
        ('4', 'Inflamables'),
        ('5', 'Toxicos'),
        ('6', 'Irritantes'),
        ('7', 'Muy toxicos'),
        ('8', 'Explosivos'),
        ('9', 'Radiactivos'),
        ('A', 'Nocivos'),
        ('B', 'Explosivos'),
        ('C', 'Polvos'),
        ('D', 'Solidos'),
        ('E', 'Otros'),
        ('F', 'Ninguno'),
    )

    opPlanificacion = (
        ('1', 'Preservativo'),
        ('2', 'Implante Subdermico'),
        ('3', 'DIU'),
        ('4', 'Pomeroy'),
        ('5', 'Inyección'),
        ('6', 'Píldora'),
        ('7', 'Ritmo'),
        ('8', 'Otros'),
        ('9', 'Ninguno'),
    )

    opHernias = (
        ('1', 'Inguinal Derecha'),
        ('2', 'Inguinal Izquierda'),
        ('3', 'Umbilical'),
        ('4', 'Diafragmatica'),
        ('5', 'Hiatal'),
        ('N', 'Ninguno'),
    )

    opPreconcepto = (
        ('A', 'Paciente Aparentemente Sano'),
        ('O', 'Paciente con Observaciones'),
        ('N', 'Ninguno'),
    )

    orden	= models.ForeignKey(orden,related_name='historia_orden')
    paciente	= models.ForeignKey(paciente,related_name='historia_paciente')
    cerrada = models.BooleanField(default=False)
    eps	= models.ForeignKey(eps,related_name='historia_eps')
    arl	= models.ForeignKey(arp,related_name='historia_arl')
    afp	= models.ForeignKey(arp,related_name='historia_afp')
    primera_vez = models.BooleanField(default=False)
    hijos	=  models.CharField(max_length=2, choices=opcionesSiNo, default='N',verbose_name=u'Hijos')
    num_hijos	=  models.CharField(max_length=2, verbose_name=u'Nº Hijos', default='0', null=True, blank=True)
    turno =  models.CharField(max_length=1, choices=opcionesTurno, default='D',verbose_name=u'Turno')
    actividad =  models.CharField(max_length=1, choices=opcionesActividad, default='P',verbose_name=u'Actividad Realizada')
    #Antecedentes de Trabajos u oficios
    a_empresa1   = models.CharField(max_length=100, null=True, blank=True)
    a_ocupacion1   = models.CharField(max_length=100, null=True, blank=True)
    a_tiempo1   = models.CharField(max_length=50, null=True, blank=True)
    a_biolog1   = models.CharField(max_length=1, choices=opBiologico, default='6')
    a_mec1   = models.CharField(max_length=1, choices=opMecanicos, default='5')
    a_fis1   = models.CharField(max_length=1, choices=opFisicos, default='B')
    a_erg1   = models.CharField(max_length=1, choices=opErgonomicos, default='4')
    a_psi1   = models.CharField(max_length=1, choices=opPsicologicos, default='4')
    a_qui1   = models.CharField(max_length=1, choices=opQuimicos, default='F')
    a_prot1   = models.CharField(max_length=1, choices=opcionesSiNo, default='S')

    a_empresa2   = models.CharField(max_length=100, null=True, blank=True)
    a_ocupacion2   = models.CharField(max_length=100, null=True, blank=True)
    a_tiempo2   = models.CharField(max_length=50, null=True, blank=True)
    a_biolog2   = models.CharField(max_length=1, choices=opBiologico, default='6')
    a_mec2   = models.CharField(max_length=1, choices=opMecanicos, default='5')
    a_fis2   = models.CharField(max_length=1, choices=opFisicos, default='B')
    a_erg2   = models.CharField(max_length=1, choices=opErgonomicos, default='4')
    a_psi2   = models.CharField(max_length=1, choices=opPsicologicos, default='4')
    a_qui2   = models.CharField(max_length=1, choices=opQuimicos, default='F')
    a_prot2   = models.CharField(max_length=1, choices=opcionesSiNo, default='S')

    accidente =   models.CharField(max_length=2, choices=opcionesSiNo, default='N',verbose_name=u'Accidente de Trabajo')
    enfermedad_profesional =   models.CharField(max_length=2, choices=opcionesSiNo, default='N',verbose_name=u'Enfermedad Profesional')
    detalle =  models.TextField(max_length=200, null=True, blank=True)

    #Antecedentes(Todos estos: Negativos)
    quirurgicos  = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    hospitalizacion = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    accidente_p = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    fracturas = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    tabaquismo = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    intoxicaciones = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    alcoholismo = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    mentales = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    asma  = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    tbc   = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    alergias = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    gripas   = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    enf_piel  = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    otologicos = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    diabetes  = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    hematologicos  = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    epilepsia  = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    cancer  = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    hipertension  = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    otros	= models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    #Antecedentes Familiares
    f_quirurgicos  = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    f_hospitalizacion = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    f_accidente_p = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    f_fracturas = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    f_tabaquismo = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    f_intoxicaciones = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    f_alcoholismo = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    f_mentales = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    f_asma  = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    f_tbc   = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    f_alergias = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    f_gripas   = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    f_enf_piel  = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    f_otologicos = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    f_diabetes  = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    f_hematologicos  = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    f_epilepsia  = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    f_cancer  = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    f_hipertension  = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    f_otros	= models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    descripcion_antecedente = models.TextField(max_length=300, null=True, blank=True)
    #Habitos
    alcohol	= models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    deportes = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    frecuencia = models.TextField(max_length=30, null=True, blank=True)
    #Gineco
    menarquia  = models.CharField(max_length=50, null=True, blank=True)
    hijos_vivos	=  models.CharField(max_length=2, verbose_name=u'Nº Hijos Vivos', default='0', null=True, blank=True)
    ciclos   = models.CharField(max_length=50, null=True, blank=True)
    gravida = models.CharField(max_length=6, null=True, blank=True)
    partos =  models.CharField(max_length=6, null=True, blank=True)
    abortos = models.CharField(max_length=6, null=True, blank=True)
    cesareas = models.CharField(max_length=6, null=True, blank=True)
    fum	= models.DateField(verbose_name="FUM", null=True, blank=True)
    fup = models.DateField(verbose_name="FUP", null=True, blank=True)
    dismenorrea = models.CharField(max_length=50, null=True, blank=True)
    metrorragias = models.CharField(max_length=50, null=True, blank=True)
    trastorno_ciclo = models.CharField(max_length=50, null=True, blank=True)
    citologias = models.CharField(max_length=50, null=True, blank=True)
    transtorno_otros = models.CharField(max_length=60, null=True, blank=True)
    planificacion = models.CharField(max_length=1, choices=opPlanificacion, default='9')
    sintomas = models.TextField(max_length=200)
    #Signos Vitales
    peso 				= models.CharField(max_length=4)#(Kilos)
    talla				= models.CharField(max_length=6) #(Cm)
    pulso				= models.CharField(max_length=4)#(min)
    temperatura 		= models.CharField(max_length=6) #(ºC)
    presion_arterial	= models.CharField(max_length=7)
    masa_corporal 		= models.CharField(max_length=6) #(Kg/mt2)
    #Estado General
    estado = models.CharField(max_length=1, choices=opEstado, default='B')
    escribe = models.CharField(max_length=1, choices=opEscribe, default='D')
    #Exploracion Osea Muscular
    cabeza = models.CharField(max_length=1, choices=opNormal, default='N')
    cuello = models.CharField(max_length=1, choices=opNormal, default='N')
    torax = models.CharField(max_length=1, choices=opNormal, default='N')
    abdomen = models.CharField(max_length=1, choices=opNormal, default='N')
    columna_cervical = models.CharField(max_length=1, choices=opNormal, default='N')
    columna_dorsal = models.CharField(max_length=1, choices=opNormal, default='N')
    columna_lumbo = models.CharField(max_length=1, choices=opNormal, default='N')
    m_superiores = models.CharField(max_length=1, choices=opNormal, default='N')
    m_inferiores = models.CharField(max_length=1, choices=opNormal, default='N')
    descripcion_osteomuscular = models.TextField(max_length=200, null=True, blank=True)
    #Dinamica (Movimientos Articulares)
    d_cuello = models.CharField(max_length=1, choices=opNormal, default='N')
    d_hombros = models.CharField(max_length=1, choices=opNormal, default='N')
    d_codo = models.CharField(max_length=1, choices=opNormal, default='N')
    d_muneca = models.CharField(max_length=1, choices=opNormal, default='N')
    d_cadera = models.CharField(max_length=1, choices=opNormal, default='N')
    d_rodilla = models.CharField(max_length=1, choices=opNormal, default='N')
    d_tobillo = models.CharField(max_length=1, choices=opNormal, default='N')

    d_cuello_o = models.TextField(max_length=50, default='Ninguna', null=True, blank=True)
    d_hombros_o = models.TextField(max_length=50, default='Ninguna', null=True, blank=True)
    d_codo_o = models.TextField(max_length=50, default='Ninguna', null=True, blank=True)
    d_muneca_o = models.TextField(max_length=50, default='Ninguna', null=True, blank=True)
    d_cadera_o = models.TextField(max_length=50, default='Ninguna', null=True, blank=True)
    d_rodilla_o = models.TextField(max_length=50, default='Ninguna', null=True, blank=True)
    d_tobillo_o	 = models.TextField(max_length=50, default='Ninguna', null=True, blank=True)
    #Organos o Sistemas
    cicatrices = models.CharField(max_length=1, choices=opNormal, default='N')
    piel = models.CharField(max_length=1, choices=opNormal, default='N')
    craneo = models.CharField(max_length=1, choices=opNormal, default='N')
    #Ojos
    conjuntivas = models.CharField(max_length=1, choices=opNormal, default='N')
    pupilas = models.CharField(max_length=1, choices=opNormal, default='N')
    anexos = models.CharField(max_length=1, choices=opNormal, default='N')
    reflejos = models.CharField(max_length=1, choices=opNormal, default='N')
    fondo = models.CharField(max_length=1, choices=opNormal, default='N')
    #Oidos
    pabellones = models.CharField(max_length=1, choices=opNormal, default='N')
    ostocopia = models.CharField(max_length=1, choices=opNormal, default='N')
    #Nariz
    tabique = models.CharField(max_length=1, choices=opNormal, default='N')
    cornetes = models.CharField(max_length=1, choices=opNormal, default='N')
    #Boca
    labios = models.CharField(max_length=1, choices=opNormal, default='N')
    faringe = models.CharField(max_length=1, choices=opNormal, default='N')
    #Otros
    tiroides = models.CharField(max_length=1, choices=opNormal, default='N')
    o_torax = models.CharField(max_length=1, choices=opNormal, default='N')
    pulmones = models.CharField(max_length=1, choices=opNormal, default='N')
    corazon = models.CharField(max_length=1, choices=opNormal, default='N')
    #Abdomen
    pared = models.CharField(max_length=1, choices=opNormal, default='N')
    viseras = models.CharField(max_length=1, choices=opNormal, default='N')
    hernias = models.CharField(max_length=1, choices=opHernias, default='N')

    genitales = models.CharField(max_length=1, choices=opGenitales, default='N')
    vascular = models.CharField(max_length=1, choices=opNormal, default='N')
    #Sistema Nervioso
    o_reflejos = models.CharField(max_length=1, choices=opNormal, default='N')
    marcha = models.CharField(max_length=1, choices=opNormal, default='N')
    coordinacion = models.CharField(max_length=1, choices=opNormal, default='N')
    #Sistema Circulatorio
    ruidos  = models.CharField(max_length=1, choices=opNormal, default='N')
    extrasistoles = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    fibrilacion = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    soplos = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    sistolicos = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    diastolicos = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    presistolicos = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    vasos = models.CharField(max_length=1, choices=opVasos, default='N')
    varices = models.CharField(max_length=1, choices=opGrados, default='N')
    observaciones = models.TextField(max_length=200, default="Ninguna", null=True, blank=True)
    tunel = models.TextField(max_length=200, default="Ninguno", null=True, blank=True)
    phannel = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    tinnel = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    pre_concepto = models.CharField(max_length=1, choices=opPreconcepto, default='N')
    #Examenes de Diagnosticos
    f_imagen = models.DateField(verbose_name="Fecha Imagenologia", null=True, blank=True)
    r_imagen = models.TextField(max_length=150, null=True, blank=True)
    f_audiometria = models.DateField(verbose_name="Fecha Audiometria", null=True, blank=True)
    r_audiometria = models.TextField(max_length=150, null=True, blank=True)
    f_visiometria = models.DateField(verbose_name="Fecha Visiometria", null=True, blank=True)
    r_visiometria = models.TextField(max_length=150, null=True, blank=True)
    f_espirometria = models.DateField(verbose_name="Fecha Espirometria", null=True, blank=True)
    r_espirometria = models.TextField(max_length=150, null=True, blank=True)
    f_laboratorio = models.DateField(verbose_name="Fecha Laboratorio", null=True, blank=True)
    r_laboratorio = models.TextField(max_length=150, null=True, blank=True)
    concepto = models.CharField(max_length=1, choices=opConcepto, default='8')
    remitir = models.CharField(max_length=1, choices=opRemitir, default='N')
    valoracion = models.TextField(max_length=80, null=True, blank=True)
    recomendacion = models.TextField(max_length=500, null=True, blank=True)

    def __unicode__(self):
        salida = "%s  %s"%(self.paciente,self.id)
        return salida.encode('utf-8')

class test_altura(models.Model):
    opcionesSiNo = (
        ('S', 'Si'),
        ('N', 'No'),
    )

    opciones = (
        ('A', 'Anormal'),
        ('N', 'Normal'),
    )

    orden	= models.ForeignKey(orden,related_name='test_altura_orden')
    convulsiones_p   = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    diabetes   = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    reacciones   = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    claustrofobia   = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    acrofobia   = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    vertigos   = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    epilepsia   = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    enfermedad_mental   = models.CharField(max_length=1, choices=opcionesSiNo, default='N')

    a_cardiaco   = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    a_cerebro_v   = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    angina_pecho   = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    insuficiencia_cardiaca   = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    hinchazon_pies   = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    latidos   = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    presion   = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    otro   = models.CharField(max_length=1, choices=opcionesSiNo, default='N')

    dolor_pecho1   = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    dolor_pecho2  = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    dolor_pecho3  = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    late_irregularmente   = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    dolor_pecho_indigestion  = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    otros_sintomas   = models.CharField(max_length=1, choices=opcionesSiNo, default='N')

    lentes_contacto   = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    lentes  = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    daltonismo   = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    problema_ojos   = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    ob_problema = models.CharField(max_length=150, null=True, blank=True)

    prob_pulmonares  = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    prob_circulacion  = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    presion_alta  = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    convulsiones   = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    enf_mental  = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    perdida_vista   = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    dano_oidos   = models.CharField(max_length=1, choices=opcionesSiNo, default='N')

    dificultad_oir   = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    aparato_oir  = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    prob_audicion   = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    d_prob_audicion   = models.CharField(max_length=150, null=True, blank=True)

    debilidad_brazos  = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    dolor_espalda  = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    dificultad_extremidades  = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    dolor_rigidez   = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    dif_cabeza_arriba  = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    dif_cabeza_lado   = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    dif_agacharse   = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    dif_agacharse_piso  = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    dif_escalera   = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    lesion_espalda   = models.CharField(max_length=1, choices=opcionesSiNo, default='N')
    d_lesion   = models.CharField(max_length=150, null=True, blank=True)
    #Pruebas de equilibrio estatico
    romberg   = models.CharField(max_length=1, choices=opciones, default='N')
    ob_romberg   = models.CharField(max_length=150, null=True, blank=True)
    baranay   = models.CharField(max_length=1, choices=opciones, default='N')
    ob_baranay   = models.CharField(max_length=150, null=True, blank=True)
    hallpike   = models.CharField(max_length=1, choices=opciones, default='N')
    ob_hallpike   = models.CharField(max_length=150, null=True, blank=True)
    #Pruebas de equilibrio dinamico
    babinski_m_d   = models.CharField(max_length=5, null=True, blank=True)
    ob_babinski_m_d   = models.CharField(max_length=150, null=True, blank=True)
    babinski_m_i   = models.CharField(max_length=5, null=True, blank=True)
    ob_babinski_m_i   = models.CharField(max_length=150, null=True, blank=True)
    babinski_m_n   = models.CharField(max_length=5, null=True, blank=True)
    ob_babinski_m_n   = models.CharField(max_length=150, null=True, blank=True)

    unterberger_m_d   = models.CharField(max_length=5, null=True, blank=True)
    ob_unterberger_m_d   = models.CharField(max_length=150, null=True, blank=True)
    unterberger_m_c   = models.CharField(max_length=5, null=True, blank=True)
    ob_unterberger_m_c   = models.CharField(max_length=150, null=True, blank=True)
    unterberger_m_i   = models.CharField(max_length=5, null=True, blank=True)
    ob_unterberger_m_i   = models.CharField(max_length=150, null=True, blank=True)
    #Impresion Diagnostica
    neg_vert_per   = models.CharField(max_length=5, null=True, blank=True)
    ob_neg_vert_per  = models.CharField(max_length=150, null=True, blank=True)
    pos_vert_per   = models.CharField(max_length=5, null=True, blank=True)
    ob_pos_vert_per  = models.CharField(max_length=150, null=True, blank=True)
    post_vert_cent   = models.CharField(max_length=5, null=True, blank=True)
    ob_post_vert_cent = models.CharField(max_length=150, null=True, blank=True)

    def __unicode__(self):
        return "Test Orden #: %s. Orden: %s"%(self.orden.id,self.orden)

class laboratorios(models.Model):
    orden	= models.ForeignKey(orden,related_name='laboratorios_orden')
    examen  = models.CharField(max_length=50)
    fecha   = models.DateField(verbose_name="Fecha Examen", null=True, blank=True)
    resultado = models.CharField(max_length=150)

    def __unicode__(self):
        return "Orden: %s. Examen: %s"%(self.orden,self.examen)

class posologias(models.Model):
    orden	= models.ForeignKey(orden,related_name='posologias_orden')
    medicamento		= models.CharField(max_length=150)
    uso				= models.TextField(max_length=300)

class remision(models.Model):
    orden	= models.ForeignKey(orden,related_name='remision_orden')
    ordenado    		= models.CharField(max_length=150)
    descripcion_orden	= models.TextField(max_length=300)
    entidad				= models.CharField(max_length=100) #preguntar si estas entidades estan establecidas

class remisionlab(models.Model):
    orden	= models.ForeignKey(orden,related_name='remisionlab_orden')
    laboratorio		= models.CharField(max_length=150) #preguntar si estos laboratorios estan establecidos


def number():
    #Se debe crear el primer registro para empezar a facturar
    no = consecutivo.objects.all().aggregate(Max('numero'))
    if no["numero__max"] == None:
        return 1
    else:
        return no["numero__max"]+ 1

class consecutivo(models.Model):
    numero = models.PositiveIntegerField(unique=True, default=number)

class historia_procedimientos(models.Model):
    opciones = (
        ('1', 'Ambulatorio'),
         ('2', 'Hospitalario'),
         ('3', 'En urgencias'),
    )

    opciones2 = (
        ('1', 'Diagnostico'),
         ('2', 'Terapeutico'),
         ('3', 'Proteccion especifica'),
         ('4', 'Deteccion temprana de enfermedad general'),
         ('5', 'Deteccion temprana de enfermedad profesional'),
    )

    opciones3 = (
        ('1', 'Médico (a) especialista'),
         ('2', 'Médico (a) general'),
         ('3', 'Enfermera (o)'),
         ('4', 'Auxiliar de enfermería'),
         ('5', 'Otro'),
    )

    opciones4 = (
        ('1', 'Único o unilateral'),
         ('2', 'Multiple o Bilateral misma via, diferente especialidad'),
         ('3', 'Multiple o Bilateral misma via, igual especialidad'),
         ('4', 'Multiple o Bilateral diferente via, diferente especialidad'),
         ('5', 'Multiple o Bilateral diferente via, igual especialidad'),
    )

    orden	= models.ForeignKey(orden,related_name='procedimiento_orden')
    paciente	= models.ForeignKey(paciente,related_name='historia_procedimientos_paciente')
    procedimiento = models.ForeignKey(procedimientos,related_name='procedimiento_empresa')
    hallazgos = models.TextField(max_length=1000)
    #Impresión Diagnóstica
    impresion 		= models.TextField(max_length=300, default="")
    #Remision Interna
    remision		= models.TextField(max_length=300, default="", null=True, blank=True)
    #RIPS
    ambito 		= models.CharField(max_length=1, choices=opciones, default='1',verbose_name=u'Ambito de realización del procedimiento')
    finalidad   = models.CharField(max_length=1, choices=opciones2, default='1',verbose_name=u'Finalidad del procedimiento')
    personal  = models.CharField(max_length=1, choices=opciones3, default='1',verbose_name=u'Personal que atiende')
    diagnostico = models.ForeignKey(cie,related_name='procedimiento_diagnostico_cie',verbose_name=u'Diagnostico', null=True, blank=True)
    diagnostico1 = models.ForeignKey(cie,related_name='procedimiento_diagnostico1_cie',verbose_name=u'Diagnostico 1', null=True, blank=True)
    complicacion = models.ForeignKey(cie,related_name='procedimiento_complicacion_cie',verbose_name=u'Complicacion', null=True, blank=True)
    forma = models.CharField(max_length=1, choices=opciones4, default='1',verbose_name=u'Forma de realizacion del acto quirurgico')

    def __unicode__(self):
        return "%s   %s"%(self.paciente,self.procedimiento)
