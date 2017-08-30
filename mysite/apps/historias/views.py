from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from mysite.apps.historias.models import orden,ordenesProducto,historia_clinica,test_altura,historia_procedimientos,posologias,remision,remisionlab
from mysite.apps.historias.forms import addOrdenForm,addOrdenSiomForm,addOrdenAnulaForm,addOrdenProductoForm,addhistoria_clinicaForm,addtest_alturaForm,addhistoria_procedimientosForm,addposologiaForm,addremisionForm,addremisionlabForm,fechaRipsForm,filtroOrdenForm
from mysite.apps.datos.models import especialidades,paciente,medico
from mysite.apps.parametros.models import serviciosEmpresa,cie,procedimientos,consultas,rango_procedimiento,rango_consulta,honorarios,sala,sutura
from mysite.apps.organizaciones.models import instituciones,empresas,planes_salud
from mysite.apps.facturacion.models import factura
from mysite.apps.parametros.forms import serviciosForm, servicios
from django.contrib.auth.models import User
from mysite.apps.home.models import userProfile
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
import json as simplejson
import json
from django.contrib.auth.decorators import login_required
from mysite.settings import URL_LOGIN
import csv
import datetime
from datetime import date, timedelta
from django.db.models import Max,Q
from reportlab.pdfgen import canvas

from mysite.apps.laboratorios.models import Laboratorio
from mysite.apps.examenes.models import Visiometria, Audiometria
from django.core.urlresolvers import reverse

@login_required(login_url=URL_LOGIN)
def historias_view(request,pagina):
	historias= historia_clinica.objects.all().order_by('orden__fecha')[:1000]
	ctx = {'historias':historias}
	return render_to_response('home/historias.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def add_historias_view(request,id_prod):
	exito = False
	exito_cerrada = False
	error = False
	existe_historia = False
	altura = False

	getorden = orden.objects.get(pk=id_prod) #Se obtiene informacion de la orden

	servicios = orden.objects.filter(id=getorden.id).servicios().values_list('id', flat=True)
	laboratorios = Laboratorio.objects.filter(servicio__id__in=servicios)

	resultados = getorden.resultados_laboratorio.all()

	visiometria = getattr(getorden, 'visiometria', None)

	for laboratorio in laboratorios:
		param = resultados.filter(laboratorio__id=laboratorio.id)
		if param.exists():
			laboratorio.resultado = param.get()

	if request.method == "POST":
		if 'btntabhistoria' in request.POST:
			try:#Verifica si la historia existe
				gethistoria = historia_clinica.objects.get(orden=getorden)
				existe_historia = True
			except:
				existe_historia = False

			if existe_historia:
				form1 = addhistoria_clinicaForm(request.POST,instance=gethistoria)
				if form1.is_valid():
					exito = True
					add = form1.save(commit=False)
					add.save() # Guardamos la Historia
					if getorden.examen_adicional == '1':
						altura = True
						getaltura = test_altura.objects.get(orden=getorden)
						form3= addtest_alturaForm(request.POST,instance=getaltura)
						altu = form3.save(commit=False)
						altu.save()
					else:
						altura = False
						form3= addtest_alturaForm()
			else:
				form1 = addhistoria_clinicaForm(request.POST)
				if form1.is_valid():
					add = form1.save(commit=False)
					add.paciente = getorden.paciente
					add.orden = getorden
					add.primera_vez = True
					add.save() # Guardamos la Historia
					getorden.save()
					exito = True
					if getorden.examen_adicional == '1':
						altura = True
						form3= addtest_alturaForm(request.POST)
						altu = form3.save(commit=False)
						altu.orden = getorden
						altu.save()
					else:
						altura = False
						form3 = addtest_alturaForm()
				else:
					form3 = addtest_alturaForm()
					if getorden.examen_adicional == '1':
						altura = True
					else:
						altura = False

			historial = historia_clinica.objects.filter(paciente=getorden.paciente)
			lista_proc = historia_procedimientos.objects.filter(paciente=getorden.paciente)
			form2 = addposologiaForm()
			ctx = {'visiometria': visiometria, 'laboratorios': laboratorios, 'getorden':getorden,'historial':historial,'lista_proc':lista_proc,'form1':form1,'form2':form2,'form3':form3,'exito':exito,'error':error,'altura':altura}
			return render_to_response('home/addHistorias.html',ctx,context_instance=RequestContext(request))

		if 'btntabhistoria_cerrar' in request.POST:
			try: #Verifica si existe para editarlo, de lo contrario se puede crear uno nuevo
				gethistoria = historia_clinica.objects.get(orden=getorden)
				form1 = addhistoria_clinicaForm(request.POST,instance=gethistoria)
				if getorden.examen_adicional == '1':
					altura = True
					getaltura = test_altura.objects.get(orden=getorden)
					form3= addtest_alturaForm(instance=getaltura)
				else:
					altura = False
					form3= addtest_alturaForm()

				if form1.is_valid():
					add = form1.save(commit=False)
					#Aqui se colocan todas las validaciones************************
					if add.concepto != '8':
						add.cerrada = True
						add.save() # Guardamos la Historia
						getorden.status = 'R'
						getorden.save()
						exito_cerrada = True
						exito = True
					else:
						exito_cerrada = False
						error = True
			except:
				form1 = addhistoria_clinicaForm(request.POST)
				if form1.is_valid():
					exito = False
					error = True
				form3 = addtest_alturaForm()
				if getorden.examen_adicional == '1':
					altura = True
				else:
					altura = False

			historial = historia_clinica.objects.filter(paciente=getorden.paciente)
			lista_proc = historia_procedimientos.objects.filter(paciente=getorden.paciente)
			form2 = addposologiaForm()
			ctx = {'visiometria': visiometria, 'laboratorios': laboratorios, 'getorden':getorden,'historial':historial,'lista_proc':lista_proc,'form1':form1,'form2':form2,'form3':form3,'exito':exito,'exito_cerrada':exito_cerrada,'error':error,'altura':altura}
			return render_to_response('home/addHistorias.html',ctx,context_instance=RequestContext(request))

	try: #Verifica si la historia ya existe para cargarla y continuar editandola
		gethistoria = historia_clinica.objects.get(orden=getorden)
		form1 = addhistoria_clinicaForm(instance=gethistoria)
		existe = True
	except:
		form1 = addhistoria_clinicaForm()
		existe = False

	historial = historia_clinica.objects.filter(paciente=getorden.paciente) #Se obtiene informacion de la orden
	lista_proc = historia_procedimientos.objects.filter(paciente=getorden.paciente)
	form2 = addposologiaForm()
	if getorden.examen_adicional == '1':
		altura = True
		if existe:
			getaltura = test_altura.objects.get(orden=getorden)
			form3= addtest_alturaForm(instance=getaltura)
		else:
			form3= addtest_alturaForm()
	else:
		altura = False
		form3= addtest_alturaForm()
	ctx = {'visiometria': visiometria, 'laboratorios': laboratorios, 'getorden':getorden,'historial':historial,'lista_proc':lista_proc,'form1':form1,'form2':form2,'form3':form3,'exito':exito,'error':error,'altura':altura}
	return render_to_response('home/addHistorias.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def edit_historias_view(request,id_prod):
	exito = False
	error = False
	info = True
	if request.method == "POST":
		if 'btntabhistoria' in request.POST:
			getorden = orden.objects.get(pk=id_prod)	 #Se obtiene informacion de la orden
			gethistoria = historia_clinica.objects.get(orden=getorden)
			form1 = addhistoria_clinicaForm(request.POST,instance=gethistoria)
			if form1.is_valid():
				add = form1.save(commit=False)
				add.save() # Guardamos la informacion
				exito = True
				if getorden.examen_adicional == '1':
					altura = True
					getaltura = test_altura.objects.get(orden=getorden)
					form3= addtest_alturaForm(request.POST,instance=getaltura)
					altu = form3.save(commit=False)
					altu.save()
				else:
					altura = False
					form3= addtest_alturaForm()


			historial = historia_clinica.objects.filter(paciente=getorden.paciente) #Se obtiene informacion de la orden
			lista_proc = historia_procedimientos.objects.filter(paciente=getorden.paciente)
			form2 = addposologiaForm()
			if getorden.examen_adicional == '1':
				altura = True
				getaltura = test_altura.objects.get(orden=getorden)
				form3= addtest_alturaForm(instance=getaltura)
			else:
				altura = False
				form3= addtest_alturaForm()

			ctx = {'getorden':getorden,'historial':historial,'lista_proc':lista_proc,'form1':form1,'form2':form2,'form3':form3,'exito':exito,'altura':altura}
			return render_to_response('home/addHistorias.html',ctx,context_instance=RequestContext(request))

	getorden = orden.objects.get(pk=id_prod)	 #Se obtiene informacion de la orden
	gethistoria = historia_clinica.objects.get(orden=getorden)
	historial = historia_clinica.objects.filter(paciente=getorden.paciente) #Se obtiene informacion de la orden
	lista_proc = historia_procedimientos.objects.filter(paciente=getorden.paciente)

	form1 = addhistoria_clinicaForm(instance=gethistoria)
	form2 = addposologiaForm()

	if getorden.examen_adicional == '1':
		altura = True
		getaltura = test_altura.objects.get(orden=getorden)
		form3= addtest_alturaForm(instance=getaltura)
	else:
		altura = False
		form3= addtest_alturaForm()

	ctx = {'getorden':getorden,'historial':historial,'lista_proc':lista_proc,'form1':form1,'form2':form2,'form3':form3,'exito':exito,'altura':altura}
	return render_to_response('home/addHistorias.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def show_historias_view(request, id_prod):
	"""Vista para ver las historias de una orden."""

	Orden = orden
	HistoriaClinica = historia_clinica
	TestAltura = test_altura
	# HistoriaProcedimiento = historia_procedimientos

	_orden = get_object_or_404(Orden, pk=id_prod)
	_historia = get_object_or_404(HistoriaClinica, orden=_orden)
	# _procedimientos = HistoriaProcedimiento.objects.filter(paciente=_orden.paciente)
	visiometria = getattr(_orden, 'visiometria', None)

	kwargs_form = {}
	data = {
		'getorden': _orden, 'gethistoria': _historia, 'altura': False, 'visiometria': visiometria
	}

	if _orden.examen_adicional == '1':
		data['altura'] = True
		kwargs_form['instance'] = TestAltura.objects.get(orden=_orden)
	
	data['form1'] = addhistoria_clinicaForm(instance=_historia)
	data['form2'] = addposologiaForm()
	data['form3'] = addtest_alturaForm(**kwargs_form)

	servicios = Orden.objects.filter(id=_orden.id).servicios().values_list('id', flat=True)
	laboratorios = Laboratorio.objects.filter(servicio__id__in=servicios)

	resultados = _orden.resultados_laboratorio.all()

	for laboratorio in laboratorios:
		param = resultados.filter(laboratorio__id=laboratorio.id)
		if param.exists():
			laboratorio.resultado = param.get()
	data['laboratorios'] = laboratorios

	return render(request, 'home/showHistorias.html', data)


@login_required(login_url=URL_LOGIN)
def add_evolucion_view(request,id_prod):
	exito = False
	error = False
	if request.method == "POST":
		if 'btntabhistoria' in request.POST:
			getorden= orden.objects.get(pk=id_prod)
			t_diagnostico = request.POST['diagnostico']
			if (t_diagnostico ==""):
				error = True
				form1 = addhistoria_clinicaForm(request.POST)
			else:
				try: #Verifica si existe para editarlo, de lo contrario se puede crear uno nuevo
					gethistoria = historia_clinica.objects.get(orden=getorden)
					form1 = addhistoria_clinicaForm(request.POST,instance=gethistoria)
					if form1.is_valid():
						exito = True
				except:
					form1 = addhistoria_clinicaForm(request.POST)
					if form1.is_valid():
						getdiagnostico = cie.objects.get(pk=t_diagnostico)
						t_diagnostico1 = request.POST['diagnostico1']
						t_diagnostico2 = request.POST['diagnostico2']
						t_diagnostico3 = request.POST['diagnostico3']
						if t_diagnostico1 == "":
							getdiagnostico1 = None
						else:
							getdiagnostico1 = cie.objects.get(pk=t_diagnostico1)

						if t_diagnostico2 == "":
							getdiagnostico2 = None
						else:
							getdiagnostico2 = cie.objects.get(pk=t_diagnostico2)

						if t_diagnostico3 == "":
							getdiagnostico3 = None
						else:
							getdiagnostico3 = cie.objects.get(pk=t_diagnostico3)

						add = form1.save(commit=False)
						add.paciente = getorden.paciente
						add.orden = getorden
						add.diagnostico = getdiagnostico
						add.diagnostico1 = getdiagnostico1
						add.diagnostico2 = getdiagnostico2
						add.diagnostico3 = getdiagnostico3
						add.save() # Guardamos la informacion
						getorden.status = 'R' #Se coloca la orden como realizada
						getorden.save()
						exito = True

			historial = historia_clinica.objects.filter(paciente=getorden.paciente) #Se obtiene informacion de la orden
			lista_proc = historia_procedimientos.objects.filter(paciente=getorden.paciente)
			posologia = posologias.objects.filter(orden = getorden)
			remisiones = remision.objects.filter(orden = getorden)
			remisioneslab = remisionlab.objects.filter(orden = getorden)
			form2 = addposologiaForm()
			form3 = addremisionForm(initial={'entidad':getorden.paciente.procede})
			form4 = addremisionlabForm()
			ctx = {'getorden':getorden,'historial':historial,'lista_proc':lista_proc,'form1':form1,'form2':form2,'form3':form3,'form4':form4,'posologia':posologia,'remisiones':remisiones,'remisioneslab':remisioneslab,'exito':exito,'error':error}
			return render_to_response('home/addHistorias.html',ctx,context_instance=RequestContext(request))

	getorden = orden.objects.get(pk=id_prod) #Se obtiene informacion de la orden
	historial = historia_clinica.objects.filter(paciente=getorden.paciente) #Se obtiene informacion de la orden
	lista_proc = historia_procedimientos.objects.filter(paciente=getorden.paciente)
	gethistoria = historia_clinica.objects.get(paciente=getorden.paciente,primera_vez=True)
	#Se inicializa el formulario con los valores de la historia clinica mas reciente ya que es una evolucion
	form1 = addhistoria_clinicaForm(initial={'enfermedad_actual':gethistoria.enfermedad_actual,
			'sentidos':gethistoria.sentidos,'piel':gethistoria.piel,'respiratorio':gethistoria.respiratorio,
			'cardio':gethistoria.cardio,'digestivo':gethistoria.digestivo,'genitourinario':gethistoria.genitourinario,
			'nervioso':gethistoria.nervioso,'locomotor':gethistoria.locomotor,'reproductivo':gethistoria.reproductivo,
			'otros':gethistoria.otros,'medicos':gethistoria.medicos,'transfusiones':gethistoria.transfusiones,
			'alergicos':gethistoria.alergicos,'gineco':gethistoria.gineco,'familiares':gethistoria.familiares,
			'quirurgicos':gethistoria.quirurgicos,'traumaticos':gethistoria.traumaticos,'toxicos':gethistoria.toxicos,
			'ets':gethistoria.ets,'famacologicos':gethistoria.famacologicos,'talla':gethistoria.talla,
			'peso':gethistoria.peso,'presion_arterial':gethistoria.presion_arterial,
			'frecuencia_cardiaca':gethistoria.frecuencia_cardiaca,'pulso':gethistoria.pulso,'masa_corporal':gethistoria.masa_corporal,
			'temperatura':gethistoria.temperatura,'frecuencia_respiratoria':gethistoria.frecuencia_respiratoria,
			'descripcion':gethistoria.descripcion,'cabeza':gethistoria.cabeza,'orl':gethistoria.orl,
			'sist_respiratorio':gethistoria.sist_respiratorio,'sist_cardiovascular':gethistoria.sist_cardiovascular,
			'sist_digestivo':gethistoria.sist_digestivo,'sist_genitourinario':gethistoria.sist_genitourinario})

	form2 = addposologiaForm()
	form3 = addremisionForm(initial={'entidad':getorden.paciente.procede})
	form4 = addremisionlabForm()
	posologia = posologias.objects.filter(orden=getorden)
	remisiones = remision.objects.filter(orden=getorden)
	remisioneslab = remisionlab.objects.filter(orden=getorden)

	ctx = {'getorden':getorden,'historial':historial,'lista_proc':lista_proc,'form1':form1,'form2':form2,'form3':form3,'form4':form4,'posologia':posologia,'remisiones':remisiones,'remisioneslab':remisioneslab,'exito':exito,'error':error}
	return render_to_response('home/addHistorias.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def add_procedimientoOrden_view(request,id_prod):
	exito = False
	if request.method == "POST":
		if 'btntabhistoria' in request.POST:
			getorden= orden.objects.get(pk=id_prod)
			historial = historia_clinica.objects.filter(paciente=getorden.paciente) #Se obtiene informacion de la orden
			lista_proc = historia_procedimientos.objects.filter(paciente=getorden.paciente)
			try: #Verifica si existe para editarlo, de lo contrario se puede crear uno nuevo
				getprocedimiento = historia_procedimientos.objects.get(orden=getorden)
				form1 = addhistoria_procedimientosForm(request.POST,instance=getprocedimiento)
				if form1.is_valid():
					exito = True
			except:
				form1 = addhistoria_procedimientosForm(request.POST)
				if form1.is_valid():
					t_diagnostico = request.POST['diagnostico']
					t_diagnostico1 = request.POST['diagnostico1']
					t_complicacion = request.POST['complicacion']
					if t_diagnostico == "":
						getdiagnostico = None
					else:
						getdiagnostico = cie.objects.get(pk=t_diagnostico)

					if t_diagnostico1 == "":
						getdiagnostico1 = None
					else:
						getdiagnostico1 = cie.objects.get(pk=t_diagnostico1)

					if t_complicacion == "":
						getcomplicacion = None
					else:
						getcomplicacion = cie.objects.get(pk=t_complicacion)

					add = form1.save(commit=False)
					add.paciente = getorden.paciente
					add.orden = getorden
					add.procedimiento = getorden.procedimiento
					add.diagnostico = getdiagnostico
					add.diagnostico1 = getdiagnostico1
					add.complicacion = getcomplicacion
					add.save() # Guardamos la informacion
					getorden.status = 'R' #Se coloca la orden como realizada
					getorden.save()
					exito = True

			ctx = {'getorden':getorden,'historial':historial,'lista_proc':lista_proc,'form1':form1,'exito':exito}
			return render_to_response('home/addHistoriasProcedimiento.html',ctx,context_instance=RequestContext(request))

	getorden = orden.objects.get(pk=id_prod) #Se obtiene informacion de la orden
	lista_items = getorden.procedimiento.items.all()
	cadena = ""
	first = True
	for p in lista_items:
		cadena = cadena + p.nombre + "\n" + p.descripcion + "\n\n"

	datos_items = {'hallazgos':cadena,'impresion':"", 'remision':""}
	historial = historia_clinica.objects.filter(paciente=getorden.paciente) #Se obtiene informacion de la orden
	lista_proc = historia_procedimientos.objects.filter(paciente=getorden.paciente)
	form1 = addhistoria_procedimientosForm(initial=datos_items)
	ctx = {'getorden':getorden,'historial':historial,'lista_proc':lista_proc,'form1':form1,'exito':exito}
	return render_to_response('home/addHistoriasProcedimiento.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def edit_procedimientoOrden_view(request,id_prod):
	exito = False
	info = True
	if request.method == "POST":
		if 'btntabhistoria' in request.POST:
			getorden= orden.objects.get(pk=id_prod)
			getprocedimiento = historia_procedimientos.objects.get(orden=getorden)
			historial = historia_clinica.objects.filter(paciente=getorden.paciente)
			lista_proc = historia_procedimientos.objects.filter(paciente=getorden.paciente)
			form1 = addhistoria_procedimientosForm(request.POST,instance=getprocedimiento)
			if form1.is_valid():
				t_diagnostico = request.POST['diagnostico']
				t_diagnostico1 = request.POST['diagnostico1']
				t_complicacion = request.POST['complicacion']
				if t_diagnostico == "":
					getdiagnostico = None
				else:
					getdiagnostico = cie.objects.get(pk=t_diagnostico)

				if t_diagnostico1 == "":
					getdiagnostico1 = None
				else:
					getdiagnostico1 = cie.objects.get(pk=t_diagnostico1)

				if t_complicacion == "":
					getcomplicacion = None
				else:
					getcomplicacion = cie.objects.get(pk=t_complicacion)

				add = form1.save(commit=False)
				add.diagnostico = getdiagnostico
				add.diagnostico1 = getdiagnostico1
				add.complicacion = getcomplicacion
				add.save() # Guardamos la informacion
				exito = True

			ctx = {'getorden':getorden,'historial':historial,'lista_proc':lista_proc,'form1':form1,'exito':exito,'info':info}
			return render_to_response('home/addHistoriasProcedimiento.html',ctx,context_instance=RequestContext(request))

	getorden = orden.objects.get(pk=id_prod) #Se obtiene informacion de la orden
	getprocedimiento = historia_procedimientos.objects.get(orden=getorden)
	historial = historia_clinica.objects.filter(paciente=getorden.paciente) #Se obtiene informacion de la orden
	lista_proc = historia_procedimientos.objects.filter(paciente=getorden.paciente)
	form1 = addhistoria_procedimientosForm(instance=getprocedimiento)
	ctx = {'getorden':getorden,'historial':historial,'lista_proc':lista_proc,'form1':form1,'exito':exito,'info':info}
	return render_to_response('home/addHistoriasProcedimiento.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def show_procedimientoOrden_view(request,id_prod):
	getorden = orden.objects.get(pk=id_prod) #Se obtiene informacion de la orden
	getprocedimiento = historia_procedimientos.objects.get(orden=getorden)
	historial = historia_clinica.objects.filter(paciente=getorden.paciente) #Se obtiene informacion de la orden
	lista_proc = historia_procedimientos.objects.filter(paciente=getorden.paciente)
	form1 = addhistoria_procedimientosForm(instance=getprocedimiento)

	ctx = {'getorden':getorden,'getprocedimiento':getprocedimiento,'historial':historial,'lista_proc':lista_proc,'form1':form1}
	return render_to_response('home/showHistoriasProcedimiento.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def add_orden_view(request,id_prod):
	temp = paciente.objects.get(pk=id_prod)
	if request.method == "POST":
		form = addOrdenSiomForm(request.POST)
		if form.is_valid():
			add = form.save(commit=False)
			add.paciente = temp
			add.generadapor = request.user
			add.save() # Guardamos la informacion
			return HttpResponseRedirect('/add/servicios/%s/%s/' % (id_prod,add.id))

		usuario = User.objects.get(pk=request.user.id)
		i_u = userProfile.objects.get(user=usuario)
		form.fields["institucion"].queryset = instituciones.objects.filter(pk=i_u.institucion.id)
		form.fields["empresa"].queryset = i_u.institucion.empresas
		form.fields["medico"].queryset = medico.objects.filter(institucion = i_u.institucion)
		ctx = {'form':form,'temp':temp}
		return render_to_response('home/addordenSiom.html',ctx,context_instance=RequestContext(request))
	else:
		form = addOrdenSiomForm()

	usuario = User.objects.get(pk=request.user.id)
	i_u = userProfile.objects.get(user=usuario)
	form.fields["institucion"].queryset = instituciones.objects.filter(pk=i_u.institucion.id)
	form.fields["empresa"].queryset = i_u.institucion.empresas
	form.fields["medico"].queryset = medico.objects.filter(institucion = i_u.institucion)
	ctx = {'form':form,'temp':temp}
	return render_to_response('home/addordenSiom.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def add_servicios_view(request, id_prod, id_orden):
	temp = paciente.objects.get(pk=id_prod)
	getorden = orden.objects.get(pk=id_orden)
	if request.method == "POST":
		form = addOrdenProductoForm(request.POST)
		if form.is_valid():
			add = form.save(commit=False)
			add.orden = getorden
			add.save() # Guardamos la informacion

	form = addOrdenProductoForm()
	form.fields["servicio"].queryset = serviciosEmpresa.objects.filter(empresa=getorden.empresa)
	lista = ordenesProducto.objects.filter(orden = getorden)
	ctx = {'getorden':getorden,'form':form,'temp':temp,'lista':lista}
	return render_to_response('home/addordenServicios.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def borrar_servicio_view(request,id_orden,id_servicio):
	getorden = orden.objects.get(pk=id_orden)
	p = ordenesProducto.objects.get(pk=id_servicio)
	p.delete() # Elinamos objeto de la base de datos
	return HttpResponseRedirect('/add/servicios/%s/%s/' % (getorden.paciente.id,getorden.id))

@login_required(login_url=URL_LOGIN)
def finalizar_view(request, id_orden):
	_orden = get_object_or_404(orden, pk=id_orden)
	#getorden.status = 'R'
	#getorden.save() # Elinamos objeto de la base de datos
	_visiometrias = [
		Visiometria.get_visiometria_servicio(), Visiometria.get_optometria_servicio()
	]

	url = ''
	params = ''
	if _orden.OrdenProducto_orden.filter(servicio__nombre__in=_visiometrias).exists():
		url = reverse('examenes:visiometria_nueva', args=(id_orden, ))
		params += 'visiometria=True&'
	if _orden.OrdenProducto_orden.filter(servicio__nombre=Audiometria.get_audiometria_servicio()).exists():
		url = reverse('examenes:visiometria_nueva', args=(id_orden, ))
		params += 'audiometria=True'
	if url:
		return redirect('%s?%s' % (url, params))
	return HttpResponseRedirect('/pacientes/page/1/')

@login_required(login_url=URL_LOGIN)
def ordenes_view(request):
	error = False
	if request.method == "POST":
		fi = request.POST['fechai']
		ff = request.POST['fechaf']
		t_orden = request.POST['numero']
		usuario = User.objects.get(pk=request.user.id)
		i_u = userProfile.objects.get(user=usuario)
		form2 = filtroOrdenForm(request.POST)
		form3 = serviciosForm(request.POST)
		empresa = request.POST['empresa']
		institucion = request.POST['institucion']
		servicio = request.POST['nombre']
		if servicio != "":
			n_servicio = servicios.objects.get(id=servicio)

		if (fi == "") & (ff == "") & (t_orden == ""):
			error = True
		elif (fi == "") & (ff != "") & (t_orden == ""):
			error = True
		elif (fi != "") & (ff == "") & (t_orden == ""):
			error = True
		elif (fi != "") & (ff != "") & (t_orden == ""):
			fi_format = datetime.datetime.strptime(fi, '%Y-%m-%d').date()
			ff_format = datetime.datetime.strptime(ff, '%Y-%m-%d').date()
			ff_format = ff_format + timedelta(days=1)
			if (empresa != "") & (institucion != ""):
				if request.user.has_perm("home.es_administrador"): #Si es administrador le deben salir todas las ordenes
					ordenes = orden.objects.filter(fecha__range=(fi_format,ff_format),empresa=empresa, institucion=institucion).order_by('fecha')
				else:
					ordenes = orden.objects.filter(fecha__range=(fi_format,ff_format),institucion=i_u.institucion, empresa=empresa).order_by('fecha')
			else:
				if request.user.has_perm("home.es_administrador"): #Si es administrador le deben salir todas las ordenes
					ordenes = orden.objects.filter(fecha__range=(fi_format,ff_format)).order_by('fecha')
				else:
					ordenes = orden.objects.filter(fecha__range=(fi_format,ff_format),institucion=i_u.institucion).order_by('fecha')
			lista=[]
			ordenes = ordenes.select_related(
				'paciente', 'empresa', 'institucion').prefetch_related(
					'OrdenProducto_orden').only(
						'paciente__snombre', 'empresa__razon', 'institucion__razon', 'fecha_atencion',
						'empresa_cliente', 'status', 'anulada', 'paciente__pnombre', 'paciente__sapellido',
						'paciente__papellido', 'paciente__cedula'
					)
			for p in ordenes:
				cadena = ""
				existe_servicio = False
				_servicios = serviciosEmpresa.objects.filter(ordenProducto_servicio__in=p.OrdenProducto_orden.all()).select_related('nombre')
				for z in _servicios:
					t = z.nombre.nombre
					if servicio != "":
						if t == n_servicio.nombre:
							existe_servicio = True
					cadena = cadena + z.nombre.nombre + ' | '

				if servicio != "":
					if existe_servicio:
						lista.append({'orden': p,'servicios':cadena})
				else:
					lista.append({'orden': p,'servicios':cadena})

			form = fechaRipsForm(request.POST)
			ctx = {'lista':lista,'form':form,'form2':form2,'form3':form3,'error':error}
			return render_to_response('home/ordenes.html',ctx,context_instance=RequestContext(request))
		else: #Se coloco un numero de orden, se ignoran las fechas y se hace la consulta
			if request.user.has_perm("home.es_administrador"): #Si es administrador le deben salir todas las ordenes
				ordenes = orden.objects.filter(pk = t_orden).order_by('fecha')
			else:
				ordenes = orden.objects.filter(pk = t_orden,institucion=i_u.institucion).order_by('fecha')
			ordenes = ordenes.select_related(
				'paciente', 'empresa', 'institucion').prefetch_related(
					'OrdenProducto_orden').only(
						'paciente__snombre', 'empresa__razon', 'institucion__razon', 'fecha_atencion',
						'empresa_cliente', 'status', 'anulada', 'paciente__pnombre', 'paciente__sapellido',
						'paciente__papellido', 'paciente__cedula'
					)
			lista=[]
			for p in ordenes:
				cadena = ""
				_servicios = serviciosEmpresa.objects.filter(ordenProducto_servicio__in=p.OrdenProducto_orden.all()).select_related('nombre')
				for z in _servicios:
					cadena = cadena + z.nombre.nombre + ' | '
				lista.append({'orden': p,'servicios':cadena})
			form = fechaRipsForm()
			form2 = filtroOrdenForm()
			form3 = serviciosForm()
			ctx = {'lista':lista,'form':form,'form2':form2,'form3':form3,'error':error}
			return render_to_response('home/ordenes.html',ctx,context_instance=RequestContext(request))

	lista = []
	form = fechaRipsForm()
	form2 = filtroOrdenForm()
	form3 = serviciosForm()
	ctx = {'lista':lista,'form':form,'form2':form2,'form3':form3,'error':error}
	return render_to_response('home/ordenes.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def ordenesReporte_view(request):
	error = False
	if request.method == "POST":
		fi = request.POST['fechai']
		ff = request.POST['fechaf']
		t_orden = request.POST['numero']
		usuario = User.objects.get(pk=request.user.id)
		i_u = userProfile.objects.get(user=usuario)
		form2 = filtroOrdenForm(request.POST)
		empresa = request.POST['empresa']
		institucion = request.POST['institucion']
		if (fi == "") & (ff == "") & (t_orden == ""):
			error = True
		elif (fi == "") & (ff != "") & (t_orden == ""):
			error = True
		elif (fi != "") & (ff == "") & (t_orden == ""):
			error = True
		elif (fi != "") & (ff != "") & (t_orden == ""):
			fi_format = datetime.datetime.strptime(fi, '%Y-%m-%d').date()
			ff_format = datetime.datetime.strptime(ff, '%Y-%m-%d').date()
			ff_format = ff_format + timedelta(days=1)
			if (empresa != "") & (institucion != ""):
				if request.user.has_perm("home.es_administrador"): #Si es administrador le deben salir todas las ordenes
					ordenes = ordenesProducto.objects.filter(orden__fecha__range=(fi_format,ff_format),orden__empresa=empresa, orden__institucion=institucion).order_by('orden__fecha')
				else:
					ordenes = ordenesProducto.objects.filter(orden__fecha__range=(fi_format,ff_format), orden__institucion=i_u.institucion, orden__empresa=empresa).order_by('orden_fecha')
			else:
				if request.user.has_perm("home.es_administrador"): #Si es administrador le deben salir todas las ordenes
					ordenes = ordenesProducto.objects.filter(orden__fecha__range=(fi_format,ff_format)).order_by('orden__fecha')
				else:
					ordenes = ordenesProducto.objects.filter(orden__fecha__range=(fi_format,ff_format), orden__institucion=i_u.institucion).order_by('orden__fecha')
			ordenes = ordenes.select_related(
				'orden', 'orden__paciente', 'orden__empresa', 'orden__institucion', 'servicio__nombre')#.only(
						#'paciente__snombre', 'empresa__razon', 'institucion__razon', 'fecha_atencion',
						#'empresa_cliente', 'status', 'anulada', 'paciente__pnombre', 'paciente__sapellido',
						#'paciente__papellido', 'paciente__cedula'
					#)
			lista = ordenes
			form = fechaRipsForm(request.POST)
			ctx = {'lista':lista,'form':form,'form2':form2,'error':error}
			return render_to_response('home/ordenesReporte.html',ctx,context_instance=RequestContext(request))
		else: #Se coloco un numero de orden, se ignoran las fechas y se hace la consulta
			if request.user.has_perm("home.es_administrador"): #Si es administrador le deben salir todas las ordenes
				ordenes = ordenesProducto.objects.filter(orden__pk = t_orden).order_by('orden__fecha')
			else:
				ordenes = ordenesProducto.objects.filter(orden__pk = t_orden, orden__institucion=i_u.institucion).order_by('orden__fecha')
			#lista=[]
			ordenes = ordenes.select_related(
				'orden', 'orden__paciente', 'orden__empresa', 'orden__institucion', 'servicio__nombre')
			lista = ordenes
			form = fechaRipsForm()
			form2 = filtroOrdenForm()
			ctx = {'lista':lista,'form':form,'form2':form2,'error':error}
			return render_to_response('home/ordenesReporte.html',ctx,context_instance=RequestContext(request))

	lista = []
	form = fechaRipsForm()
	form2 = filtroOrdenForm()
	ctx = {'lista':lista,'form':form,'form2':form2,'error':error}
	return render_to_response('home/ordenesReporte.html',ctx,context_instance=RequestContext(request))


@login_required(login_url=URL_LOGIN)
def edit_orden_view(request,id_prod):
	getorden = orden.objects.get(pk=id_prod)
	temp = getorden.paciente
	if request.method == "POST":
		form = addOrdenSiomForm(request.POST,instance=getorden)
		if form.is_valid():
			form.save() # Guardamos la informacion
			return HttpResponseRedirect('/add/servicios/%s/%s/' % (temp.id,id_prod))
	else:
		form = addOrdenSiomForm(instance=getorden)

	ctx = {'form':form,'temp':temp}
	return render_to_response('home/addordenSiom.html',ctx,context_instance=RequestContext(request))


@login_required(login_url=URL_LOGIN)
def anula_orden_view(request,id_prod):
	info=""
	getorden = orden.objects.get(pk=id_prod)
	temp = getorden.paciente
	if request.method == "POST":
		form = addOrdenAnulaForm(request.POST,instance=getorden)
		if form.is_valid():
			form.save() # Guardamos la informacion
			info = "Guardado satisfactoriamente"
			return HttpResponseRedirect('/ordenes/')
	else:
		form = addOrdenAnulaForm(instance=getorden)

	ctx = {'form':form,'informacion':info,'temp':temp}
	return render_to_response('home/anula_orden.html',ctx,context_instance=RequestContext(request))


def consulta_especialidad_view(request):
	prod = especialidades.objects.filter(nombre = request.GET['temp_especialidad'])
	data = serializers.serialize('json',prod,fields=('codigo'))
	return HttpResponse(data, content_type='application/json')

def consulta_procedimiento_view(request):
	prod = procedimientos.objects.get(pk = request.GET['id'])
	empresa = empresas.objects.get(pk = request.GET['empresa'])
	uvr = prod.uvr
	#Aqui se Consulta cual tipo de tarifa tiene (2001 o 2004) consultando la empresa
	if empresa.tipo_tarifa == '1':	#Tarifa ISS 2001
		incremento = empresa.plan.porcentaje
		t_honorarios = honorarios.objects.get(ref='39101') #Valor 1270
		valor_uvr = t_honorarios.valor
		honorario = uvr*valor_uvr
		honorario = honorario + honorario*incremento
		t_sala = sala.objects.get(lim_1__lte=uvr, lim_2__gte=uvr)
		valor_sala = t_sala.valor
		valor_sala = valor_sala + valor_sala*incremento
		t_sutura = sutura.objects.get(ref='39315') #Sutura
		valor_sutura = t_sutura.valor
		valor_sutura = valor_sutura + valor_sutura*incremento
		#Aqui se calcula el total incluyendo el incremento del plan
		total = honorario + valor_sala + valor_sutura
		valor = '%.2f' % total
	else:
		pass

	from django.core.serializers.json import DjangoJSONEncoder
	data = []
	data.append({'tarifa': valor,})
	return HttpResponse(simplejson.dumps(data, cls=DjangoJSONEncoder), content_type='application/json')
	#data = serializers.serialize('json',prod,fields=('tarifa'))
	#return HttpResponse(data, content_type='application/json')

def consulta_consulta_view(request):
	prod = consultas.objects.filter(pk = request.GET['id'])
	data = serializers.serialize('json',prod,fields=('tarifa'))
	return HttpResponse(data, content_type='application/json')

def consulta_plan_view(request):
	prod = empresas.objects.filter(pk = request.GET['valor'])
	for p in prod:
		t_plan = p

	prod2 = planes_salud.objects.filter(descripcion = t_plan.plan)
	data = serializers.serialize('json',prod2,fields=('porcentaje'))
	return HttpResponse(data, content_type='application/json')

def consulta_empresa_view(request):
	#En el front se hizo validacion para que siempre exista empresa en esta consulta
	t_empresa = empresas.objects.filter(pk = request.GET['id_empresa'])
	data = serializers.serialize('json',t_empresa,fields=('valor_sedacion'))
	return HttpResponse(data, content_type='application/json')

def rango_procedimiento_view(request):
	prod = rango_procedimiento.objects.filter(descripcion = request.GET['id'])
	data = serializers.serialize('json',prod,fields=('porcentaje'))
	return HttpResponse(data, content_type='application/json')

def rango_consulta_view(request):
	prod = rango_consulta.objects.filter(descripcion = request.GET['id'])
	data = serializers.serialize('json',prod,fields=('cuota'))
	return HttpResponse(data, content_type='application/json')

#Consultas ajax que se hacen en las historias clinicas
def borrar_posologia_view(request):
	if request.method=="POST":
		try:
			id_posologia = request.POST['id']
			p = posologias.objects.get(pk=id_posologia)
			mensaje = {"status":"True","product_id":p.id}
			p.delete() # Elinamos objeto de la base de datos
			return HttpResponse(simplejson.dumps(mensaje),content_type='application/json')
		except:
			mensaje = {"status":"False"}
			return HttpResponse(simplejson.dumps(mensaje),content_type='application/json')

def agregar_posologia_view(request):
	if request.method=="POST":
		try:
			id_orden = request.POST['id_orden']
			getorden= orden.objects.get(pk=id_orden)
			p = posologias(orden=getorden, medicamento= request.POST['medicamento'], uso= request.POST['uso'])
			p.save() # Guardamos la informacion
			mensaje = {"status":"True",'id_posologia':p.id}
			return HttpResponse(simplejson.dumps(mensaje),content_type='application/json')
		except:
			mensaje = {"status":"False"}
			return HttpResponse(simplejson.dumps(mensaje),content_type='application/json')

def agregar_remision_view(request):
	if request.method=="POST":
		try:
			id_orden = request.POST['id_orden']
			getorden= orden.objects.get(pk=id_orden)
			p = remision(orden=getorden, ordenado= request.POST['ordenado'], descripcion_orden= request.POST['descripcion_orden'], entidad= request.POST['entidad'])
			p.save() # Guardamos la informacion
			mensaje = {"status":"True",'id_remision':p.id}
			return HttpResponse(simplejson.dumps(mensaje),content_type='application/json')
		except:
			mensaje = {"status":"False"}
			return HttpResponse(simplejson.dumps(mensaje),content_type='application/json')

def borrar_remision_view(request):
	if request.method=="POST":
		try:
			id_remision = request.POST['id']
			p = remision.objects.get(pk=id_remision)
			mensaje = {"status":"True","remision_id":p.id}
			p.delete() # Elinamos objeto de la base de datos
			return HttpResponse(simplejson.dumps(mensaje),content_type='application/json')
		except:
			mensaje = {"status":"False"}
			return HttpResponse(simplejson.dumps(mensaje),content_type='application/json')

def agregar_laboratorio_view(request):
	if request.method=="POST":
		try:
			id_orden = request.POST['id_orden']
			getorden= orden.objects.get(pk=id_orden)
			p = remisionlab(orden=getorden, laboratorio= request.POST['laboratorio'])
			p.save() # Guardamos la informacion
			mensaje = {"status":"True",'id_laboratorio':p.id}
			return HttpResponse(simplejson.dumps(mensaje),content_type='application/json')
		except:
			mensaje = {"status":"False"}
			return HttpResponse(simplejson.dumps(mensaje),content_type='application/json')

def borrar_laboratorio_view(request):
	if request.method=="POST":
		try:
			id_laboratorio = request.POST['id']
			p = remisionlab.objects.get(pk=id_laboratorio)
			mensaje = {"status":"True","laboratorio_id":p.id}
			p.delete() # Elinamos objeto de la base de datos
			return HttpResponse(simplejson.dumps(mensaje),content_type='application/json')
		except:
			mensaje = {"status":"False"}
			return HttpResponse(simplejson.dumps(mensaje),content_type='application/json')

def consulta_cie_view(request):
	buscar = request.GET['term']
	resultado = cie.objects.filter(Q(descripcion__icontains=buscar) | Q(codigo__icontains=buscar)).order_by('descripcion')
	data = []
	for p in resultado:
		descripcion = '%s %s' % (p.codigo,p.descripcion)
		data.append({'id': p.id,'text':descripcion,})

	from django.core.serializers.json import DjangoJSONEncoder
	return HttpResponse(simplejson.dumps(data, cls=DjangoJSONEncoder), content_type='application/json')

#Consultas ajax que se hacen para conocer los historiales de los pacientes
def muestra_historia_view(request):
	gethistoria = historia_clinica.objects.get(pk = request.GET['id_historia'])
	num = gethistoria.concepto
	if num == '1':
		concepto = 'Apto'
	elif num =='2':
		concepto = 'Apto para trabajar en altura'
	elif num =='3':
		concepto = 'Apto para manipulacion de alimentos'
	elif num =='4':
		concepto = 'Apto con recomendaciones de seguimiento'
	elif num =='5':
		concepto = 'Apto con patologia que no interfieren con el cargo'
	elif num =='6':
		concepto = 'Apto con restricciones'
	else:
		concepto = 'Aplazado'

	data = {
		'concepto':concepto,'talla':gethistoria.talla,'peso':gethistoria.peso,
		'presion_arterial':gethistoria.presion_arterial,'masa_corporal':gethistoria.masa_corporal,
		'temperatura':gethistoria.temperatura,'pulso':gethistoria.pulso,
	}
	json_data = json.dumps(data) #Convierte diccionario python a json
	return HttpResponse(json_data,content_type='application/json')

def muestra_procedimiento_view(request):
	getprocedimiento = historia_procedimientos.objects.filter(pk = request.GET['id_historia'])
	data = serializers.serialize('json',getprocedimiento,fields=('hallazgos','impresion'))
	return HttpResponse(data, content_type='application/json')

#Impresion de Documentos
from mysite.apps.historias.funciones_imprimir import ImprimeRecibo, ImprimeHistoria, ImprimeConcepto, ImprimeOrden, ImprimeProcedimiento

def imprimir_recibo_view(request,id_prod):
	t_orden = orden.objects.get(pk = id_prod)
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="Orden_%s.pdf"' % t_orden.id

	ips = instituciones.objects.get(pk='1')

	t_titulo = ips.razon
	t_nit = ips.numero
	t_empresa = t_orden.empresa
	t_no_orden = t_orden.id
	t_pageinfo = ips.direccion
	t_telefono = ips.telefono
	t_fecha = t_orden.fecha
	t_cedula = t_orden.paciente
	t_procedimiento = "Ver Relacion"
	t_cancela = 0

	t_particular = 0
	#************************************************************
	t_sala = 0 #Aqui hay que ver que es lo que se debe consultar
	# Pues no entiendo este item
	#************************************************************
	t_generadapor = t_orden.generadapor

	ImprimeRecibo(response, t_titulo, t_nit, t_no_orden, t_pageinfo, t_telefono, t_fecha, t_cedula, t_procedimiento, t_empresa, t_cancela, t_particular, t_sala, t_generadapor)
	return response

def imprimir_historia_view(request,id_prod):
	t_orden = orden.objects.get(pk = id_prod) #Buscar si la historia existe
	#try:
	t_historia = historia_clinica.objects.get(orden = t_orden)
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="Historia_Clinica_%s.pdf"' % t_historia.id
	ImprimeHistoria(response, id_prod)
	'''
	except:
		response = HttpResponse(content_type='application/pdf')
		response['Content-Disposition'] = 'attachment; filename="Historia_Clinica_Sin_Datos.pdf"'
		p = canvas.Canvas(response)
		p.drawString(100, 800, "No hay datos para mostrar, verificar configuracion.")
		p.showPage()
		p.save()
	'''

	return response

def imprimir_concepto_view(request,id_prod):
	t_orden = orden.objects.get(pk = id_prod) #Buscar si la historia existe
	try:
		t_historia = historia_clinica.objects.get(orden = t_orden)
		response = HttpResponse(content_type='application/pdf')
		response['Content-Disposition'] = 'attachment; filename="Concepto_Medico_%s.pdf"' % t_historia.id
		ImprimeConcepto(response, id_prod)
	except:
		response = HttpResponse(content_type='application/pdf')
		response['Content-Disposition'] = 'attachment; filename="Concepto_Medico_Sin_Datos.pdf"'
		p = canvas.Canvas(response)
		p.drawString(100, 800, "No hay datos para mostrar, verificar configuracion.")
		p.showPage()
		p.save()

	return response

def imprimir_medicamentos_view(request,id_prod):
	t_orden = orden.objects.get(pk = id_prod)  #Buscar si la historia existe
	try:
		t_historia = historia_clinica.objects.get(orden = t_orden)
		response = HttpResponse(content_type='application/pdf')
		response['Content-Disposition'] = 'attachment; filename="Medicamentos_Historia_%s.pdf"' % t_historia.id
		ImprimeOrden(response, id_prod, 1) #Imprime medicamentos, la opcion 1 indica que son medicentos
	except:
		response = HttpResponse(content_type='application/pdf')
		response['Content-Disposition'] = 'attachment; filename="Historia_Clinica_Sin_Datos.pdf"'
		p = canvas.Canvas(response)
		p.drawString(100, 800, "No hay datos para mostrar, la historia no ha sido creada.")
		p.showPage()
		p.save()

	return response

def imprimir_ordenamientos_view(request,id_prod):
	t_orden = orden.objects.get(pk = id_prod) #Buscar si la historia existe
	try:
		t_historia = historia_clinica.objects.get(orden = t_orden)
		response = HttpResponse(content_type='application/pdf')
		response['Content-Disposition'] = 'attachment; filename="Ordenamientos_Historia_%s.pdf"' % t_historia.id
		ImprimeOrden(response, id_prod, 2) #Imprime ordenamientos, la opcion 2 indica que son ordenamientos
	except:
		response = HttpResponse(content_type='application/pdf')
		response['Content-Disposition'] = 'attachment; filename="Historia_Clinica_Sin_Datos.pdf"'
		p = canvas.Canvas(response)
		p.drawString(100, 800, "No hay datos para mostrar, la historia no ha sido creada.")
		p.showPage()
		p.save()

	return response

def imprimir_laboratorios_view(request,id_prod):
	t_orden = orden.objects.get(pk = id_prod) #Buscar si la historia existe
	try:
		t_historia = historia_clinica.objects.get(orden = t_orden)
		response = HttpResponse(content_type='application/pdf')
		response['Content-Disposition'] = 'attachment; filename="Laboratorios_Historia_%s.pdf"' % t_historia.id
		ImprimeOrden(response, id_prod, 3) #Imprime Laboratorios, la opcion 3 indica que son laboratorios
	except:
		response = HttpResponse(content_type='application/pdf')
		response['Content-Disposition'] = 'attachment; filename="Historia_Clinica_Sin_Datos.pdf"'
		p = canvas.Canvas(response)
		p.drawString(100, 800, "No hay datos para mostrar, verificar configuracion.")
		p.showPage()
		p.save()

	return response

def imprimir_remision_view(request,id_prod):
	t_orden = orden.objects.get(pk = id_prod) #Buscar si la historia existe
	try:
		t_historia = historia_clinica.objects.get(orden = t_orden)
		response = HttpResponse(content_type='application/pdf')
		response['Content-Disposition'] = 'attachment; filename="Remision_Historia_%s.pdf"' % t_historia.id
		ImprimeOrden(response, id_prod, 4) #Imprime Remision, la opcion 4 indica que es remision
	except:
		response = HttpResponse(content_type='application/pdf')
		response['Content-Disposition'] = 'attachment; filename="Historia_Clinica_Sin_Datos.pdf"'
		p = canvas.Canvas(response)
		p.drawString(100, 800, "No hay datos para mostrar, verificar configuracion.")
		p.showPage()
		p.save()

	return response

def imprimir_procedimiento_view(request,id_prod):
	#Buscar si la historia existe
	t_orden = orden.objects.get(pk = id_prod)
	try:
		t_procedimiento = historia_procedimientos.objects.get(orden = t_orden)
		response = HttpResponse(content_type='application/pdf')
		response['Content-Disposition'] = 'attachment; filename="Procedimiento_%s.pdf"' % t_procedimiento.id
		ImprimeProcedimiento(response, id_prod)
	except:
		response = HttpResponse(content_type='application/pdf')
		response['Content-Disposition'] = 'attachment; filename="Procedimiento_Sin_Datos.pdf"'
		p = canvas.Canvas(response)
		p.drawString(100, 800, "No hay datos para mostrar, el procedimiento no ha sido creado.")
		p.showPage()
		p.save()

	return response

#Creacion de Rips
def crear_rips_view(request):
	error = False
	pendiente = False
	#Es un POST*****************************************************
	if request.method=="POST":
		fi = request.POST['fechai']
		ff = request.POST['fechaf']
		fr = request.POST['fecha_r']
		t_inst = request.POST['institucion']
		t_empr = request.POST['empresa']
		t_tipo = request.POST['tipo']
		t_consecutivo = request.POST['consecutivo']
		if (fi == "") | (ff == "") | (fr == "") | (t_consecutivo == ""): #Validacion de fecha y consecutivo
			error = True
		else:
			if (t_inst == "-1") | (t_empr == "-1") : #Validacion de seleccion institucion y empresa
				error = True
			else: #Si todas las validaciones son correctas entonces verifica si puede generar rips
				fi_format = datetime.datetime.strptime(fi, '%Y-%m-%d').date()
				ff_format = datetime.datetime.strptime(ff, '%Y-%m-%d').date()
				fr_format = datetime.datetime.strptime(fr, '%Y-%m-%d').date()
				fi_format = fi_format.strftime("%d/%m/%Y")
				ff_format = ff_format.strftime("%d/%m/%Y")
				fr_format = fr_format.strftime("%d/%m/%Y")
				listado = orden.objects.filter(status = 'R', fecha__gte = fi, fecha__lte = ff, institucion = t_inst, empresa = t_empr, tipo_usuario = t_tipo).exclude(pendiente_autoriza = False)
				if not listado: #No existen ordenes pendientes, se puede generar rips
					#Se Generan Rips de acuerdo a opciones escogidas******************************************
					opcion_escogida = request.POST['archivo']
					if opcion_escogida == '1': #Se escogio archivo de consultas
						listado = historia_clinica.objects.filter(orden__status = 'R', orden__fecha__gte = fi, orden__fecha__lte = ff, orden__institucion = t_inst, orden__empresa = t_empr, orden__tipo_usuario = t_tipo)
						response = HttpResponse(content_type='text/csv')
						t_archivo = 'attachment; filename="AC%s.txt"' %(t_consecutivo)
						response['Content-Disposition'] = t_archivo
						writer = csv.writer(response)
						for p in listado:
							if not p.diagnostico1:
								diagnostico1 = ""
							else:
								diagnostico1 = p.diagnostico1.codigo

							if not p.diagnostico2:
								diagnostico2 = ""
							else:
								diagnostico2 = p.diagnostico2.codigo

							if not p.diagnostico3:
								diagnostico3 = ""
							else:
								diagnostico3 = p.diagnostico3.codigo

							writer.writerow([p.orden.id,p.orden.empresa.codigo,p.paciente.documento,p.paciente.cedula,
								p.orden.fecha_atencion.strftime("%d/%m/%Y"),p.orden.id,p.orden.consulta.codigo,p.finalidad,
								p.causa_externa,p.diagnostico.codigo,diagnostico1,diagnostico2,diagnostico3,
								p.tipo_diagnostico,p.orden.valor,p.orden.couta,p.orden.total])
						return response
					elif opcion_escogida == '2': #Se escogio archivo de procedimientos
						listado = historia_procedimientos.objects.filter(orden__status = 'R', orden__fecha__gte = fi, orden__fecha__lte = ff, orden__institucion = t_inst, orden__empresa = t_empr, orden__tipo_usuario = t_tipo)
						response = HttpResponse(content_type='text/csv')
						t_archivo = 'attachment; filename="AP%s.txt"' %(t_consecutivo)
						response['Content-Disposition'] = t_archivo
						writer = csv.writer(response)
						for p in listado:
							if not p.diagnostico:
								diagnostico = ""
							else:
								diagnostico = p.diagnostico.codigo

							if not p.diagnostico1:
								diagnostico1 = ""
							else:
								diagnostico1 = p.diagnostico1.codigo

							if not p.complicacion:
								complicacion = ""
							else:
								complicacion = p.complicacion.codigo

							writer.writerow([p.orden.id,p.orden.empresa.codigo,p.paciente.documento,p.paciente.cedula,
								p.orden.fecha_atencion	,p.orden.id,p.orden.procedimiento.codigo,p.ambito,p.finalidad,
								p.personal,diagnostico,diagnostico1,complicacion, p.forma,p.orden.valor])
						return response
					elif opcion_escogida == '3': #Se escogio archivo de facturacion
						listado = factura.objects.filter(orden__status = 'R', orden__fecha__gte = fi, orden__fecha__lte = ff, orden__institucion = t_inst, orden__empresa = t_empr, orden__tipo_usuario = t_tipo)
						response = HttpResponse(content_type='text/csv')
						t_archivo = 'attachment; filename="AF%s.txt"' %(t_consecutivo)
						response['Content-Disposition'] = t_archivo
						writer = csv.writer(response)
						for p in listado:
							num = "%s-%s" %(p.letra_factura,p.numero)
							writer.writerow([p.orden.institucion.codigo,p.orden.institucion.razon,p.orden.institucion.documento,
								p.orden.institucion.numero,num,p.fecha_emision.strftime("%d/%m/%Y"),fi_format,ff_format,p.orden.empresa.codigo,p.orden.empresa.razon,
								p.orden.empresa.contrato,p.orden.empresa.plan_beneficios,p.orden.empresa.poliza,p.orden.copago,"","",
								p.orden.total])
						return response
					elif opcion_escogida =='4':
						temp = historia_clinica.objects.filter(orden__status = 'R', orden__fecha__gte = fi, orden__fecha__lte = ff, orden__institucion = t_inst, orden__empresa = t_empr, orden__tipo_usuario = t_tipo)
						usuarios = []
						for q in temp:
							coincidencia = False
							if not usuarios:
								usuarios.append({"empresa":q.orden.empresa,'paciente':q.paciente,'tipo':q.orden.tipo_usuario})
							else:
								for z in usuarios:
									if z["paciente"] == q.paciente:
										coincidencia = True
								if not coincidencia:
									usuarios.append({"empresa":q.orden.empresa,'paciente':q.paciente,'tipo':q.orden.tipo_usuario})
						temp = historia_procedimientos.objects.filter(orden__status = 'R', orden__fecha__gte = fi, orden__fecha__lte = ff, orden__institucion = t_inst, orden__empresa = t_empr, orden__tipo_usuario = t_tipo)
						for q in temp:
							coincidencia = False
							if not usuarios:
								usuarios.append({"empresa":q.orden.empresa,'paciente':q.paciente,'tipo':q.orden.tipo_usuario})
							else:
								for z in usuarios:
									if z["paciente"] == q.paciente:
										coincidencia = True
								if not coincidencia:
									usuarios.append({"empresa":q.orden.empresa,'paciente':q.paciente,'tipo':q.orden.tipo_usuario})
						response = HttpResponse(content_type='text/csv')
						t_archivo = 'attachment; filename="US%s.txt"' %(t_consecutivo)
						response['Content-Disposition'] = t_archivo
						writer = csv.writer(response)
						for p in usuarios:
							writer.writerow([p["paciente"].documento,p["paciente"].cedula,p["empresa"].codigo,p["tipo"],p["paciente"].papellido,
								p["paciente"].sapellido,p["paciente"].pnombre,p["paciente"].snombre,p["paciente"].edad,p["paciente"].unidad,
								p["paciente"].genero,p["paciente"].ciudad.codigo,p["paciente"].ciudad.codigo_municipio,p["paciente"].zona])
						return response
					elif opcion_escogida =='5':
						temp = historia_clinica.objects.filter(orden__status = 'R', orden__fecha__gte = fi, orden__fecha__lte = ff, orden__institucion = t_inst, orden__empresa = t_empr, orden__tipo_usuario = t_tipo).count()
						t_hclinicas = temp
						temp = historia_procedimientos.objects.filter(orden__status = 'R', orden__fecha__gte = fi, orden__fecha__lte = ff, orden__institucion = t_inst, orden__empresa = t_empr, orden__tipo_usuario = t_tipo).count()
						t_hprocedimiento = temp
						temp = factura.objects.filter(orden__status = 'R', orden__fecha__gte = fi, orden__fecha__lte = ff, orden__institucion = t_inst, orden__empresa = t_empr, orden__tipo_usuario = t_tipo).count()
						t_factura = temp
						temp = historia_clinica.objects.filter(orden__status = 'R', orden__fecha__gte = fi, orden__fecha__lte = ff, orden__institucion = t_inst, orden__empresa = t_empr, orden__tipo_usuario = t_tipo)
						usuarios = []
						for q in temp:
							coincidencia = False
							if not usuarios:
								usuarios.append({"empresa":q.orden.empresa,'paciente':q.paciente,'tipo':q.orden.tipo_usuario})
							else:
								for z in usuarios:
									if z["paciente"] == q.paciente:
										coincidencia = True
								if not coincidencia:
									usuarios.append({"empresa":q.orden.empresa,'paciente':q.paciente,'tipo':q.orden.tipo_usuario})
						temp = historia_procedimientos.objects.filter(orden__status = 'R', orden__fecha__gte = fi, orden__fecha__lte = ff, orden__institucion = t_inst, orden__empresa = t_empr, orden__tipo_usuario = t_tipo)
						for q in temp:
							coincidencia = False
							if not usuarios:
								usuarios.append({"empresa":q.orden.empresa,'paciente':q.paciente,'tipo':q.orden.tipo_usuario})
							else:
								for z in usuarios:
									if z["paciente"] == q.paciente:
										coincidencia = True
								if not coincidencia:
									usuarios.append({"empresa":q.orden.empresa,'paciente':q.paciente,'tipo':q.orden.tipo_usuario})
						t_usuarios = len(usuarios)
						t_institucion = instituciones.objects.get(pk=t_inst)
						response = HttpResponse(content_type='text/csv')
						t_archivo = 'attachment; filename="CT%s.txt"' %(t_consecutivo)
						response['Content-Disposition'] = t_archivo
						s_consulta = 'AC%s' %(t_consecutivo)
						s_procedimiento = 'AP%s' %(t_consecutivo)
						s_usuario = 'US%s' %(t_consecutivo)
						s_facturacion = 'AF%s' %(t_consecutivo)
						writer = csv.writer(response)
						writer.writerow([t_institucion.codigo,fr_format,s_consulta,t_hclinicas])
						writer.writerow([t_institucion.codigo,fr_format,s_procedimiento,t_hprocedimiento])
						writer.writerow([t_institucion.codigo,fr_format,s_usuario,t_usuarios])
						writer.writerow([t_institucion.codigo,fr_format,s_facturacion,t_factura])
						return response
					#******************************************************************************************
				else: #Se encontraron ordenes pendientes por numero de autorizacion, no se puede generar el rips
					pendiente = True
					lista_instituciones = instituciones.objects.all()
					form = fechaRipsForm(request.POST)
					ctx = {'form':form,'lista_instituciones':lista_instituciones,'error':error,'pendiente':pendiente}
					return render_to_response('home/crearRips.html',ctx,context_instance=RequestContext(request))

		if error:
			lista_instituciones = instituciones.objects.all()
			form = fechaRipsForm(request.POST)
			ctx = {'form':form,'lista_instituciones':lista_instituciones,'error':error,'pendiente':pendiente}
			return render_to_response('home/crearRips.html',ctx,context_instance=RequestContext(request))
	#Es un GET*****************************************************
	else:
		lista_instituciones = instituciones.objects.all()
		form = fechaRipsForm()
		ctx = {'form':form,'lista_instituciones':lista_instituciones,'error':error,'pendiente':pendiente}
		return render_to_response('home/crearRips.html',ctx,context_instance=RequestContext(request))

def empresas_institucion_view(request):
	#Se listan todas las instituciones
	lista_instituciones = instituciones.objects.get(pk=request.GET['id'])
	#Se obtienen las empresas que atiende cada institucion explorando su relacion manytomany
	empresas = lista_instituciones.empresas.all()
	data = []
	for p in empresas:
		data.append({'id': p.id,'razon':p.razon,})
	from django.core.serializers.json import DjangoJSONEncoder
	return HttpResponse(simplejson.dumps(data, cls=DjangoJSONEncoder), content_type='application/json')
