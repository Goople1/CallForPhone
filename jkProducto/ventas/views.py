from django.shortcuts import render_to_response , HttpResponse
from django.template.context import RequestContext
from sucursales.models import SucursalTrabajador,DetalleSucursalAlmacen,Sucursal
from django.contrib.auth.decorators import login_required

# from django.http import HttpResponse

# Create your views here.

#fdef para el Home_empleado

@login_required(login_url='/cuenta/login')
def home_ventas(request):
	print request.user.id
	user_id = request.user.id
	try :
		trabajador = SucursalTrabajador.objects.get(trabajador = user_id)
		print trabajador._meta.get_all_field_names()
	except Exception , e :
		print e
		return HttpResponse("Es  Usuario , Pero no Trabajador")

	template = "empleado_home.html"
	return render_to_response(template , {"trabajador": trabajador} , context_instance=RequestContext(request))

@login_required(login_url='/cuenta/login')
def lista_producto (request):

	user_id = request.user.id
	print "Con Only () "
	trabajador = SucursalTrabajador.objects.get(trabajador = user_id)
	print trabajador 

	print "+++++++++++++++++++++++++++++++++++++"
	print "sin Only () "
	trabajador = SucursalTrabajador.objects.get(trabajador = user_id)
	trabajador_sucursal_id = trabajador.sucursal.id
	print trabajador_sucursal_id
	sucursal  = Sucursal.objects.get(pk =trabajador_sucursal_id )
	lista_producto = DetalleSucursalAlmacen.objects.filter(sucursal_id = trabajador_sucursal_id)
	template = "listaProductosSucursalAlmacen.html"

	return render_to_response(template,{"detalle_sucursal_almacen_productos":lista_producto , "sucursal" :sucursal} , context_instance = RequestContext(request))

@login_required(login_url='/cuenta/login')
def venta (request):	

	user_id = request.user.id
	trabajador = SucursalTrabajador.objects.get(trabajador = user_id)

	if request.method == "POST":
		return 

	else:
		trabajador_sucursal_id = trabajador.sucursal.id
		template = "template_ventas.html"
		lista_productos = DetalleSucursalAlmacen.objects.filter(sucursal_id = trabajador_sucursal_id)
		return  render_to_response( template , {'productos': lista_productos} , context_instance = RequestContext(request))
	 





