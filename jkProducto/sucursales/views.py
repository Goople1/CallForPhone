from django.shortcuts import render_to_response , HttpResponse,render
from django.template.context import RequestContext
from models import Sucursal , DetalleAlmacen , DetalleSucursalAlmacen, HistorialDetalleSucursalAlmacen
from productos.models import Producto
from sucursales.utilidades import Utilidades
from django.core.exceptions import ObjectDoesNotExist
from ventas.models import Venta
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from ventas.models import DetalleVenta
import json
import djqscsv




# Create your views here.

@login_required(login_url='/cuenta/')
def mantenimientoSucursal(request):
	#template = 'MantenimientoAsignacionSucursales.html'
	#template = 'modificarProductoSucursalOriginal.html'
	#template = 'ListarProductosOriginal.html'
	# template = 'signin.html'
	#template = "IndiceOriginal.html"
	#template = 'AddProductosSucursal.html'
	#template = 'ListarSucursales.html' #fake
	#template = 'registrarProductoOriginal.html'
	if  is_admin(request.user.id):
		template = 'mantenimientoSucursal.html'
		datos = request.session["datos"]
		return render_to_response(template,{"datos":datos},context_instance = RequestContext(request))

	else :
		return HttpResponseRedirect("/ventas/")

@login_required(login_url='/cuenta/')
def addSucursal(request):
	if is_admin(request.user.id):
		template='ListarSucursales.html'
		template = "IndiceOriginal.html"
		operation = 'addSucursalA'
		sucursal = Sucursal.objects.all()
		datos = request.session["datos"]

		return render_to_response(template,{'sucursales':sucursal,'operation':operation , "datos":datos},context_instance=RequestContext(request))

	else :
		return HttpResponseRedirect("/ventas/")

@login_required(login_url='/cuenta/')
def editSucursal(request):
	if is_admin(request.user.id):
		template='ListarSucursales.html'
		template = "IndiceOriginal.html"
		operation = 'editSucursalE'
		sucursal = Sucursal.objects.all()
		datos = request.session["datos"]

		return render_to_response(template,{'sucursales':sucursal,'operation':operation,"datos":datos},context_instance=RequestContext(request))

	else:
		return HttpResponseRedirect("/ventas/")

@login_required(login_url='/cuenta/')
def listSucursal(request):
	if is_admin(request.user.id):
		template='ListarSucursales.html'
		template = "IndiceOriginal.html"
		operation = 'listSucursalL'
		sucursal = Sucursal.objects.all()
		datos = request.session["datos"]

		return render_to_response(template,{'sucursales':sucursal,'operation':operation , "datos" : datos},context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect("/ventas/")

@login_required(login_url='/cuenta/')
def historialVentas(request):
	if is_admin(request.user.id):
		template = "IndiceOriginal.html"
		operation = 'histoSucursalVentasAdm'
		sucursal = Sucursal.objects.all()
		datos = request.session["datos"]

		return render_to_response(template,{'sucursales':sucursal,'operation':operation , "datos":datos},context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect("/ventas/")

@login_required(login_url='/cuenta/')
def Historial_ventas_Sucursal_Admin(request,id):

	if is_admin(request.user.id):

		sucursal_id = Utilidades().validarIngresoNum(id)

		try:
			ventas  = Venta.objects.filter(sucursal = sucursal_id,estado=True).order_by('-fecha_emision')
		except Exception,e :
			print e

		template  = "reporteHistorialVenta.html"
		datos = request.session["datos"]
		return render_to_response(template , {"ventas":ventas , "datos" : datos} , context_instance  = RequestContext(request))

	else:
		return HttpResponseRedirect("/ventas/")


@login_required(login_url='/cuenta/')
def addSucursalA(request,id):

	#template = 'AddProductosSucursal.html'
	#template = 'mantenimientoSucursal.html'

	if is_admin(request.user.id):

		template = 'registrarProductoOriginal.html'

		#para Sacar los productos  que ya existen en  los DetallesSucursalAlmacen  de una Sucursal 
		sucursal_id = id 

		try:
			Sucursal.objects.get(pk=sucursal_id)
			try:
				detalle_sucursal_almacen_productos = DetalleSucursalAlmacen.objects.filter(sucursal_id = sucursal_id)
			
			except Exception, e:
				print e
				return  HttpResponse("PROBLEMAS CON SERVER")
			

			if detalle_sucursal_almacen_productos:
				id_producto_detalle_sucu_almacen = [deta.producto_id for deta in  detalle_sucursal_almacen_productos]
				#print "Productos en Detalle Sucursal Almacen"
				#print id_producto_detalle_sucu_almacen
				#print "Productos En Detalle Almacen que no estan En DetalleSucursalAlmacen "
				detalle_almacen_productos = DetalleAlmacen.objects.exclude(producto_id__in= id_producto_detalle_sucu_almacen)
				#print detalle_almacen_productos


			else:
				#print " No hay nada en la lista asi que rojo par y pasa "
				detalle_almacen_productos  =  DetalleAlmacen.objects.only("producto_id")
		
		except Exception, e:
			return HttpResponse("<html><body>PAGE NOT FOUND</body></html>")

		datos = request.session["datos"]
		return render_to_response (template, {'productos':detalle_almacen_productos ,'id_sucursal': sucursal_id , "datos":datos} , context_instance = RequestContext(request))

	else :
		return HttpResponseRedirect("/ventas/")

		
@login_required(login_url='/cuenta/')
def editSucursalE(request,id):
	if is_admin(request.user.id):
		#template  = "modificarProductoSucursal.html"
		template = "modificarProductoSucursalOriginal.html"
		sucursal_id = id
		
		
		try:

			Sucursal.objects.get(pk=sucursal_id)
			
			try:
				detalle_sucursal_almacen_productos = DetalleSucursalAlmacen.objects.filter(sucursal_id = sucursal_id)
			except Exception, e:
				print e
				return HttpResponse("Problemas Con el  Server")

		except ObjectDoesNotExist,e:

			return HttpResponse("<html><body>PAGE NOT FOUND</body></html>")

		id_producto_detalle_sucu_almacen = [detalle.producto_id for detalle  in detalle_sucursal_almacen_productos]

		datos = request.session["datos"]

		return render_to_response(template,{"productos": id_producto_detalle_sucu_almacen , 'id_sucursal': sucursal_id , "datos":datos },context_instance = RequestContext(request))
	else:
		return HttpResponseRedirect("/ventas/")
	



@login_required(login_url='/cuenta/')
def listSucursalL(request,id):

	if is_admin(request.user.id):

		sucursal_id = Utilidades().validarIngresoNum(id)
		try:
			sucursal = Sucursal.objects.get(pk=sucursal_id)


			try:
				detalle_sucursal_almacen_productos = DetalleSucursalAlmacen.objects.filter(sucursal_id = sucursal)
			except Exception, e:
				return HttpResponse("Problemas del Server")

		
		except Exception, e : 
			print e  
			mensaje ="<html>	<head>		<title></title>		</head>		<body>			<h1> PAGE NOT FOUND!</h1>		</body>		</html>"
			return HttpResponse(mensaje)


		#template = "listaProductosSucursalAlmacen.html"
		template = "ListarProductosOriginal.html"
		datos = request.session["datos"]
		
		return render_to_response (template, locals() , context_instance = RequestContext(request))
	else: 
		return HttpResponseRedirect("/ventas/")
	
#Asignacion de Pedidos a Sucursales
def registrarPedidoSucursal(request):
	pass

@login_required(login_url='/cuenta/')
def dameStock(request):


	if request.method == "GET":
		#print "pase el get"
		a =  request.GET.get("codigo_producto")

		codigo_producto = Utilidades().validarIngresoNum(a)
		#print codigo_producto

		if(codigo_producto != 0) & (codigo_producto > 0):
			try:
				
				da = DetalleAlmacen.objects.get(producto_id=codigo_producto)
			except Exception, e:

				print e
				return HttpResponse("Problemas Con el SERVER!!!")
			
			da = da.stock
			return  HttpResponse(da)

		else:
			mensaje = "imposible de encontrar el Producto "
			return HttpResponse(mensaje)
	else : 
		return HttpResponse("Only Get")


@login_required(login_url='/cuenta/')
def addProductotoSucursal(request):

	if request.method == "POST":
		producto_id = Utilidades().validarIngresoNum(request.POST.get("producto_id"))
		sucursal_id  = Utilidades().validarIngresoNum(request.POST.get("sucursal_id"))
		stock_add = Utilidades().validarIngresoNum(request.POST.get("stock_add"))
		if ((producto_id != 0) & (producto_id > 0) ):

			#print "pass"
			if stock_add > 0 :

				#print "pase is digit"
				try : 
					detalle_almacen = DetalleAlmacen.objects.get(producto_id = producto_id )
				except Exception,e:
					print e
					mensaje = "Problemas con el SERVER"
					return HttpResponse(mensaje)

				#print detalle_almacen
				detalle_almacen.stock -= stock_add
				

				try:
					producto = Producto.objects.get(id = producto_id)
				except ObjectDoesNotExist, e :
					print e
					mensaje = "Producto no Encontrado,Pruebe otra vez"
					return HttpResponse(mensaje)
				
				try : 
					sucursal = Sucursal.objects.get(id = sucursal_id)
				except ObjectDoesNotExist, e:
					print e 
					mensaje = "Es posible que la Sucursal no Exista, Intente otra vez"
					return HttpResponse(mensaje)

				#print producto
				#print "............"
				#print sucursal
				#print "Creando el detalleSurcusalAlmacen"
				# Para crear Objetos con  campos que son llaves Foraneas ,  se debe Vincular  un  Objeto  del Tipo  de  esa  Llave
				#print "fin de Crear detalleSurcusalAlmacen"
				#se Crea el DetalleSucursalAlamcen

				try:
					detalleSA = DetalleSucursalAlmacen(stock = stock_add, producto_id = producto , sucursal_id =  sucursal) 
					
					detalleSA.save()
					HistorialDetalleSucursalAlmacen.objects.create(stock_actual =detalleSA.stock ,id_detalle_sucursal_almacen=detalleSA)

				except Exception , e : 
					print e 
					mensaje = "no se puede Guardar los Datos , Parece Que ya Existen , Intente Otro vez"
					return HttpResponse(mensaje)

				detalle_almacen.save()
				return HttpResponse("Done!")
				#SeGuardan Los cambios para el Stock de DetalleAlmacen

			else:
				return HttpResponse("Algo va mal ")
		else : 
			return HttpResponse("No se Eligio ningun Producto")

	else: 
		return HttpResponse("No es posible esta accion por metodo Get")

@login_required(login_url='/cuenta/')
def StockDetalleSucursalAlmacen(request):

	
	if request.method == "GET":

		cod_prod = Utilidades().validarIngresoNum(request.GET.get('codigo_producto'))
		cod_suc = Utilidades().validarIngresoNum(request.GET.get('codigo_sucursal'))

		

		if (cod_prod != 0) & (cod_prod > 0) :
			try:
				product = DetalleSucursalAlmacen.objects.get(sucursal_id = cod_suc,producto_id = cod_prod)

			except Exception, e:
				print e
				return HttpResponse("Problemas con el Server!!!!")
			
			rsp =  product.stock
			return HttpResponse(rsp)
			
		else:
			mensaje = "No se Eligio ningun producto"
			print mensaje
			mensaje = ""
			return HttpResponse(mensaje)


	else:
		mensaje = "27 rojo , impar  y pasas "
		print mensaje
		return HttpResponse(mensaje)


@login_required(login_url='/cuenta/')
def editProductotoSucursal(request):

	if request.method == "POST":
		
		sucursal_id  = Utilidades().validarIngresoNum(request.POST.get("sucursal_id",0))

		producto_id = Utilidades().validarIngresoNum(request.POST.get("producto_id",0))
		#funcion que cuando no sea un numero me retorne 0 
		stock_add = Utilidades().validarIngresoNum(request.POST.get("stock_add",0))
		# stock_dispo = request.POST.get("stock_dispo")


		if(producto_id != 0 )& (producto_id > 0):

			try:
				producto_detalle_sucursal_almacen = DetalleSucursalAlmacen.objects.get(sucursal_id=sucursal_id , producto_id=producto_id)
			except Exception,e :
				print e
				return HttpResponse("No Es Posible Editar  el Producto  en  la Sucursal ")

			print producto_detalle_sucursal_almacen.producto_id
			print producto_detalle_sucursal_almacen.stock

			try:
				detalle_almacen = DetalleAlmacen.objects.get(producto_id=producto_id)
			except Exception, e:
				print e
				return HttpResponse ("Problemas con el Server")

			if(detalle_almacen.stock >= stock_add): 
				detalle_almacen.stock-=stock_add
				antes_dsa = producto_detalle_sucursal_almacen.stock
				producto_detalle_sucursal_almacen.stock+=stock_add
				detalle_almacen.save()
				producto_detalle_sucursal_almacen.save()
				HistorialDetalleSucursalAlmacen.objects.create(stock_actual =antes_dsa,stock_adicional= stock_add,id_detalle_sucursal_almacen=producto_detalle_sucursal_almacen)
				return HttpResponse("Modificacion  del Producto hecha")
			else:
				mensaje = "La Cantidad En el Almacen  no es Suficiente para su Pedido"
				print mensaje
				return HttpResponse(mensaje)
		else:
			mensaje = "Imposible encontrar el producto"
			print mensaje
			return HttpResponse(mensaje)

	else: 
		return HttpResponse(" Problemas Con el Server")






def is_admin(user_id):

	user = User.objects.get(id = user_id)

	if user.is_staff:

 		return True

	else: 
		return False

def export(request , suc_id):

	sucursal_id = Utilidades().validarIngresoNum(suc_id)

	detalle_productos_sucursal	=	DetalleSucursalAlmacen.objects.filter(sucursal_id = sucursal_id)

	data = detalle_productos_sucursal.values('id','producto_id__tipo_producto__nombre','producto_id__marca__nombre','producto_id__codigo','producto_id__color','stock','producto_id__precio_x_menor','producto_id__precio_x_mayor')	
	#field_header_map={'producto_id__tipo_producto__nombre': 'TIPO','producto_id__marca__nombre':'MARCA','producto_id__codigo': 'MODELO' , 'producto_id__color':'COLOR', 'producto_id__precio_x_menor': 'PRECIO por Menor' , 'producto_id__precio_x_mayor': 'Precio por Mayor'}
	
	# qs = Producto.objects.all()
	return djqscsv.render_to_csv_response(data,field_header_map = {'producto_id__tipo_producto__nombre': 'TIPO','producto_id__marca__nombre':'MARCA','producto_id__codigo': 'MODELO' , 'producto_id__color':'COLOR', 'producto_id__precio_x_menor': 'PRECIO por Menor' , 'producto_id__precio_x_mayor': 'Precio por Mayor'})


@login_required(login_url='/cuenta/')
def prueba(request):
	

	if request.method == "GET":


		if request.user.is_staff:


			codido =Utilidades().validarIngresoNum(request.GET.get("codigo"))
			try:
				venta = Venta.objects.get(id = codido)
			except Exception, e:
				print e
				HttpResponse("Error")
			det = DetalleVenta.objects.filter(venta_id = venta.id)

			if det:
				data = [Utilidades().detalle_venta_to_json(detalle) for detalle in det] 


			else :
				data = []
			return HttpResponse( json.dumps(data) , content_type='application/json')

		else :
			return HttpResponse("Zorry")


	else :
		return HttpResponse("Zorry")






def sessionData(request):
    if request.session['datos']:
        return request.session['datos']
    else:
        try:
            trabajador = SucursalTrabajador.objects.get(trabajador = request.user)  
            if trabajador.cargo.lower() == "empl":
                request.session["datos"] = {"empresa": trabajador.sucursal.nombre,"nombre":trabajador.trabajador.get_full_name()}
            else :
                if trabajador.cargo.lower() == "admi":
                    request.session["datos"] = {"empresa": trabajador.sucursal.id_almacen.nombre_empresa,"nombre":trabajador.trabajador.get_full_name()}
        except Exception ,e : 
            if acceso.is_staff:
                request.session['datos'] = {"empresa": "Administrador","nombre":request.user.get_full_name()}
            return request.session['datos']








