from django.shortcuts import render,render_to_response
from django.template import RequestContext
from mysite.apps.historias.models import orden,historia_clinica,ordenesProducto
from mysite.apps.citas.models import agenda_consulta,agenda_procedimiento,citas_consulta,citas_procedimiento
from mysite.apps.datos.models import medico,paciente
from django.contrib.auth.models import User
from mysite.apps.home.models import userProfile
from mysite.apps.citas.forms import fechaForm,addCitaConsultaForm,addAgendaConsultaForm,addCitaProcedimientoForm,addAgendaProcedimientoForm,buscaAgendaConsultaForm,buscaAgendaProcedimientoForm
from django.http import HttpResponse,HttpResponseRedirect
from datetime import date
import datetime
from django.core import serializers
import json as simplejson
from django.contrib.auth.decorators import login_required
from mysite.settings import URL_LOGIN

@login_required(login_url=URL_LOGIN)
def agenda_view(request):
	error = False
	try:
		usuario_doctor = medico.objects.get(usuario=request.user)
	except:
		usuario_doctor = None

	if request.method == "POST":
		t_fechai = request.POST['fechai']
		if (t_fechai == ""):
			error = True
			ordenes = None
		else:	
			fi_format = datetime.datetime.strptime(t_fechai, '%Y-%m-%d').date() 
			ordenes = orden.objects.filter(fecha__year=fi_format.year,fecha__month=fi_format.month,fecha__day=fi_format.day, medico=usuario_doctor,anulada=False)
			lista=[]
			for p in ordenes:
				cadena = ""
				genera_historia = False
				productos = ordenesProducto.objects.filter(orden=p)
				for z in productos:
					if z.servicio.nombre.historia == True:
						genera_historia = True				
					cadena = cadena + z.servicio.nombre.nombre + ' | '
				if genera_historia == True: # Con esto se depura la lista para solamente mostrar las ordenes que generan historia	
					lista.append({'orden': p,'servicios':cadena})

		form = fechaForm(initial={'fechai':request.POST['fechai']})
		ctx = {'lista':lista,'form':form, 'error':error}
		return render_to_response('home/agenda.html',ctx,context_instance=RequestContext(request))	
	else:
		today = datetime.date.today()
		#ordenes = orden.objects.filter(fecha__year=today.year,fecha__month=today.month,fecha__day=today.day, medico=usuario_doctor)
		ordenes = orden.objects.filter(fecha__year=today.year,fecha__month=today.month,fecha__day=today.day, medico=usuario_doctor, anulada=False)
		lista=[]
		for p in ordenes:
			cadena = ""
			genera_historia = False
			productos = ordenesProducto.objects.filter(orden=p)
			for z in productos:
				if z.servicio.nombre.historia == True:
					genera_historia = True				
				cadena = cadena + z.servicio.nombre.nombre + ' | '
			if genera_historia == True: # Con esto se depura la lista para solamente mostrar las ordenes que generan historia	
				lista.append({'orden': p,'servicios':cadena})
	
		form = fechaForm()
		ctx = {'lista':lista,'form':form, 'error':error}
		return render_to_response('home/agenda.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def agenda_doctor_view(request):
	error = False
	if request.method == "POST":
		t_medico = request.POST['medico']
		t_fechai = request.POST['fechai']
		lista=[]
		if (t_fechai == "" or t_medico =="-1"):
			error = True
			ordenes = None
		else:
			fi_format = datetime.datetime.strptime(t_fechai, '%Y-%m-%d').date()	
			doctor = medico.objects.get(pk=t_medico)
			ordenes = orden.objects.filter(fecha__year=fi_format.year,fecha__month=fi_format.month,fecha__day=fi_format.day, medico=doctor, anulada=False)
			lista=[]
			for p in ordenes:
				cadena = ""
				genera_historia = False
				productos = ordenesProducto.objects.filter(orden=p)
				for z in productos:
					if z.servicio.nombre.historia == True:
						genera_historia = True				
					cadena = cadena + z.servicio.nombre.nombre + ' | '
				if genera_historia == True: # Con esto se depura la lista para solamente mostrar las ordenes que generan historia	
					lista.append({'orden': p,'servicios':cadena})

		form = fechaForm(initial={'fechai':request.POST['fechai']})
		usuario = User.objects.get(pk=request.user.id)
		i_u = userProfile.objects.get(user=usuario)
		lista_medicos = medico.objects.filter(institucion = i_u.institucion)
		ctx = {'lista':lista,'lista_medicos':lista_medicos,'form':form,'error':error}
		return render_to_response('home/agendaDoctor.html',ctx,context_instance=RequestContext(request))	
	else:
		lista = None
		form = fechaForm()
		usuario = User.objects.get(pk=request.user.id)
		i_u = userProfile.objects.get(user=usuario)
		lista_medicos = medico.objects.filter(institucion = i_u.institucion)
		ctx = {'lista':lista,'lista_medicos':lista_medicos,'form':form,'error':error}
		return render_to_response('home/agendaDoctor.html',ctx,context_instance=RequestContext(request))

def busca_paciente_view(request):
	if request.method == "GET":
		valor_cedula = request.GET['cedula']
		p = paciente.objects.filter(cedula=valor_cedula)
		data = serializers.serialize('json',p,fields=('pnombre','snombre','papellido','sapellido','documento','telefono','celular','procede'))
		return HttpResponse(data, content_type='application/json')	

def obtiene_citas_consultas_view(request):
	if request.method == "GET":
		llave = request.GET['id']
		p = agenda_consulta.objects.get(pk=llave)
		p_citas = citas_consulta.objects.filter(agenda=p)
		data = serializers.serialize('json',p_citas,fields=('pnombre','snombre','papellido','sapellido','documento','cedula','telefono','celular','consulta','empresa','llego','confirmo','cumplida','anestesiologo','observacion','hora_llegada'))
		return HttpResponse(data, content_type='application/json')	

@login_required(login_url=URL_LOGIN)
def citas_consultas_view(request):
	error = False
	if request.method == "POST":
		if request.POST['medico'] == '-1': #Valida que se haya seleccionado un doctor
			error = True
			form = addCitaConsultaForm(request.POST)
			form2 = addAgendaConsultaForm(request.POST)
		else:
			if request.POST['crear'] == '': #No existe la cita, se va a crear
				form2 = addAgendaConsultaForm(request.POST)
				if form2.is_valid():
					form = addCitaConsultaForm(request.POST)
					if form.is_valid():
						doctor = medico.objects.get(pk=request.POST['medico'])
						agenda = form2.save(commit=False)
						agenda.title = "%s  %s"%(request.POST['pnombre'],request.POST['papellido'])
						agenda.medico = doctor
						agenda.editable = True  
						agenda.overlap = False
						agenda.save() # Guardamos la informacion
						cita = form.save(commit=False)
						cita.agenda = agenda
						cita.generadapor = request.user
						try: #Verifica si el paciente existe
							t_paciente = paciente.objects.get(cedula=request.POST['cedula'])
							t_paciente.telefono = request.POST['telefono']
							t_paciente.celular = request.POST['celular']
							t_paciente.save()
							cita.paciente = t_paciente
						except: #El paciente no existe
							cita.paciente = None
						cita.save()
						return HttpResponseRedirect('/citas/consultas/')
			else: #Existe la cita, se va a editar
				llave = request.POST['crear']
				p = agenda_consulta.objects.get(pk=llave)
				form2 = addAgendaConsultaForm(request.POST,instance=p)
				if form2.is_valid():
					p_citas = citas_consulta.objects.get(agenda=p)
					form = addCitaConsultaForm(request.POST,instance=p_citas)
					if form.is_valid():
						form2.save() # Guardamos la informacion
						form.save()
						p.title = "%s  %s"%(request.POST['pnombre'],request.POST['papellido'])
						p.save()
						try:
							t_paciente = paciente.objects.get(cedula=request.POST['cedula'])
							t_paciente.telefono = request.POST['telefono']
							t_paciente.celular = request.POST['celular']
							t_paciente.save()
						except:
							pass
						return HttpResponseRedirect('/citas/consultas/')							

		lista_medicos = medico.objects.all()
		ctx = {'lista_medicos':lista_medicos,'form':form,'form2':form2,'error':error}
		return render_to_response('home/citas_consulta.html',ctx,context_instance=RequestContext(request))	
	else:
		lista_medicos = medico.objects.all()
		form = addCitaConsultaForm()
		form2 = addAgendaConsultaForm()
		ctx = {'lista_medicos':lista_medicos,'form':form,'form2':form2,'error':error}
		return render_to_response('home/citas_consulta.html',ctx,context_instance=RequestContext(request))

def citas_listado_view(request):
	error = True
	consulta = True 
	if request.method == "POST":
		form = fechaForm(request.POST)
		form2 = buscaAgendaConsultaForm(request.POST)
		if form.is_valid():
			if form2.is_valid():
				t_fechai = request.POST['fechai']
				fi_format = datetime.datetime.strptime(t_fechai, '%Y-%m-%d').date() 
				t_medico = request.POST['medico']
				error = False
				doctor = medico.objects.get(pk=t_medico)
				tipo = request.POST['tipo']
				if tipo == "C": #Se escogio la opcion Consulta
					listado = citas_consulta.objects.filter(agenda__start__year=fi_format.year,agenda__start__month=fi_format.month,agenda__start__day=fi_format.day, agenda__medico=doctor).order_by('agenda__start')
				else:
					consulta = False
					#agenda__start__contains=t_fechai, 
					listado = citas_procedimiento.objects.filter(agenda__start__year=fi_format.year,agenda__start__month=fi_format.month,agenda__start__day=fi_format.day,agenda__medico=doctor).order_by('agenda__start')	

		ctx = {'form':form,'form2':form2,'listado':listado,'error':error,'consulta':consulta}
		return render_to_response('home/citas_listado.html',ctx,context_instance=RequestContext(request))
	else:
		error = False
		listado = None			
		form = fechaForm()
		form2 = buscaAgendaConsultaForm()
		ctx = {'form':form,'form2':form2,'listado':listado,'error':error,'consulta':consulta}
		return render_to_response('home/citas_listado.html',ctx,context_instance=RequestContext(request))

def obtiene_citas_procedimientos_view(request):
	if request.method == "GET":
		llave = request.GET['id']
		p = agenda_procedimiento.objects.get(pk=llave)
		p_citas = citas_procedimiento.objects.filter(agenda=p)
		data = serializers.serialize('json',p_citas,fields=('pnombre','snombre','papellido','sapellido','documento','cedula','telefono','celular','procedimiento','empresa','llego','confirmo','cumplida','anestesiologo','observacion','hora_llegada'))
		return HttpResponse(data, content_type='application/json')	

@login_required(login_url=URL_LOGIN)
def citas_procedimientos_view(request):
	error = False
	if request.method == "POST":
		if request.POST['medico'] == '-1': #Valida que se haya seleccionado un doctor
			error = True
			form = addCitaConsultaForm(request.POST)
			form2 = addAgendaConsultaForm(request.POST)
		else:	
			if request.POST['crear'] == '': #No existe la cita, se va a crear
				form2 = addAgendaProcedimientoForm(request.POST)
				if form2.is_valid():
					form = addCitaProcedimientoForm(request.POST)
					if form.is_valid():
						doctor = medico.objects.get(pk=request.POST['medico'])
						agenda = form2.save(commit=False)
						agenda.title = "%s  %s"%(request.POST['pnombre'],request.POST['papellido'])
						agenda.medico = doctor
						agenda.editable = True  
						agenda.overlap = False
						agenda.save() # Guardamos la informacion
						cita = form.save(commit=False)
						cita.agenda = agenda
						cita.generadapor = request.user
						try: #Verifica si el paciente existe
							t_paciente = paciente.objects.get(cedula=request.POST['cedula'])
							t_paciente.telefono = request.POST['telefono']
							t_paciente.celular = request.POST['celular']
							t_paciente.save()
							cita.paciente = t_paciente
						except: #El paciente no existe
							cita.paciente = None
						cita.save()
						return HttpResponseRedirect('/citas/procedimiento/')
			else: #Existe la cita, se va a editar
				llave = request.POST['crear']
				p = agenda_procedimiento.objects.get(pk=llave)
				form2 = addAgendaProcedimientoForm(request.POST,instance=p)
				if form2.is_valid():
					p_citas = citas_procedimiento.objects.get(agenda=p)
					form = addCitaProcedimientoForm(request.POST,instance=p_citas)
					if form.is_valid():
						form2.save() # Guardamos la informacion
						form.save()
						p.title = "%s  %s"%(request.POST['pnombre'],request.POST['papellido'])
						p.save()
						try: #Verifica si el paciente existe
							t_paciente = paciente.objects.get(cedula=request.POST['cedula'])
							t_paciente.telefono = request.POST['telefono']
							t_paciente.celular = request.POST['celular']
							t_paciente.save()
						except:
							pass
						return HttpResponseRedirect('/citas/procedimiento/')							

		lista_medicos = medico.objects.all()
		ctx = {'lista_medicos':lista_medicos,'form':form,'form2':form2,'error':error}
		return render_to_response('home/citas_procedimiento.html',ctx,context_instance=RequestContext(request))	
	else:
		lista_medicos = medico.objects.all()
		form = addCitaProcedimientoForm()
		form2 = addAgendaProcedimientoForm()
		ctx = {'lista_medicos':lista_medicos,'form':form,'form2':form2,'error':error}
		return render_to_response('home/citas_procedimiento.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def citas_reservaciones_view(request):
	error = False
	exito = False
	if request.method == "POST":
		doctor = request.POST['medico']
		t_mes = request.POST['mes']
		t_ano = request.POST['ano']
		if (doctor == '-1') | (t_mes == "-1") | (t_ano == "-1"):
			error = True
		else:	
			t_medico = medico.objects.get(pk=doctor)
			mes = int(t_mes)
			ano = int(t_ano)
			if (mes > 0) & (ano >0):
				inicio = datetime.datetime(ano, mes, 1, 00, 00)
				while (inicio.month < mes+1):
					fin = inicio + datetime.timedelta(days=1)
					p = agenda_consulta(title='Reservado',start=inicio,end=fin,medico=t_medico,editable=False,overlap=False,color='#d3d3d3')
					p.save()
					q = agenda_procedimiento(title='Reservado',start=inicio,end=fin,medico=t_medico,editable=False,overlap=False,color='#d3d3d3')
					q.save()
					inicio = inicio + datetime.timedelta(days=1)
			exito = True		
		lista_medicos = medico.objects.all()
		rango = range(2015,2100)
		ctx = {'lista_medicos':lista_medicos,'rango':rango,'error':error,'exito':exito}
		return render_to_response('home/citas_reservacion.html',ctx,context_instance=RequestContext(request))
	else:
		lista_medicos = medico.objects.all()
		rango = range(2015,2100)
		ctx = {'lista_medicos':lista_medicos,'rango':rango,'error':error,'exito':exito}
		return render_to_response('home/citas_reservacion.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def citas_disponibilidad_consultas_view(request):
	if request.method == "POST":
		if 'btnGuardar' in request.POST:
			if request.POST['crear'] == '': #No existe la cita, se va a crear
				form = addAgendaConsultaForm(request.POST)
				if form.is_valid():
					doctor = medico.objects.get(pk=request.POST['medico'])
					temp_agenda = form.save(commit=False)
					temp_agenda.title = 'Reservado'
					temp_agenda.medico = doctor
					temp_agenda.editable = False
					temp_agenda.overlap = False
					temp_agenda.color = '#d3d3d3'
					temp_agenda.save()
			else: #Existe la cita, se va a editar
				llave = request.POST['crear']
				p = agenda_consulta.objects.get(pk=llave)
				form = addAgendaConsultaForm(request.POST,instance=p)
				if form.is_valid():
					form.save()
		else:
			if request.POST['crear'] == '': #No existe la cita, se ignora el intento de borrado												
				form = addAgendaConsultaForm()
			else: #La cita existe, se procede al borrado
				llave = request.POST['crear']
				p = agenda_consulta.objects.get(pk=llave)
				form = addAgendaConsultaForm(request.POST,instance=p)
				if form.is_valid():
					p.delete()
					
		lista_medicos = medico.objects.all()
		ctx = {'lista_medicos':lista_medicos,'form':form}
		return render_to_response('home/citas_disponibilidad_consultas.html',ctx,context_instance=RequestContext(request))	
	else:
		lista_medicos = medico.objects.all()
		form = addAgendaConsultaForm()
		ctx = {'lista_medicos':lista_medicos,'form':form}
		return render_to_response('home/citas_disponibilidad_consultas.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def citas_disponibilidad_procedimientos_view(request):
	if request.method == "POST":
		if 'btnGuardar' in request.POST:
			if request.POST['crear'] == '': #No existe la cita, se va a crear
				form = addAgendaProcedimientoForm(request.POST)
				if form.is_valid():
					doctor = medico.objects.get(pk=request.POST['medico'])
					temp_agenda = form.save(commit=False)
					temp_agenda.title = 'Reservado'
					temp_agenda.medico = doctor
					temp_agenda.editable = False
					temp_agenda.overlap = False
					temp_agenda.color = '#d3d3d3'
					temp_agenda.save()
			else: #Existe la cita, se va a editar
				llave = request.POST['crear']
				p = agenda_procedimiento.objects.get(pk=llave)
				form = addAgendaProcedimientoForm(request.POST,instance=p)
				if form.is_valid():
					form.save()
		else:
			if request.POST['crear'] == '': #No existe la cita, se ignora el intento de borrado												
				form = addAgendaProcedimientoForm()
			else: #La cita existe, se procede al borrado
				llave = request.POST['crear']
				p = agenda_consulta.objects.get(pk=llave)
				form = addAgendaProcedimientoForm(request.POST,instance=p)
				if form.is_valid():
					p.delete()
				
		lista_medicos = medico.objects.all()
		ctx = {'lista_medicos':lista_medicos,'form':form}
		return render_to_response('home/citas_disponibilidad_procedimientos.html',ctx,context_instance=RequestContext(request))	
	else:
		lista_medicos = medico.objects.all()
		form = addAgendaProcedimientoForm()
		ctx = {'lista_medicos':lista_medicos,'form':form}
		return render_to_response('home/citas_disponibilidad_procedimientos.html',ctx,context_instance=RequestContext(request))

def calendario_view(request):
	if request.method == "POST":
		try:
			doctor = medico.objects.get(pk=request.POST['medico'])
			llave = request.POST['id']
			inicio = request.POST['start']
			fin    = request.POST['end']
			p = agenda_consulta.objects.get(pk=llave)
			p.start = inicio
			p.end = fin
			p.save() # Guardamos la informacion
			mensaje = {"status":"True"}
			return HttpResponse(simplejson.dumps(mensaje),content_type='application/json')
		except:
			mensaje = {"status":"False"}
			return HttpResponse(simplejson.dumps(mensaje),content_type='application/json')
	else:	
		#Se debe hacer una consulta por usuario doctor
		try:
			doctor = medico.objects.get(pk=request.GET.get('doctor'))
		except:
			doctor = 0	
		start_timestamp = request.GET.get('start')
		end_timestamp = request.GET.get('end')
		agenda = agenda_consulta.objects.filter(start__lte=end_timestamp, end__gte=start_timestamp, medico=doctor)
		from django.core.serializers.json import DjangoJSONEncoder
		events = []
		for event in agenda:
			events.append({'id': event.id,'title': event.title,'start': event.start,'end': event.end,'editable': event.editable,'overlap': event.overlap,'color': event.color,})
		return HttpResponse(simplejson.dumps(events, cls=DjangoJSONEncoder), content_type='application/json')	

def calendario_procedimientos_view(request):
	if request.method == "POST":
		try:
			doctor = medico.objects.get(pk=request.POST['medico'])
			llave = request.POST['id']
			inicio = request.POST['start']
			fin    = request.POST['end']
			p = agenda_procedimiento.objects.get(pk=llave)
			p.start = inicio
			p.end = fin
			p.save() # Guardamos la informacion
			mensaje = {"status":"True"}
			return HttpResponse(simplejson.dumps(mensaje),content_type='application/json')
		except:
			mensaje = {"status":"False"}
			return HttpResponse(simplejson.dumps(mensaje),content_type='application/json')
	else:	
		#Se debe hacer una consulta por usuario doctor
		try:
			doctor = medico.objects.get(pk=request.GET.get('doctor'))
		except:
			doctor = 0	
		start_timestamp = request.GET.get('start')
		end_timestamp = request.GET.get('end')
		agenda = agenda_procedimiento.objects.filter(start__lte=end_timestamp, end__gte=start_timestamp, medico=doctor)
		from django.core.serializers.json import DjangoJSONEncoder
		events = []
		for event in agenda:
			events.append({'id': event.id,'title': event.title,'start': event.start,'end': event.end,'editable': event.editable,'overlap': event.overlap,'color': event.color,})
		return HttpResponse(simplejson.dumps(events, cls=DjangoJSONEncoder), content_type='application/json')	

def calendario_disponibilidad_consultas_view(request):
	if request.method == "GET":
		try:
			doctor = medico.objects.get(pk=request.GET.get('doctor'))
		except:
			doctor = 0	
		start_timestamp = request.GET.get('start')
		end_timestamp = request.GET.get('end')
		agenda = agenda_consulta.objects.filter(start__lte=end_timestamp, end__gte=start_timestamp, medico=doctor)
		from django.core.serializers.json import DjangoJSONEncoder
		events = []
		for event in agenda:
			events.append({'id': event.id,'title': event.title,'start': event.start,'end': event.end,'editable': event.editable,'overlap': event.overlap,'color': event.color,})
		return HttpResponse(simplejson.dumps(events, cls=DjangoJSONEncoder), content_type='application/json')	

def calendario_disponibilidad_procedimientos_view(request):
	if request.method == "GET":
		try:
			doctor = medico.objects.get(pk=request.GET.get('doctor'))
		except:
			doctor = 0	
		start_timestamp = request.GET.get('start')
		end_timestamp = request.GET.get('end')
		agenda = agenda_procedimiento.objects.filter(start__lte=end_timestamp, end__gte=start_timestamp, medico=doctor)
		from django.core.serializers.json import DjangoJSONEncoder
		events = []
		for event in agenda:
			events.append({'id': event.id,'title': event.title,'start': event.start,'end': event.end,'editable': event.editable,'overlap': event.overlap,'color': event.color,})
		return HttpResponse(simplejson.dumps(events, cls=DjangoJSONEncoder), content_type='application/json')	

def redirecciona_view(request,id_prod):
	getorden = orden.objects.get(pk=id_prod) #Obtiene objeto Orden
	#Verifica si es primera vez que viene el paciente
	gethistoria = historia_clinica.objects.filter(paciente=getorden.paciente)
	if not gethistoria:
		#Si no tiene historia es porque viene por primera vez
		return HttpResponseRedirect('/add/historias/orden/%s/'%id_prod)
	else:
		#Si tiene historia entonces es una evolucion
		return HttpResponseRedirect('/add/historias/orden/%s/'%id_prod)	
		#return HttpResponseRedirect('/add/evolucion/orden/%s/'%id_prod)

			
