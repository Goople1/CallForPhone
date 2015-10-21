from django.shortcuts import render_to_response , HttpResponse
from django.template.context import RequestContext
from models import Sucursal , DetalleAlmacen , DetalleSucursalAlmacen
from productos.models import Producto
from sucursales.utilidades import Utilidades
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def mantenimientoSucursal(request):
	template = 'MantenimientoAsignacionSucursales.html'
	template = 'modificarProductoSucursalOriginal.html'
	template = 'ListarProductosOriginal.html'
	template = 'signin.html'
	return render_to_response(template,{},context_instance=RequestContext(request))

def addSucursal(request):
	template='ListarSucursales.html'
	operation = 'addSucursalA'
	sucursal = Sucursal.objects.all()
	return render_to_response(template,{'sucursales':sucursal,'operation':operation},context_instance=RequestContext(request))

def editSucursal(request):
	template='ListarSucursales.html'
	operation = 'editSucursalE'
	sucursal = Sucursal.objects.all()
	return render_to_response(template,{'sucursales':sucursal,'operation':operation},context_instance=RequestContext(request))

def listSucursal(request):
	template='ListarSucursales.html'
	operation = 'listSucursalL'
	sucursal = Sucursal.objects.all()
	return render_to_response(template,{'sucursales':sucursal,'operation':operation},context_instance=RequestContext(request))


def addSucursalA(request,id):

	template = 'AddProductosSucursal.html'

	#para Sacar los productos  que ya existen en  los DetallesSucursalAlmacen  de una Sucursal 

	sucursal_id = id 
	print sucursal_id

	try:
		Sucursal.objects.get(pk=sucursal_id)
		try:
			detalle_sucursal_almacen_productos = DetalleSucursalAlmacen.objects.filter(sucursal_id = sucursal_id)
		
		except Exception, e:
			print e
			return  HttpResponse("PROBLEMAS CON SERVER")
		

		if detalle_sucursal_almacen_productos:
			id_producto_detalle_sucu_almacen = [deta.producto_id for deta in  detalle_sucursal_almacen_productos]
			print "Productos en Detalle Sucursal Almacen"
			print id_producto_detalle_sucu_almacen
			print "Productos En Detalle Almacen que no estan En DetalleSucursalAlmacen "
			detalle_almacen_productos = DetalleAlmacen.objects.exclude(producto_id__in= id_producto_detalle_sucu_almacen)
			print detalle_almacen_productos


		else:
			print " No hay nada en la lista asi que rojo par y pasa "
			detalle_almacen_productos  =  DetalleAlmacen.objects.only("producto_id")
	
	except Exception, e:
		return HttpResponse("<html><body>PAGE NOT FOUND</body></html>")


	return render_to_response (template, {'productos':detalle_almacen_productos ,'id_sucursal': sucursal_id} , context_instance = RequestContext(request))
	

def editSucursalE(request,id):
	template  = "modificarProductoSucursal.html"
	sucursal_id = id
	print "dsdfsd"
	
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

	return render_to_response(template,{"productos": id_producto_detalle_sucu_almacen , 'id_sucursal': sucursal_id },context_instance = RequestContext(request))
	

def listSucursalL(request,id):

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


	template = "listaProductosSucursalAlmacen.html"
	return render_to_response (template, locals() , context_instance = RequestContext(request))
	
#Asignacion de Pedidos a Sucursales
def registrarPedidoSucursal(request):
	pass


def dameStock(request):
	print "Consultando Stock de DetalleAlmecen"

	if request.method == "GET":
		print "pase el get"
		a =  request.GET.get("codigo_producto")

		codigo_producto = Utilidades().validarIngresoNum(a)
		print codigo_producto

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
			print mensaje
			mensaje = ""
			return HttpResponse(mensaje)
	else : 
		print "algo paso"


def addProductotoSucursal(request):
	if request.method == "POST":

		producto_id = Utilidades().validarIngresoNum(request.POST.get("producto_id"))
		sucursal_id  = Utilidades().validarIngresoNum(request.POST.get("sucursal_id"))
		stock_add = Utilidades().validarIngresoNum(request.POST.get("stock_add"))
		


		if ((producto_id != 0) & (producto_id > 0) ):

			print "pass"
			if stock_add > 0 :

				print "pase is digit"
				try : 
					detalle_almacen = DetalleAlmacen.objects.get(producto_id = producto_id )
				except Exception,e:
					print e
					mensaje = "Problemas con el SERVER"
					return HttpResponse(mensaje)

				print detalle_almacen
				detalle_almacen.stock -= stock_add
				print detalle_almacen.stock

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

				print producto
				print "............"
				print sucursal
				print "Creando el detalleSurcusalAlmacen"
				# Para crear Objetos con  campos que son llaves Foraneas ,  se debe Vincular  un  Objeto  del Tipo  de  esa  Llave
				print "fin de Crear detalleSurcusalAlmacen"
				#se Crea el DetalleSucursalAlamcen

				try:
					DetalleSucursalAlmacen.objects.create(stock = stock_add, producto_id = producto , sucursal_id =  sucursal) 
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


def StockDetalleSucursalAlmacen(request):

	print "Dentro de StockDetalleSucursalAlmacen"
	if request.method == "GET":

		cod_prod = Utilidades().validarIngresoNum(request.GET.get('codigo_producto'))
		cod_suc = Utilidades().validarIngresoNum(request.GET.get('codigo_sucursal'))

		print "codigo_producto:",cod_prod
		print "codigo_sucursal:",cod_suc

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

def editProductotoSucursal(request):

	print "Editar Producto  de DetalleSucursalAlmacen ..."
	print "Obteniendo  datos  ... "

	if request.method == "POST":
		
		sucursal_id  = Utilidades().validarIngresoNum(request.POST.get("sucursal_id",0))

		producto_id = Utilidades().validarIngresoNum(request.POST.get("producto_id",0))
		#funcion que cuando no sea un numero me retorne 0 
		stock_add = Utilidades().validarIngresoNum(request.POST.get("stock_add",0))
		# stock_dispo = request.POST.get("stock_dispo")

		print "Datos Obtenidos :  "
		print  "Sucursal_id :  %s , producto_id : %s , stock_add : %s " %(sucursal_id,producto_id,stock_add)

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

			print "...................................."
			print type(detalle_almacen.stock),type(stock_add)
			print "....................................."

			if(detalle_almacen.stock >= stock_add):

				detalle_almacen.stock-=stock_add
				producto_detalle_sucursal_almacen.stock+=stock_add
				detalle_almacen.save()
				producto_detalle_sucursal_almacen.save()
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
		return HttpResponse(" 27 rojo , impar  y pasa ")







