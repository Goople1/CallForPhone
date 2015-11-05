from django.shortcuts import render_to_response , HttpResponse
from django.template.context import RequestContext
from sucursales.models import SucursalTrabajador,DetalleSucursalAlmacen,Sucursal
from productos.models import Producto
from django.contrib.auth.decorators import login_required
import json
from sucursales.utilidades import Utilidades
from ventas.models import  Venta , DetalleVenta
from django.db import transaction, IntegrityError
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User




# from django.http import HttpResponse

# Create your views here.

#fdef para el Home_empleado

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
    return render_to_response(template , {"trabajador": trabajador} , context_instance=RequestContext(request))


@login_required(login_url='/cuenta/')
def lista_producto(request):
    print "lista porducto"
    user_id = request.user.id
    try:
        trabajador = SucursalTrabajador.objects.get(trabajador=user_id)
        print trabajador

    except Exception , e :
        print e
        user = User.objects.get(id = user_id)
        if user.is_staff:
            return HttpResponseRedirect("/admin/")

    print "pase try"
    trabajador_sucursal_id = trabajador.sucursal.id
    print trabajador_sucursal_id
    sucursal  = Sucursal.objects.get(pk =trabajador_sucursal_id )
    lista_producto = DetalleSucursalAlmacen.objects.filter(sucursal_id = trabajador_sucursal_id)
    template = "homeListaProductoSucursal.html"
    return render_to_response(template,{"detalle_sucursal_almacen_productos":lista_producto , "sucursal" :sucursal} , context_instance = RequestContext(request))

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
        template = "template_ventas.html"
        venta  = True
        return  render_to_response( template , {"venta":venta,"productos": lista_productos} , context_instance = RequestContext(request))



@login_required(login_url='/cuenta/')
@transaction.atomic()
def addVenta(request):

    if request.method == "POST":
        try:
            with transaction.atomic():
                trabajador = SucursalTrabajador.objects.get(trabajador = request.user.id)
                print trabajador.sucursal
                my_json_products_to_dict = json.loads(request.POST.get("json"))
                if my_json_products_to_dict:
                    print "Create Venta"
                    total = Utilidades().validarIngresoNum(request.POST.get("total"))
                    venta = Venta(empleado = trabajador , sucursal = trabajador.sucursal , total = total)
                    print "--------------------------------------------------"
                    print "--------------------------------------------------"
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
                        producto = Producto.objects.get(id = producto_dict.get("producto_id"))
                        print producto
                        detalle_sucursal_producto = DetalleSucursalAlmacen.objects.get(producto_id = producto2 , sucursal_id = trabajador.sucursal)
                        print detalle_sucursal_producto
                        print "#-------------------------------#"
                        print detalle_sucursal_producto.stock
                        print cantidad
                        print "#-------------------------------#"
                        if detalle_sucursal_producto.stock  > cantidad:
                            detalle_sucursal_producto.stock-= cantidad
                            print "detalle_sucursal cambios"
                            detalle_venta = DetalleVenta(venta_id = venta,detalle_Sucursal_almacen_id = detalle_sucursal_producto , cantidad = cantidad , tipo_precio  =  tipo_precio , precio =precio , importe = importe, descripcion = descripcion)
                            detalle_venta.save()
                            detalle_sucursal_producto.save()
                        else:
                            print "Else"
                            raise IntegrityError
                else :
                    raise IntegrityError
        except :
            print "roll"
            transaction.rollback()
        else:
            transaction.commit()
        finally:
            return HttpResponse("algo")

@login_required(login_url='/cuenta/')
def reporte_ventas(request):

    if request.method == "GET":
        #primero saber en que sucursal estoy  ....
        #Sacar la info del trabajador
        template = "homeReporteVentas.html"
        try:
            trabajador = SucursalTrabajador.objects.get(trabajador = request.user.id)
        except Exception,e :
            print e
            user = User.objects.get(id =request.user.id)
            if user.is_staff:
                return HttpResponseRedirect("/admin/")
        trabajador_sucursal  = trabajador.sucursal
        try:
            ventas = Venta.objects.filter(sucursal = trabajador_sucursal , estado  = True)

        except Exception,e:
            print e

        return render_to_response( template , {"ventas":ventas , "trabajador" :trabajador}, context_instance = RequestContext(request))



@login_required(login_url='/cuenta/')
def detalle_ventas (request,venta_id):

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
        detalle_venta = DetalleVenta.objects.filter(venta_id = venta_id)
        template = "template_ventas.html"
        modificar = True
        lista_productos = DetalleSucursalAlmacen.objects.filter(sucursal_id = trabajador.sucursal.id)
        return render_to_response (template , {"detalle_venta": detalle_venta , "modificar":modificar,"productos": lista_productos , "ObjVenta" : venta} , context_instance = RequestContext(request))

"""
producto_id
por el momento lo  unico que me interesa  es :

    1.- id producto
    2.- cantidad del  producto
    3.- sucursal
    4.-  ...
"""
@login_required(login_url='/cuenta/')
def cargar_productos(request):

    if request.method == "POST":

        # Obtener el Trabajador para sacarla sucursal
        #trabajador = SucursalTrabajador.objects.get(trabajador = request.user.id)
        dict_products = json.loads(request.POST.get("json"))
        venta_id = request.POST.get("venta_id")

        # de donde saco la sucursal ?  de la VEnta!!!!!!

        venta = Venta.objects.get(id = venta_id)
        venta.sucursal


        print "cargar_productos"
        print "datos : "
        print "venta_id : " ,venta_id
        print "json obj : ", dict_products

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




