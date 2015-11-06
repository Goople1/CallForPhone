from django.conf.urls  import patterns,url
from ventas import views 

urlpatterns = patterns('',

	url(r'^$',views.home_ventas , name='home_ventas'),
	url(r'^listaproducto/$',views.lista_producto , name='lista_producto'),
	url(r'^realizarventa/$',views.venta , name='venta'),
	url(r'^addVenta/$',views.addVenta , name='addVenta'),
	
	url(r'^reporte/$',views.reporte_ventas, name='reporteve'),
	url(r'^reporte/(?P<venta_id>[0-9]+)/$',views.detalle_ventas, name='detalleventa'),
	url(r'^reporte/asistencia/$',views.reporte_asistencia, name='reporteAsistencia'),
	url(r'^cargarProductos/$',views.cargar_productos, name='cargar_productos'),
	url(r'^asistencia/$',views.asistencia , name='asistencia'),





  	)