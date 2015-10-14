from django.shortcuts import render_to_response , HttpResponse
from django.template.context import RequestContext
from models import Sucursal , DetalleAlmacen , DetalleSucursalAlmacen
from productos.models import Producto

# Create your views here.

def mantenimientoSucursal(request):
	template = 'MantenimientoAsignacionSucursales.html'
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

	detalle_sucursal_almacen_productos = DetalleSucursalAlmacen.objects.filter(sucursal_id = sucursal_id)

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

	return render_to_response (template, {'productos':detalle_almacen_productos ,'id_sucursal': sucursal_id} , context_instance = RequestContext(request))
	

def editSucursalE(request,id):
	template  = "modificarProductoSucursal.html"
	sucursal_id = id
	detalle_sucursal_almacen_productos = DetalleSucursalAlmacen.objects.filter(sucursal_id = sucursal_id)
	id_producto_detalle_sucu_almacen = [detalle.producto_id for detalle  in detalle_sucursal_almacen_productos]

	return render_to_response(template,{"productos": id_producto_detalle_sucu_almacen , 'id_sucursal': sucursal_id },context_instance = RequestContext(request))
	

def listSucursalL(request,id):
	pass

#Asignacion de Pedidos a Sucursales
def registrarPedidoSucursal(request):
	pass


def dameStock(request):
	print "Consultando Stock de DetalleAlmecen"

	if request.method == "GET":
		codigo_producto = request.GET.get("codigo_producto", "")

		if((int(codigo_producto) != 0) & (int(codigo_producto) > 0)):

			da = DetalleAlmacen.objects.get(producto_id=codigo_producto)
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

		producto_id = request.POST.get("producto_id")
		sucursal_id  = request.POST.get("sucursal_id")
		stock_add =  request.POST.get("stock_add")
		print producto_id


		if ((int(producto_id) != 0) & (int(producto_id) > 0) ):

			print "pass"
			if stock_add.isdigit():

				print "pase is digit"
				detalle_almacen = DetalleAlmacen.objects.get(producto_id = producto_id )
				print detalle_almacen
				detalle_almacen.stock -= int(stock_add)
				print detalle_almacen.stock
				print int(stock_add)
				producto = Producto.objects.get(id = producto_id)
				sucursal = Sucursal.objects.get(id = sucursal_id)
				print producto
				print "............"
				print sucursal
				print "Creando el detalleSurcusalAlmacen"
				# Para crear Objetos con  campos que son llaves Foraneas ,  se debe Vincular  un  Objeto  del Tipo  de  esa  Llave
				print "fin de Crear detalleSurcusalAlmacen"
				#se Crea el DetalleSucursalAlamcen
				DetalleSucursalAlmacen.objects.create(stock = int(stock_add), producto_id = producto , sucursal_id =  sucursal) 
				#SeGuardan Los cambios para el Stock de DetalleAlmacen
				detalle_almacen.save()
				return HttpResponse("Done!")

			else:
				return HttpResponse("Algo va mal ")
		else : 
			return HttpResponse("No se Eligio ningun Producto")

	else: 
		return HttpResponse("No es posible esta accion por metodo Get")


def StockDetalleSucursalAlmacen(request):

	print "Dentro de StockDetalleSucursalAlmacen"
	if request.method == "GET":

		cod_prod = request.GET.get('codigo_producto')
		cod_suc = request.GET.get('codigo_sucursal')

		print "codigo_producto:",cod_prod
		print "codigo_sucursal:",cod_suc

		if ((int(cod_prod) != 0) & (int(cod_prod) > 0) ):
			product = DetalleSucursalAlmacen.objects.get(sucursal_id = cod_suc,producto_id = cod_prod)
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
		
		sucursal_id  = request.POST.get("sucursal_id")
		producto_id = request.POST.get("producto_id")
		stock_add = int(request.POST.get("stock_add"))
		# stock_dispo = request.POST.get("stock_dispo")

		print "Datos Obtenidos :  "
		print  "Sucursal_id :  %s , producto_id : %s , stock_add : %s " %(sucursal_id,producto_id,stock_add)

		if((int(producto_id) != 0 )& (int(producto_id) > 0)):

			producto_detalle_sucursal_almacen = DetalleSucursalAlmacen.objects.get(sucursal_id=sucursal_id , producto_id=producto_id)
			print producto_detalle_sucursal_almacen.producto_id
			print producto_detalle_sucursal_almacen.stock

			detalle_almacen = DetalleAlmacen.objects.get(producto_id=producto_id)
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







