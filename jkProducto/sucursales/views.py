from django.shortcuts import render,render_to_response
from django.template.context import RequestContext
from models import Sucursal
# Create your views here.

def mantenimientoSucursal(request):
	template = 'MantenimientoAsignacionSucursales.html'
	return render_to_response(template,{},context_instance=RequestContext(request))

def addSucursal(request):
	template='ListarSucursales.html'
	operation = 'add'
	sucursal = Sucursal.objects.all()
	return render_to_response(template,{'sucursales':sucursal,'operation':operation},context_instance=RequestContext(request))

def editSucursal(request):
	template='ListarSucursales.html'
	operation = 'edit'
	sucursal = Sucursal.objects.all()
	return render_to_response(template,{'sucursales':sucursal,'operation':operation},context_instance=RequestContext(request))

def listSucursal(request):
	template='ListarSucursales.html'
	operation = 'list'
	sucursal = Sucursal.objects.all()
	return render_to_response(template,{'sucursales':sucursal,'operation':operation},context_instance=RequestContext(request))

def listarSucusarles(request):
	template='ListarSucursales.html'
	sucursal = Sucursal.objects.all()
	return render_to_response(template,{'sucursales':sucursal},context_instance=RequestContext(request))

#Asignacion de Pedidos a Sucursales
def registrarPedidoSucursal(request):
	pass