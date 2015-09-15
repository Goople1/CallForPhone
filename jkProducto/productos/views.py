from django.shortcuts import render,render_to_response
from django.template.context import RequestContext
# Create your views here.
def home(request):
	template = 'ventas.html'
	return render_to_response(template,{},context_instance=RequestContext(request))

def iniciarSesion(request):
	template='login.html'
	return render_to_response(template,{},context_instance=RequestContext(request)) 