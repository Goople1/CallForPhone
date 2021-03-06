from django.shortcuts import render_to_response , HttpResponse,render
from django.template.context import RequestContext
from sucursales.models import SucursalTrabajador,DetalleSucursalAlmacen,Sucursal
from productos.models import Producto
from django.contrib.auth.decorators import login_required
from sucursales.utilidades import Utilidades
from ventas.models import  Venta , DetalleVenta
from django.db import transaction, IntegrityError
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.db.models import Q
from forms import FormInciarSesion
from django.contrib.auth import login, authenticate,logout
from sucursales.models import Almacen
from models import AsistenciaTrabajador
import datetime
import json
# from django.http import HttpResponse
# Create your views here.
#fdef para el Home_empleado
#from django.utils import timezone

@login_required(login_url='/cuenta/')
def home_ventas(request):
    print request.user.id
    user_id = request.user.id
    try :
        trabajador = SucursalTrabajador.objects.get(trabajador = user_id)
    except Exception , e :
        print e
        user = User.objects.get(id = user_id)
        print user
        if user.is_staff:
           return HttpResponseRedirect("/admin/")
            #return HttpResponse("Es  Usuario , Pero no Trabajador")
    #template = "empleado_home.html"
    template = "homeEmpleado.html"
    datos = request.session["datos"]
    return render_to_response(template , {"trabajador": trabajador , 'datos':datos} ,context_instance=RequestContext(request))


@login_required(login_url='/cuenta/')
def lista_producto(request):
   
    user_id = request.user.id
    try:
        trabajador = SucursalTrabajador.objects.get(trabajador=user_id)
        print trabajador

    except Exception , e :
        print e
        user = User.objects.get(id = user_id)
        if user.is_staff:
            return HttpResponseRedirect("/admin/")

    
    trabajador_sucursal_id = trabajador.sucursal.id
    sucursal  = Sucursal.objects.get(pk =trabajador_sucursal_id )
    lista_producto = DetalleSucursalAlmacen.objects.filter(sucursal_id = trabajador_sucursal_id)
    template = "homeListaProductoSucursal.html"
    datos = request.session["datos"]
    return render_to_response(template,{"detalle_sucursal_almacen_productos":lista_producto , "sucursal" :sucursal , "datos":datos} , context_instance = RequestContext(request))

@login_required(login_url='/cuenta/')
def venta (request):    

    if request.method == "GET":

        user_id = request.user.id
        try:
            trabajador = SucursalTrabajador.objects.get(trabajador=user_id)
        except Exception , e :
            print e
            user = User.objects.get(id = user_id)
            if user.is_staff:
                return HttpResponseRedirect("/admin/")

        trabajador_sucursal_id = trabajador.sucursal.id
        lista_productos = DetalleSucursalAlmacen.objects.filter(sucursal_id = trabajador_sucursal_id)
        template = "homeVentas.html"
        venta  = True
        datos = request.session["datos"]
        return  render_to_response( template , {"venta":venta,"productos": lista_productos, "trabajador":trabajador, "datos":datos} , context_instance = RequestContext(request))



@login_required(login_url='/login/')
@transaction.atomic()
def addVenta(request):

    if request.method == "POST":
        try:
            with transaction.atomic():
                trabajador = SucursalTrabajador.objects.get(trabajador = request.user.id)
                my_json_products_to_dict = json.loads(request.POST.get("json"))
                if my_json_products_to_dict:
                    total = Utilidades().validarIngresoNum(request.POST.get("total"))
                    venta = Venta(empleado = trabajador , sucursal = trabajador.sucursal , total = total)
                    venta.save()
                    #En my_json_products_to_dict estan todos los productos  que se agregan a la venta       
                    for producto_dict in my_json_products_to_dict :
                        cantidad =  Utilidades().validarIngresoNum(producto_dict.get("cantidad"))
                        tipo_precio = producto_dict.get("tipo_precio")
                        precio  =  producto_dict.get("precio_unitario")
                        importe = producto_dict.get("importe")
                        producto2 = producto_dict.get("producto_id")
                        descripcion = producto_dict.get("descripcion")
                        #Saber que  el Producto Existe :[Porsiaca]
                        detalle_sucursal_producto = DetalleSucursalAlmacen.objects.get(producto_id = producto2 , sucursal_id = trabajador.sucursal)
                    

                        if tipo_precio == "mayor":
                            precio_real = detalle_sucursal_producto.producto_id.precio_x_mayor
                        if  tipo_precio == "menor":
                            precio_real = detalle_sucursal_producto.producto_id.precio_x_menor


                        if detalle_sucursal_producto.stock  > cantidad:
                            detalle_sucursal_producto.stock-= cantidad
                            detalle_venta = DetalleVenta(venta_id = venta,detalle_Sucursal_almacen_id = detalle_sucursal_producto , cantidad = cantidad , tipo_precio  =  tipo_precio , precio =precio , importe = importe, descripcion = descripcion , precio_real = precio_real)
                            detalle_venta.save()
                            detalle_sucursal_producto.save()
                        else:
                            raise IntegrityError
                else :
                    return HttpResponse("JSON VACIO")
        except :
            transaction.rollback()
        else:
            transaction.commit()
        finally:
            return HttpResponse("algo")

@login_required(login_url='/login/')
def modificar_venta(request):

    if request.method == "GET":
        #primero saber en que sucursal estoy  ....
        #Sacar la info del trabajador
        template = "homeModificarVentas.html"
        try:
            trabajador = SucursalTrabajador.objects.get(trabajador = request.user.id)
        except Exception,e :
            print e
            user = User.objects.get(id =request.user.id)
            if user.is_staff:
                return HttpResponseRedirect("/admin/")
        trabajador_sucursal  = trabajador.sucursal
        try:
            ventas = Venta.objects.filter(sucursal = trabajador_sucursal , estado  = True).order_by('-fecha_emision')
        except Exception,e:
            print e

        datos = request.session["datos"]
        return render_to_response( template , {"ventas":ventas , "trabajador" :trabajador , "datos":datos}, context_instance = RequestContext(request))

@login_required(login_url='/login/')
def modificar_detalle_ventas (request,venta_id):

    #FALTA VALIDAR ALGUNOS CAMPOS



    if request.method == "GET":

        try:
            trabajador = SucursalTrabajador.objects.get(trabajador = request.user.id)
        except Exception,e :
            print e
            user = User.objects.get(id =request.user.id)
            if user.is_staff:
                return HttpResponseRedirect("/admin/")
        try:
            venta = Venta.objects.get(id = venta_id , estado = True)
        except Exception ,e :
            print e
            return  HttpResponse("No se puede Acceder a esta Detalle de venta")

        if trabajador.sucursal.id == venta.sucursal.id:

            detalle_venta = DetalleVenta.objects.filter(venta_id = venta_id)
            template = "homeVentas.html"
            modificar = True
            lista_productos = DetalleSucursalAlmacen.objects.filter(sucursal_id = trabajador.sucursal.id)
            datos = request.session["datos"]

            return render_to_response (template , {"trabajador":trabajador,"detalle_venta": detalle_venta , "modificar":modificar,"productos": lista_productos , "ObjVenta" : venta ,"datos":datos} , context_instance = RequestContext(request))
        else :
            return  HttpResponse("ESTE DETALLE PERTENECE A OTRA SUCURSAL")


"""
producto_id
por el momento lo  unico que me interesa  es :

    1.- id producto
    2.- cantidad del  producto
    3.- sucursal
    4.-  ...
"""
@login_required(login_url='/login/')
def cargar_productos(request):

    if request.method == "POST":

        # Obtener el Trabajador para sacarla sucursal
        #trabajador = SucursalTrabajador.objects.get(trabajador = request.user.id)
        dict_products = json.loads(request.POST.get("json"))
        venta_id = request.POST.get("venta_id")

        # de donde saco la sucursal ?  de la VEnta!!!!!!

        venta = Venta.objects.get(id = venta_id)
        venta.sucursal
        venta.estado = False
        venta.save()

        if dict_products:

            for producto in dict_products:
                cantidad =  Utilidades().validarIngresoNum(producto.get("cantidad"))
                producto_id = producto.get("producto_id")
                try:
                    det_sucu_alm_prod_to_add = DetalleSucursalAlmacen.objects.get(producto_id = producto_id , sucursal_id = venta.sucursal)
                except Exception,e:
                    print e
                det_sucu_alm_prod_to_add.stock += cantidad
                det_sucu_alm_prod_to_add.save()
            return HttpResponse("1")
        else :
            return HttpResponse("0")
    else:
        #mensaje = "No se Puede Realizar esta Action"
        return HttpResponse("2")



# Create your views here.
def iniciarSesion(request):
    template = "login.html"
    template = "signin.html"
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
                        login(request,acceso)

                        session = sessionData(request)

                        if session.get("cargo") == "admi":
                            return HttpResponseRedirect('/admin/')
                        else:
                            if session.get("cargo") == "empl":
                                return HttpResponseRedirect('/ventas/')
             
                        # try:
                        #     trabajador = SucursalTrabajador.objects.get(trabajador = request.user)  
                        #     print trabajador.cargo
                        #     if trabajador.cargo.lower() == "empl":

                        #         request.session["datos"] = {"empresa": trabajador.sucursal.nombre,"nombre":trabajador.trabajador.get_full_name()}

                        #         return HttpResponseRedirect('/ventas/')


                        #     else :
                        #         if trabajador.cargo.lower() == "admi":
                        #             request.session["datos"] = {"empresa": trabajador.sucursal.id_almacen.nombre_empresa,"nombre":trabajador.trabajador.get_full_name()}
                        #             print request.session.datos
                        #             return HttpResponseRedirect('/admin/')

                        # except Exception ,e : 
                        #     print e
                        #     print "fail"
                        #     if acceso.is_staff:
                        #         request.session['datos'] = {"empresa": "Administrador","nombre":request.user.get_full_name()}
                        #         return HttpResponseRedirect('/admin/')
                        #     else :
                        #         return render_to_response(template,{'form_iniciar_sesion':iniciar_sesion,'error':'Su cuenta ha sido desactivada,por violar los derechos de uso'},context_instance = RequestContext(request))     
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
        

    
@login_required(login_url='/login/')
def cerrarSesion(request):
    logout(request)
    try:
        del request.session['datos']
    except:
        pass
    return  HttpResponseRedirect('/')


# def asistencia(request):
#     fecha = datetime.datetime.now()
#     if request.method == 'POST':
#         try:            
#             traba = SucursalTrabajador.objects.get(trabajador=request.user)
#             tipo = request.POST.get('tipo',"")
#             print "post"
#             #Asistencia Manana
#             if tipo.strip().lower() == "on":
#                 asistir = AsistenciaTrabajador.objects.filter(Q(hora_ingreso__year=fecha.year) , Q(hora_ingreso__month=fecha.month), Q(hora_ingreso__day=fecha.day) )
#                 if len(asistir)==1:
#                     #actualizar = asistir.get()
#                     actualizar = 'Ya se marco hora de ingreso'
#                 elif len(asistir) == 0:
#                     AsistenciaTrabajador.objects.create(trabajador = traba,hora_ingreso=fecha)
#                     actualizar = 'Hora de Ingreso registrado'
#                 else:
#                     print "Ha ocurrido un error, duplicidad de data"
#                     actualizar = "Ha Ocurrido un error"    
#             elif tipo.strip().lower() == "off":
#                 #Asumimos que este es off-Asistencia Salida
#                 asistir = AsistenciaTrabajador.objects.filter(Q(hora_ingreso__year=fecha.year) , Q(hora_ingreso__month=fecha.month), Q(hora_ingreso__day=fecha.day) )
#                 if len(asistir) == 1:
#                     #code para registrar salida
#                     salida = AsistenciaTrabajador.objects.filter(Q(hora_salida__year=fecha.year) , Q(hora_salida__month=fecha.month), Q(hora_salida__day=fecha.day) )
#                     if len(salida) == 1:
#                         actualizar = 'Ya se marco hora de salida'
#                     elif len(salida) == 0:
#                         asistir = asistir.get()
#                         asistir.hora_salida = fecha
#                         asistir.save()
#                         actualizar = 'Hora de Salida registrado'
#                     else:
#                         print "Ha ocurrido un error, duplicidad de data"
#                         actualizar = "Ha Ocurrido un error"
#                 elif len(asistir) == 0:
#                     actualizar = "Primero debe de registrar,su Ingreso"
#                 else:
#                     print "Ha ocurrido un error, duplicidad de data"
#                     actualizar = "Ha Ocurrido un error"
#         except Exception, e:
#             print "fallo"
#             print e
#             actualizar = "Ha ocurrido un error"
#         return HttpResponse(actualizar)
#     else:
#         template = "asistencia.html"
#         datos = request.session["datos"]

#         return render_to_response(template,{"datos": datos},context_instance=RequestContext(request))


@login_required(login_url='/login/')
def home_empleado_menu_reporte(request):
    if request.method == "GET":
        if request.user.is_staff:
            return HttpResponseRedirect("/admin/")

        elif  request.user.is_active:
            try:
                trabajador =  SucursalTrabajador.objects.get(trabajador = request.user.id)
            except Exception, e:
                print e

            template = "homeEmpleadoReporte.html"
            datos = request.session["datos"]

            return render_to_response(template , {"trabajador":trabajador , "datos":datos} , context_instance=RequestContext(request) )
        else :
            return HttpResponse("ERROR ")
    else : 
        return HttpResponse("Error")


@login_required(login_url='/login/')
def reporte_venta (request):
    if request.method == "GET":
        if request.user.is_staff:
            return HttpResponseRedirect("/admin/")

        elif  request.user.is_active:
            try:
                trabajador =  SucursalTrabajador.objects.get(trabajador = request.user.id)
            except Exception, e:
                print e
                return HttpResponse("error")

            template = "homeEmpleadoReporteVentas.html"
            ventas = Venta.objects.filter(sucursal = trabajador.sucursal.id , estado  = True).order_by('-fecha_emision')
            datos = request.session["datos"]

            return render_to_response(template , {"trabajador":trabajador , "ventas":ventas , "datos":datos} , context_instance=RequestContext(request) )
        else :
            return HttpResponse("ERROR ")
    else : 
        return HttpResponse("Error")






def detalle_venta(request):


    if request.method  == "GET":


        if request.user.is_staff:
            return HttpResponseRedirect("/admin/")

        elif  request.user.is_active:
            try:
                trabajador =  SucursalTrabajador.objects.get(trabajador = request.user.id)
            except Exception, e:
                print e
                return HttpResponse("error")

            codido =Utilidades().validarIngresoNum(request.GET.get("codigo"))

            try:
                venta = Venta.objects.get(id = codido)
            except Exception, e:
                print e
                HttpResponse("Error")

            if trabajador.sucursal.id == venta.sucursal.id:
                det = DetalleVenta.objects.filter(venta_id = venta.id)
                if det:

                    data = [Utilidades().detalle_venta_to_json(detalle) for detalle in det] 
                else :

                    data = []

                return HttpResponse( json.dumps(data) , content_type='application/json')
                
def sessionData(request):
    print "datos"
    print "datos" in request.session
    #print request.session['datos']

    if "datos" in request.session:
        return request.session['datos']
    else:
        try:
            trabajador = SucursalTrabajador.objects.get(trabajador = request.user)  
            if trabajador.cargo.lower() == "empl":
                request.session["datos"] = {"empresa": trabajador.sucursal.nombre,"nombre":trabajador.trabajador.get_full_name() , "cargo" : trabajador.cargo}
            else :
                if trabajador.cargo.lower() == "admi":
                    request.session["datos"] = {"empresa": trabajador.sucursal.id_almacen.nombre_empresa,"nombre":trabajador.trabajador.get_full_name(),"cargo" : trabajador.cargo}
        except Exception ,e : 

            try:
                if not request.user.is_anonymous() :
                    if request.user.is_staff:
                        request.session['datos'] = {"empresa": "Administrador","nombre":request.user.get_full_name(),"cargo":"admi"}

                else : 
                    return HttpResponseRedirect("/login")

            except Exception ,e   :
                print e
                    
        return request.session['datos']
            

            

