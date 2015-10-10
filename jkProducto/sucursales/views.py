from django.shortcuts import render,render_to_response
from django.template.context import RequestContext
from models import Sucursal
# Create your views here.
def listarSucusarles(request):
	template='ListarSucursales.html'
	sucursal = Sucursal.objects.all()
	return render_to_response(template,{'sucursales':sucursal},context_instance=RequestContext(request))