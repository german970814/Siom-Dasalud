
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from mysite.apps.historias.models import historia_clinica,historia_procedimientos
from mysite.apps.datos.models import medico,paciente
from mysite.apps.home.models import userProfile
from mysite.apps.organizaciones.models import empresas,instituciones
from mysite.apps.datos.forms import addmedicoForm,addPacienteForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from mysite.settings import URL_LOGIN


@login_required(login_url=URL_LOGIN)
def medicos_view(request):
	if request.method == "POST":
		try:
			prod = medico.objects.get(cedula=request.POST['cedula'])
			form = addmedicoForm(request.POST,instance=prod)
			if form.is_valid():
				form.save()
		except:
			form = addmedicoForm(request.POST)
			if form.is_valid():
				form.save()
	else:
		form = addmedicoForm()		

	medicos = medico.objects.all() # Select * from ventas_productos where status = True
	ctx = {'medicos':medicos,'form':form}
	return render_to_response('citas/medicos.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def pacientes_view(request,pagina):
	if request.method == "POST":
		st = request.POST['numero']
		usuario = User.objects.get(pk=request.user.id)
		i_u = userProfile.objects.get(user=usuario)
		if request.user.has_perm("home.es_administrador"):
			pacientes= paciente.objects.filter(Q(pnombre__icontains=st) | Q(snombre__icontains=st) | Q(cedula=st) | Q(papellido__icontains=st) | Q(sapellido__icontains=st)).order_by("pnombre")
		else:	
			pacientes= paciente.objects.filter(Q(pnombre__icontains=st) | Q(snombre__icontains=st) | Q(cedula=st) | Q(papellido__icontains=st) | Q(sapellido__icontains=st),institucion=i_u.institucion).order_by("pnombre") # Select * from ventas_productos where status = True
		pacientes = pacientes.select_related('procede')
		ctx = {'pacientes':pacientes}
		return render_to_response('home/pacientes.html',ctx,context_instance=RequestContext(request))
	else:	
		pacientes = None
		ctx = {'pacientes':pacientes}
		return render_to_response('home/pacientes.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def add_paciente_view(request):
	info = ""
	if request.method == "POST":
		form = addPacienteForm(request.POST,request.FILES)
		if form.is_valid():
			usuario = User.objects.get(pk=request.user.id)
			i_u = userProfile.objects.get(user=usuario)
			add = form.save(commit=False)
			u = User.objects.create_user(username=add.cedula,email=add.email,password='123456')
			u.save() # Guardar el objeto
			add.status = True
			add.usuario = u
			add.institucion = i_u.institucion
			add.save() # Guardamos la informacion
			info = "Guardado satisfactoriamente"
			return HttpResponseRedirect('/pacientes/page/1/')
	else:
		form = addPacienteForm()
		
	usuario = User.objects.get(pk=request.user.id)
	i_u = userProfile.objects.get(user=usuario)
	form.fields["procede"].queryset = i_u.institucion.empresas	
	ctx = {'form':form,'informacion':info}
	return render_to_response('home/addPaciente.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def edit_paciente_view(request,id_prod):
	getpaciente = paciente.objects.get(pk=id_prod)
	if request.method == "POST":
		form = addPacienteForm(request.POST,request.FILES,instance=getpaciente)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/pacientes/page/1/')
	else:
		form = addPacienteForm(instance=getpaciente)
	ctx = {'form':form}
	return render_to_response('home/addPaciente.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def historial_paciente_view(request,id_prod):
	getpaciente = paciente.objects.get(pk=id_prod)
	lista_historias = historia_clinica.objects.filter(paciente = getpaciente)
	lista_procedimientos = historia_procedimientos.objects.filter(paciente = getpaciente)
	ctx = {'getpaciente':getpaciente,'lista_historias':lista_historias,'lista_procedimientos':lista_procedimientos}
	return render_to_response('home/historial_paciente.html',ctx,context_instance=RequestContext(request))			

