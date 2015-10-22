from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from forms import FormInciarSesion
# Create your views here.
def iniciarSesion(request):


    template = "login.html"
    print request.user.is_authenticated()
    if not request.user.is_authenticated():
        if request.method == "POST":
            iniciar_sesion = FormInciarSesion(request.POST)
            if iniciar_sesion.is_valid():
                user = iniciar_sesion.cleaned_data['username'] #iniciar_sesion.cleaned_data['iniciar_input_email']
                clave = iniciar_sesion.cleaned_data['password']#iniciar_sesion.cleaned_data['iniciar_input_password']
                acceso = authenticate(username=user,password=clave)
                if acceso is not None:
                    if acceso.is_active:
                        login(request,acceso)
                        print "acceso"
                        return HttpResponseRedirect('/ventas/')
                    else:
                        iniciar_sesion = FormInciarSesion(request.POST)
                        return render_to_response(template,{'form_iniciar_sesion':iniciar_sesion,'error':'Su cuenta ha sido desactivada,por violar los derechos de uso'},context_instance = RequestContext(request))
                else:
                    iniciar_sesion = FormInciarSesion(request.POST)
                    return render_to_response(template,{'form_iniciar_sesion':iniciar_sesion,'error':'Por favor Ingrese Correctamente su usuario o password'},context_instance=RequestContext(request))
            else:
                iniciar_sesion = FormInciarSesion(request.POST)
                return render_to_response(template,{'form_iniciar_sesion':iniciar_sesion},context_instance=RequestContext(request))
        else:
            iniciar_sesion = FormInciarSesion(request.POST)
            return render_to_response(template,{'form_iniciar_sesion':iniciar_sesion},context_instance=RequestContext(request))
    else:
    	return HttpResponseRedirect("/ventas/")
    	

	
@login_required(login_url='/cuenta/login')
def cerrarSesion(request):
    logout(request)
    return  HttpResponseRedirect('/')