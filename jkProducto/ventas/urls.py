from django.conf.urls  import patterns,url
from ventas import views 

urlpatterns = patterns('',

	url(r'^$',views.home_ventas , name='home_ventas'),
	url(r'^listaproducto/$',views.lista_producto , name='lista_producto'),
	url(r'^realizarventa/$',views.venta , name='venta'),

  	)