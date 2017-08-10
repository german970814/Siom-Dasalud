# -*- coding: utf-8 -*- 
from django import forms
from django.contrib.auth.models import User
from mysite.apps.home.models import userProfile
from mysite.apps.organizaciones.models import usuario_empresa

class ContactForm(forms.Form):
    Email	= forms.EmailField(widget=forms.TextInput())
    Titulo	= forms.CharField(widget=forms.TextInput())
    Texto	= forms.CharField(widget=forms.Textarea())

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))

class RegisterForm(forms.Form):
    nombre = forms.CharField(label="Nombres",widget=forms.TextInput())
    papellido = forms.CharField(label="Primer apellido",widget=forms.TextInput())
    sapellido = forms.CharField(label="Segundo apellido",widget=forms.TextInput())
    cedula = forms.CharField(label="Cedula",widget=forms.TextInput())
    username = forms.CharField(label="Nombre de Usuario",widget=forms.TextInput())
    email    = forms.EmailField(label="Correo Electronico",widget=forms.TextInput())
    password_one = forms.CharField(label="Password",widget=forms.PasswordInput(render_value=False))
    password_two = forms.CharField(label="Confirmar password",widget=forms.PasswordInput(render_value=False))

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            u = User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Nombre de usuario ya existe')

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            u = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('Email ya registrado')

    def clean_password_two(self):
        password_one = self.cleaned_data['password_one']
        password_two = self.cleaned_data['password_two']
        if password_one == password_two:
            pass
        else:
            raise forms.ValidationError('Password no coinciden')

class FormularioCambiarContrasena(forms.Form):
    contrasenaAnterior = forms.CharField(widget=forms.PasswordInput(render_value=False),max_length=20, label=u'Clave anterior:')      
    contrasenaNueva = forms.CharField(widget=forms.PasswordInput(render_value=False),max_length=20, label=u'Clave nueva:')
    contrasenaNuevaVerificacion = forms.CharField(widget=forms.PasswordInput(render_value=False), max_length=20, label=u'Verifique clave nueva:')
    def __init__(self, *args, **kwargs):
        super(FormularioCambiarContrasena, self).__init__(*args, **kwargs)
        self.fields['contrasenaAnterior'].widget.attrs.update({'class' : 'form-control'})
        self.fields['contrasenaNueva'].widget.attrs.update({'class' : 'form-control'})	
        self.fields['contrasenaNuevaVerificacion'].widget.attrs.update({'class' : 'form-control'})

class FormularioCambiarClave(forms.Form): 
    contrasenaNueva = forms.CharField(widget=forms.PasswordInput(render_value=False),max_length=20, label=u'Clave nueva:')
    contrasenaNuevaVerificacion = forms.CharField(widget=forms.PasswordInput(render_value=False), max_length=20, label=u'Verifique clave nueva:')
    def __init__(self, *args, **kwargs):
        super(FormularioCambiarClave, self).__init__(*args, **kwargs)
        self.fields['contrasenaNueva'].widget.attrs.update({'class' : 'form-control'})	
        self.fields['contrasenaNuevaVerificacion'].widget.attrs.update({'class' : 'form-control'})
 
class usuarioForm(forms.ModelForm):
    class Meta:
        model   = User
        fields = ['username', 'first_name', 'last_name','is_active', 'groups']	
    def __init__(self, *args, **kwargs):
        super(usuarioForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class' : 'form-control'})
        self.fields['first_name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['is_active'].widget.attrs.update({'class' : 'form-control'})
        self.fields['groups'].widget.attrs.update({'class' : 'form-control'})							

    def save(self, *args, **kwargs):
        data = self.cleaned_data
        if not self.instance.pk:
            data.setdefault('password', '123456')
            active = data.pop('is_active', None)
            groups = data.pop('groups', [])
            user = User.objects.create_user(**data)
            for group in groups:
                user.groups.add(group)
        else:
            user = super(usuarioForm, self).save(*args, **kwargs)
        return user

class usuarioEmpresaForm(forms.ModelForm):
    class Meta:
        model   = usuario_empresa
        fields = ['empresa', 'nombre', 'usuario']
    def __init__(self, *args, **kwargs):
        super(usuarioEmpresaForm, self).__init__(*args, **kwargs)
        self.fields['empresa'].widget.attrs.update({'class' : 'form-control'})
        self.fields['nombre'].widget.attrs.update({'class' : 'form-control'})
        self.fields['usuario'].widget.attrs.update({'class' : 'form-control'})

class AddusuarioEmpresaForm(forms.ModelForm):
    class Meta:
        model   = usuario_empresa
        fields = ['empresa', 'nombre']
    def __init__(self, *args, **kwargs):
        super(AddusuarioEmpresaForm, self).__init__(*args, **kwargs)
        self.fields['empresa'].widget.attrs.update({'class' : 'form-control'})
        self.fields['nombre'].widget.attrs.update({'class' : 'form-control'})

class userProfileForm(forms.ModelForm):
    class Meta:
        model   = userProfile
        fields = ['institucion',]
    def __init__(self, *args, **kwargs):
        super(userProfileForm, self).__init__(*args, **kwargs)
        self.fields['institucion'].widget.attrs.update({'class' : 'form-control'})
                        