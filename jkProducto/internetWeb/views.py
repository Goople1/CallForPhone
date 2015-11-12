from django.shortcuts import render_to_response ,HttpResponse
from django.template.context import RequestContext
from  productos.models import Marca , TipoProducto
from  sucursales.models import Sucursal , DetalleSucursalAlmacen

from sucursales.utilidades import Utilidades


def filtroproductos(request):


	#obtener  todas las  sucursales
	try : 
		sucursales = Sucursal.objects.filter(id_estadoSucursal = 1).order_by("nombre")
	except Exception ,e : 
		sucursales = None		

	#obtener todas las Marcas 

	try:
		marcas = Marca.objects.all().order_by("nombre")
	except Exception,e:
		print e;
		marcas = None


	try: 
		tipos = TipoProducto.objects.all().order_by("nombre")
	except Exception,e:
		print e
		tipos = None


	template = "InternetCatalogo.html"
	template = "catalogo.html"
	return render_to_response(template , {"sucursales":sucursales , "marcas" : marcas , "tipos":tipos} ,context_instance = RequestContext(request)) 

def filtrocriterio(request):

	if request.method == "GET":

		#Obtener Datos

		sucursal_id = Utilidades().validarIngresoNum(request.GET.get("sucursal_id"))
		producto_id = Utilidades().validarIngresoNum(request.GET.get("producto_id"))
		tipo_id = Utilidades().validarIngresoNum(request.GET.get("tipo_id"))



		rpt = criteriobusqueda(sucursal_id,producto_id,tipo_id)
		print "criterios"
		print rpt

		if not rpt :

			print  "Pasar todos los Objetos"

			productos = DetalleSucursalAlmacen.objects.all()
			print productos.count()

			if productos:

				print "helllo"
				data = [Utilidades().detalle_sucursal_almacen_to_json(producto) for producto in productos]
				print data

			else : 

				data = []

			return HttpResponse(json.dumps(data) , content_type='application/json')


		else :

			print "rpt  Tiene Criterios"
			try:
				productos = DetalleSucursalAlmacen.objects.filter(**rpt)
				print productos

				if productos:

					print "helllo"
					data = [Utilidades().detalle_sucursal_almacen_to_json(producto) for producto in productos]
					print data

				else : 

					data = []

			except Exception , e:
				 print e
				 return  HttpResponse("Error de Servidor ")
			print productos.count()

			return HttpResponse(json.dumps(data) ,content_type='application/json')


		return HttpResponse("No se puede realizar esta accion")



def criteriobusqueda(suc,pro,tipo):

	criterio = {}

	#any() retorna   True si alguna condicion es True 
	
	valor = [suc,pro,tipo]
	if  not any(valor) :

		# try:
		# 	todo = DetalleSucursalAlmacen.objects.all()
		# except Exception,e:
		# 	print e 
		# 	return HttpResponse("Servidor OFf")

		return criterio

	else: 

		campos = ["suc","prod","tipo"]
		my_dict = dict(zip(campos,valor))
		my_dict = clean_dict_for_value_0(my_dict)

		if "suc" in my_dict :
			regla = {"sucursal_id":my_dict.get("suc")}
			criterio.update(regla)

		if "prod" in my_dict:
			regla = {"producto_id__marca":my_dict.get("prod")}
			criterio.update(regla)

		if "tipo" in my_dict:
			regla = {"producto_id__tipo_producto":my_dict.get("tipo")}
			criterio.update(regla)

		return criterio


#funcion para limpiar  un dictionario  con value difrente de 0
#Teniendo en cuenta que los valores que se pasan son 0 o positivos
def clean_dict_for_value_0 (data):

	d = {k:v for k, v in list(data.items()) if v != 0}

	return d


