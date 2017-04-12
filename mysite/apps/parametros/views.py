from django.shortcuts import render,render_to_response
from django.template import RequestContext
from mysite.apps.parametros.models import procedimientos,items,servicios,serviciosEmpresa
from mysite.apps.parametros.forms import addProcedimientoForm,addPlantillaForm
from mysite.apps.organizaciones.models import empresas
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from mysite.settings import URL_LOGIN
import json as simplejson

@login_required(login_url=URL_LOGIN)
def procedimientos_view(request):
	lista_procedimientos = procedimientos.objects.all().order_by('descripcion') # Select * from ventas_productos where status = True
	ctx = {'procedimientos':lista_procedimientos}	
	return render_to_response('home/procedimientos.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def edit_procedimientos_view(request,id_prod):
	getprocedimiento = procedimientos.objects.get(pk=id_prod)
	if request.method == "POST":
		form = addProcedimientoForm(request.POST,instance=getprocedimiento)
		if form.is_valid():
			add = form.save(commit=False)
			form.save_m2m()
			add.save() # Guardamos la informacion
		return HttpResponseRedirect('/procedimientos/')	
	
	form = addProcedimientoForm(instance=getprocedimiento)
	ctx = {'form':form}	
	return render_to_response('home/editProcedimientos.html',ctx,context_instance=RequestContext(request))	

@login_required(login_url=URL_LOGIN)
def add_procedimiento_view(request):
	if request.method == "POST":
		form = addProcedimientoForm(request.POST)
		if form.is_valid():
			add = form.save(commit=False)
			add.save() # Guardamos la informacion
			form.save_m2m()
		return HttpResponseRedirect('/procedimientos/')	
	
	form = addProcedimientoForm()
	ctx = {'form':form}	
	return render_to_response('home/addProcedimiento.html',ctx,context_instance=RequestContext(request))	

@login_required(login_url=URL_LOGIN)
def plantillas_view(request):
	lista_plantillas = items.objects.all().order_by('nombre') # Select * from ventas_productos where status = True
	ctx = {'plantillas':lista_plantillas}	
	return render_to_response('home/plantillas.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def edit_plantillas_view(request,id_prod):
	getplantilla = items.objects.get(pk=id_prod)
	if request.method == "POST":
		form = addPlantillaForm(request.POST,instance=getplantilla)
		if form.is_valid():
			add = form.save(commit=False)
			add.save() # Guardamos la informacion
		return HttpResponseRedirect('/plantillas/')	
	
	form = addPlantillaForm(instance=getplantilla)
	ctx = {'form':form}	
	return render_to_response('home/editPlantillas.html',ctx,context_instance=RequestContext(request))	

@login_required(login_url=URL_LOGIN)
def add_plantilla_view(request):
	if request.method == "POST":
		form = addPlantillaForm(request.POST)
		if form.is_valid():
			add = form.save(commit=False)
			add.save() # Guardamos la informacion
		return HttpResponseRedirect('/plantillas/')	
	
	form = addPlantillaForm()
	ctx = {'form':form}	
	return render_to_response('home/addPlantilla.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def servicios_view(request):
	lista_servicios = servicios.objects.all().order_by('nombre') # Select * from ventas_productos where status = True
	ctx = {'servicios':lista_servicios}	
	return render_to_response('home/servicios.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def actualizar_servicio_view(request):
	id_servicio = request.GET['id_servicio']
	servicio = servicios.objects.get(pk = id_servicio)
	lista_empresas = empresas.objects.all()
	acciones = []
	for p in lista_empresas:
		try:
			lista = serviciosEmpresa.objects.get(nombre=servicio, empresa = p)
		except:
			#Crea el servicio
			temp = empresas.objects.get(razon=p.razon)
			nuevo = serviciosEmpresa(nombre=servicio, empresa=temp, costo=servicio.costo)
			nuevo.save()

	mensaje = {"status":"False"}
	return HttpResponse(simplejson.dumps(mensaje),content_type='application/json')		