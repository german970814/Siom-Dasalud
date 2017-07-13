from django.shortcuts import render_to_response
from django.template import RequestContext
from mysite.apps.datos.models import medico
from mysite.apps.historias.models import orden,ordenesProducto,historia_clinica,historia_procedimientos
from mysite.apps.organizaciones.models import usuario_empresa
from mysite.apps.home.forms import ContactForm, LoginForm,RegisterForm,FormularioCambiarContrasena,FormularioCambiarClave,usuarioForm,usuarioEmpresaForm,AddusuarioEmpresaForm,userProfileForm
from mysite.apps.home.models import userProfile
from mysite.apps.historias.forms import fechaRipsForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import Group,User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from mysite.settings import URL_LOGIN
import datetime
from datetime import date, timedelta

@login_required(login_url=URL_LOGIN)
def index_view(request):
    today = datetime.date.today()
    mes = today.month
    if request.user.has_perm("home.es_administrador"):
        pendientes = orden.objects.filter(fecha__year=today.year,fecha__month=today.month,status='P').count()
        realizadas = orden.objects.filter(fecha__year=today.year,fecha__month=today.month,status='R').count()
        hoy = orden.objects.filter(fecha__year=today.year,fecha__month=today.month,fecha__day=today.day).count()
        pendientes_hoy = orden.objects.filter(fecha__year=today.year,fecha__month=today.month,fecha__day=today.day,status='P').count()
    else:
        try:
            doctor = medico.objects.get(usuario=request.user)
        except:
            doctor = None   
        pendientes = orden.objects.filter(fecha__year=today.year,fecha__month=today.month,status='P',medico=doctor).count()
        realizadas = orden.objects.filter(fecha__year=today.year,fecha__month=today.month,status='R',medico=doctor).count()
        hoy = orden.objects.filter(fecha__year=today.year,fecha__month=today.month,fecha__day=today.day,medico=doctor).count()
        pendientes_hoy = orden.objects.filter(fecha__year=today.year,fecha__month=today.month,fecha__day=today.day,status='P',medico=doctor).count()        

    medicos = medico.objects.filter(estado='A')
    if mes == 1:
        s_mes = 'Enero'
    elif mes == 2:
        s_mes = 'Febrero'
    elif mes == 3:
        s_mes = 'Marzo'
    elif mes == 4:
        s_mes = 'Abril'
    elif mes == 5:
        s_mes = 'Mayo'
    elif mes == 6:
        s_mes = 'Junio'
    elif mes == 7:
        s_mes = 'Julio'
    elif mes == 8:
        s_mes = 'Agosto'                        
    elif mes == 9:
        s_mes = 'Septiembre'
    elif mes == 10:
        s_mes = 'Octubre'
    elif mes == 11:
        s_mes = 'Noviembre'
    else:
        s_mes = 'Diciembre'                
        
    ctx = {'medicos':medicos,'pendientes':pendientes,'realizadas':realizadas,'hoy':hoy,'pendientes_hoy':pendientes_hoy,'mes':s_mes,'today':today}
    return render_to_response('home/index.html',ctx,context_instance=RequestContext(request))

def login_view(request):
	mensaje = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method == "POST":
			form = LoginForm(request.POST)
			if form.is_valid():	
				next = request.POST['next']
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				usuario = authenticate(username=username,password=password)
				if usuario is not None and usuario.is_active:
					login(request,usuario)
					if request.user.has_perm("home.es_coordinador_general"):
						return HttpResponseRedirect("/portal_empresas")
					else:
						return HttpResponseRedirect(next)
				else:
					mensaje = "usuario y/o password incorrecto"
		next = request.REQUEST.get('next')
		form = LoginForm()
		ctx = {'form':form,'mensaje':mensaje,'next':next}
		return render_to_response('home/login.html',ctx,context_instance=RequestContext(request))

def register_view(request):
	form = RegisterForm()
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			usuario = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password_one = form.cleaned_data['password_one']
			password_two = form.cleaned_data['password_two']
			u = User.objects.create_user(username=usuario,email=email,password=password_one)
			u.save() # Guardar el objeto
			return render_to_response('home/thanks_register.html',context_instance=RequestContext(request))
		else:
			ctx = {'form':form}
			return 	render_to_response('home/register.html',ctx,context_instance=RequestContext(request))
	ctx = {'form':form}
	return render_to_response('home/register.html',ctx,context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/login')

import csv

def rips_consulta_view(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="AC000001.txt"'
    #response['Content-Disposition'] = 'inline; filename="somefilename.txt"'
    historial = historia_clinica.objects.all()
    writer = csv.writer(response)
    for p in historial:
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
    #writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    #writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])
    return response

def rips_procedimiento_view(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="AP000001.txt"'
    #response['Content-Disposition'] = 'inline; filename="somefilename.txt"'
    historial = historia_procedimientos.objects.all()
    writer = csv.writer(response)
    for p in historial:
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
    		p.orden.fecha_atencion.strftime("%d/%m/%Y"),p.orden.id,p.orden.procedimiento.codigo,p.ambito,p.finalidad,
    		p.personal,diagnostico,diagnostico1,complicacion, p.forma,p.orden.valor])

    return response

@login_required(login_url=URL_LOGIN)
def portal_empresas_view(request):     
	error = False
	if request.method == "POST":
		fi = request.POST['fechai']
		ff = request.POST['fechaf']
		t_orden = request.POST['numero']
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
			usuario = usuario_empresa.objects.get(usuario__pk = request.user.id)			
			ordenes = orden.objects.filter(fecha__range=(fi_format,ff_format),empresa=usuario.empresa).order_by('fecha')
			lista=[]
			for p in ordenes:
				cadena = ""
				productos = ordenesProducto.objects.filter(orden=p)
				for z in productos:				
					cadena = cadena + z.servicio.nombre.nombre + ' | '
				lista.append({'orden': p,'servicios':cadena})
			form = fechaRipsForm()	
			ctx = {'lista':lista,'form':form,'error':error}
			return render_to_response('home/portal_empresas.html',ctx,context_instance=RequestContext(request))
		else: #Se coloco un numero de orden, se ignoran las fechas y se hace la consulta
			ordenes = orden.objects.filter(pk = t_orden).order_by('fecha')
			lista=[]
			for p in ordenes:
				cadena = ""
				productos = ordenesProducto.objects.filter(orden=p)
				for z in productos:				
					cadena = cadena + z.servicio.nombre.nombre + ' | '
				lista.append({'orden': p,'servicios':cadena})			
			form = fechaRipsForm()	
			ctx = {'lista':lista,'form':form,'error':error}
			return render_to_response('home/portal_empresas.html',ctx,context_instance=RequestContext(request))	
			
	lista = []
	form = fechaRipsForm()	
	ctx = {'lista':lista,'form':form,'error':error}
	return render_to_response('home/portal_empresas.html',ctx,context_instance=RequestContext(request))


@login_required(login_url=URL_LOGIN)
def buscar_orden_view(request):     
    error = False
    if request.method == "POST":
        t_orden = request.POST['numero']
        ordenes = orden.objects.filter(paciente__cedula = t_orden).order_by('fecha')
        lista=[]
        for p in ordenes:
            cadena = ""
            productos = ordenesProducto.objects.filter(orden=p)
            for z in productos:             
                cadena = cadena + z.servicio.nombre.nombre + ' | '
            lista.append({'orden': p,'servicios':cadena})           

        ctx = {'lista':lista,'error':error}
        return render_to_response('home/buscar_orden.html',ctx,context_instance=RequestContext(request)) 
            
    lista = [] 
    ctx = {'lista':lista,'error':error}
    return render_to_response('home/buscar_orden.html',ctx,context_instance=RequestContext(request))


@login_required(login_url=URL_LOGIN)
def cambiarPassword_view(request):
    miembroUsuario = request.user
    if request.method == 'POST':
        form = FormularioCambiarContrasena(data=request.POST)
        if form.is_valid():
            if(miembroUsuario.check_password(form.cleaned_data['contrasenaAnterior']) and \
               form.cleaned_data['contrasenaNueva'] == form.cleaned_data['contrasenaNuevaVerificacion']):
                miembroUsuario.set_password(form.cleaned_data['contrasenaNueva'])
                miembroUsuario.save()
                return HttpResponseRedirect("/")
            else:
                validacionContrasena = u'Error al tratar de cambiar la Clave, verifique que la Clave anterior sea correcta, y que concuerde la Clave nueva y la verificacion.'
                #return render_to_response("Miembros/cambiar_contrasena.html", locals(), context_instance=RequestContext(request))      
    else:
        form = FormularioCambiarContrasena() 

    return render_to_response("home/cambiar_contrasena.html", locals(), context_instance=RequestContext(request))


@login_required(login_url=URL_LOGIN)
def usuarios_view(request):     
    usuarios = userProfile.objects.all().exclude(user__pk__iexact = '1')
    ctx = {'usuarios':usuarios}
    return render_to_response('home/usuarios.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def add_usuario_view(request):
    add = True
    if request.method == "POST":
        form = usuarioForm(request.POST)
        form2 = userProfileForm(request.POST)
        if form.is_valid():
            nuevo = form.save()
            # nuevo.set_password('123456')
            # nuevo.save()
            perfil = form2.save(commit=False)
            perfil.user = nuevo
            perfil.save()
            return HttpResponseRedirect('/usuarios/')            
    else:
        form = usuarioForm()
        form2 = userProfileForm()
    ctx = {'form':form,'form2':form2,'add':add}
    return render_to_response('home/editUsuario.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def edit_usuario_view(request,id_prod):
    getusuario = User.objects.get(pk=id_prod)
    getprofile = userProfile.objects.get(user=getusuario)
    if request.method == "POST":
        form = usuarioForm(request.POST,instance=getusuario)
        form2 = userProfileForm(request.POST,instance=getprofile)
        if form.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect('/usuarios/')
    else:
        form = usuarioForm(instance=getusuario)
        form2 = userProfileForm(instance=getprofile)
    ctx = {'form':form,'form2':form2}
    return render_to_response('home/editUsuario.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def cambiarClave_view(request,id_prod):
    miembroUsuario = User.objects.get(pk=id_prod)
    if request.method == 'POST':
        form = FormularioCambiarClave(data=request.POST)
        if form.is_valid():
            if(form.cleaned_data['contrasenaNueva'] == form.cleaned_data['contrasenaNuevaVerificacion']):
                miembroUsuario.set_password(form.cleaned_data['contrasenaNueva'])
                miembroUsuario.save()
                return HttpResponseRedirect("/usuarios/")
            else:
                validacionContrasena = u'Error al tratar de cambiar la Clave, verifique que la Clave anterior sea correcta, y que concuerde la Clave nueva y la verificacion.'
                #return render_to_response("Miembros/cambiar_contrasena.html", locals(), context_instance=RequestContext(request))      
    else:
        form = FormularioCambiarClave() 

    return render_to_response("home/cambiar_contrasena.html", locals(), context_instance=RequestContext(request))        

@login_required(login_url=URL_LOGIN)
def usuariosEmpresa_view(request):     
    usuarios = usuario_empresa.objects.all()
    ctx = {'usuarios':usuarios}
    return render_to_response('home/usuariosEmpresa.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def edit_usuarioEmpresa_view(request,id_prod):
    getusuario = usuario_empresa.objects.get(pk=id_prod)
    if request.method == "POST":
        form = usuarioEmpresaForm(request.POST,instance=getusuario)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/usuariosEmpresa/')
    else:
        form = usuarioEmpresaForm(instance=getusuario)

    ctx = {'form':form}
    return render_to_response('home/editUsuarioEmpresa.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def add_usuarioEmpresa_view(request):
    if request.method == "POST":
        form = AddusuarioEmpresaForm(request.POST)
        if form.is_valid():
            nuevo = form.save(commit=False)
            u = User.objects.create_user(username=nuevo.empresa.nit,password=nuevo.empresa.nit)
            u.save() # Guardar el objeto
            u.groups.add(Group.objects.get(name__iexact='Empresa'))
            nuevo.usuario = u
            nuevo.save()
            return HttpResponseRedirect('/usuariosEmpresa/')            
    else:
        form = AddusuarioEmpresaForm()

    ctx = {'form':form}
    return render_to_response('home/addUsuarioEmpresa.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def cambiarClaveEmpresa_view(request,id_prod):
    miembroUsuario = User.objects.get(pk=id_prod)
    if request.method == 'POST':
        form = FormularioCambiarClave(data=request.POST)
        if form.is_valid():
            if(form.cleaned_data['contrasenaNueva'] == form.cleaned_data['contrasenaNuevaVerificacion']):
                miembroUsuario.set_password(form.cleaned_data['contrasenaNueva'])
                miembroUsuario.save()
                return HttpResponseRedirect("/usuariosEmpresa/")
            else:
                validacionContrasena = u'Error al tratar de cambiar la Clave, verifique que la Clave anterior sea correcta, y que concuerde la Clave nueva y la verificacion.'
                #return render_to_response("Miembros/cambiar_contrasena.html", locals(), context_instance=RequestContext(request))      
    else:
        form = FormularioCambiarClave() 

    return render_to_response("home/cambiar_contrasena.html", locals(), context_instance=RequestContext(request))        
