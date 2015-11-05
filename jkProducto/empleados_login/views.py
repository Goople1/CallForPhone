<<<<<<< HEAD
from django.shortcuts import render_to_response
=======
from django.shortcuts import render_to_response,redirect,HttpResponse
>>>>>>> 88944daaf8c3e3ed73961759b5031a0d4bd5c39e
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from forms import FormInciarSesion
from models import AsistenciaTrabajador
from sucursales.models import SucursalTrabajador
#from django.utils import timezone
from django.db.models import Q
import datetime
# Create your views here.
def iniciarSesion(request):


    template = "login.html"
    template = "signin.html"
    print request.user.is_authenticated()
    if not request.user.is_authenticated():
        if request.method == "POST":
            iniciar_sesion = FormInciarSesion(request.POST)
            if iniciar_sesion.is_valid():
                user = iniciar_sesion.cleaned_data['username'] #iniciar_sesion.cleaned_data['iniciar_input_email']
                clave = iniciar_sesion.cleaned_data['password']#iniciar_sesion.cleaned_data['iniciar_input_password']
                acceso = authenticate(username=user,password=clave)
                #return redirect("/admin/")
                if acceso is not None:
                    if acceso.is_active:
                        if acceso.is_staff:
                            login(request,acceso)

                            return HttpResponseRedirect('/admin/')

                        else :


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
        template = "asistencia.html"
        return render_to_response(template,{},context_instance=RequestContext(request))
    	#return HttpResponseRedirect("/ventas/")
    	

	
@login_required(login_url='/cuenta/login')
def cerrarSesion(request):
    logout(request)
    return  HttpResponseRedirect('/')


def asistencia(request):
    print "tiempo"
    fecha = datetime.datetime.now()
    if request.method == 'POST':
        try:            
            traba = SucursalTrabajador.objects.get(trabajador=request.user)
            tipo = request.POST.get('tipo',"")
            print "post"
            #Asistencia Manana
            if tipo.strip().lower() == "on":
                asistir = AsistenciaTrabajador.objects.filter(Q(hora_ingreso__year=fecha.year) , Q(hora_ingreso__month=fecha.month), Q(hora_ingreso__day=fecha.day) )
                if len(asistir)==1:
                    #actualizar = asistir.get()
                    actualizar = 'Ya se marco hora de ingreso'
                elif len(asistir) == 0:
                    AsistenciaTrabajador.objects.create(trabajador = traba,hora_ingreso=fecha)
                    actualizar = 'Hora de Ingreso registrado'
                else:
                    print "Ha ocurrido un error, duplicidad de data"
                    actualizar = "Ha Ocurrido un error"    
            elif tipo.strip().lower() == "off":
                #Asumimos que este es off-Asistencia Salida
                asistir = AsistenciaTrabajador.objects.filter(Q(hora_ingreso__year=fecha.year) , Q(hora_ingreso__month=fecha.month), Q(hora_ingreso__day=fecha.day) )
                if len(asistir) == 1:
                    #code para registrar salida
                    salida = AsistenciaTrabajador.objects.filter(Q(hora_salida__year=fecha.year) , Q(hora_salida__month=fecha.month), Q(hora_salida__day=fecha.day) )
                    if len(salida) == 1:
                        actualizar = 'Ya se marco hora de salida'
                    elif len(salida) == 0:
                        asistir = asistir.get()
                        asistir.hora_salida = fecha
                        asistir.save()
                        actualizar = 'Hora de Salida registrado'
                    else:
                        print "Ha ocurrido un error, duplicidad de data"
                        actualizar = "Ha Ocurrido un error"
                elif len(asistir) == 0:
                    actualizar = "Primero debe de registrar,su Ingreso"
                else:
                    print "Ha ocurrido un error, duplicidad de data"
                    actualizar = "Ha Ocurrido un error"
        except Exception, e:
            print "fallo"
            print e
            actualizar = "Ha ocurrido un error"
        return HttpResponse(actualizar)
    else:
        return HttpResponse("No se permite, esta accion")
