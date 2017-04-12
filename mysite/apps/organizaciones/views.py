from django.shortcuts import render,render_to_response
from django.template import RequestContext
from mysite.apps.organizaciones.models import empresas,instituciones,planes_salud
from mysite.apps.organizaciones.forms import addEmpresaForm,addInstitucionForm,addPlanForm
from mysite.apps.parametros.models import servicios,serviciosEmpresa
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from mysite.settings import URL_LOGIN

@login_required(login_url=URL_LOGIN)
def empresas_view(request):
	lista_empresas = empresas.objects.all().order_by('razon') # Select * from ventas_productos where status = True
	ctx = {'empresas':lista_empresas}	
	return render_to_response('citas/empresas.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def add_empresas_view(request):
	if request.method == "POST":
		form = addEmpresaForm(request.POST)
		if form.is_valid():
			add = form.save(commit=False)
			add.save() # Guardamos la informacion
			empresa = empresas.objects.get(pk = add.id)
			lista = servicios.objects.all()
			for p in lista:
				nuevo = serviciosEmpresa(nombre=p,empresa=empresa,costo=p.costo)
				nuevo.save()
			return HttpResponseRedirect('/empresas/')
			
		ctx = {'form':form}	
		return render_to_response('citas/addEmpresa.html',ctx,context_instance=RequestContext(request))				
	else:
		form = addEmpresaForm()
	ctx = {'form':form}	
	return render_to_response('citas/addEmpresa.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def edit_empresas_view(request,id_prod):
	getempresa = empresas.objects.get(pk=id_prod)
	if request.method == "POST":
		form = addEmpresaForm(request.POST,instance=getempresa)
		if form.is_valid():
			add = form.save(commit=False)
			form.save_m2m()
			add.save() # Guardamos la informacion
		return HttpResponseRedirect('/empresas/')	
	
	form = addEmpresaForm(instance=getempresa)
	ctx = {'form':form}	
	return render_to_response('citas/editEmpresa.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def instituciones_view(request):
	lista_instituciones = instituciones.objects.all().order_by('razon') # Select * from ventas_productos where status = True
	ctx = {'instituciones':lista_instituciones}	
	return render_to_response('citas/instituciones.html',ctx,context_instance=RequestContext(request))	

@login_required(login_url=URL_LOGIN)
def add_instituciones_view(request):
	if request.method == "POST":
		form = addInstitucionForm(request.POST)
		if form.is_valid():
			add = form.save(commit=False)
			add.save() # Guardamos la informacion
			form.save_m2m()
			return HttpResponseRedirect('/instituciones/')	
	else:
		form = addInstitucionForm()

	ctx = {'form':form}	
	return render_to_response('citas/addInstitucion.html',ctx,context_instance=RequestContext(request))						

@login_required(login_url=URL_LOGIN)
def edit_instituciones_view(request,id_prod):
	getinstitucion = instituciones.objects.get(pk=id_prod)
	if request.method == "POST":
		form = addInstitucionForm(request.POST,instance=getinstitucion)
		if form.is_valid():
			add = form.save(commit=False)
			form.save_m2m()
			add.save() # Guardamos la informacion
			return HttpResponseRedirect('/instituciones/')	
	else:
		form = addInstitucionForm(instance=getinstitucion)
	ctx = {'form':form}	
	return render_to_response('citas/editInstitucion.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def planes_view(request):
	lista_planes = planes_salud.objects.all().order_by('descripcion') # Select * from ventas_productos where status = True
	ctx = {'planes':lista_planes}	
	return render_to_response('home/planes.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def add_planes_view(request):
	if request.method == "POST":
		form = addPlanForm(request.POST)
		if form.is_valid():
			add = form.save(commit=False)
			add.save() # Guardamos la informacion
			form.save_m2m()
			return HttpResponseRedirect('/planes/')	
	else:
		form = addPlanForm()
	ctx = {'form':form}	
	return render_to_response('home/addPlan.html',ctx,context_instance=RequestContext(request))	

@login_required(login_url=URL_LOGIN)
def edit_planes_view(request,id_prod):
	getplanes = planes_salud.objects.get(pk=id_prod)
	if request.method == "POST":
		form = addPlanForm(request.POST,instance=getplanes)
		if form.is_valid():
			add = form.save(commit=False)
			form.save_m2m()
			add.save() # Guardamos la informacion
			return HttpResponseRedirect('/planes/')	
	else:		
		form = addPlanForm(instance=getplanes)
	ctx = {'form':form}	
	return render_to_response('home/editPlan.html',ctx,context_instance=RequestContext(request))