from django.shortcuts import render,render_to_response
from django.template.context import RequestContext
from models import Sucursal
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
	pass

def editSucursalE(request,id):
	pass

def listSucursalL(request,id):
	pass

#Asignacion de Pedidos a Sucursales
def registrarPedidoSucursal(request):
	pass