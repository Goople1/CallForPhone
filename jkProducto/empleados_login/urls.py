from django.conf.urls  import patterns,url
from empleados_login import views 

urlpatterns = patterns('',

	url(r'^$',views.iniciarSesion , name='iniciarSesion'),
	url(r'^logout/$',views.cerrarSesion , name='cerrarSesion'),


  	)