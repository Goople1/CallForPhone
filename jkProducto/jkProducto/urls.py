from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jkProducto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'productos.views.home', name='home'),
    url(r'^login/$', 'productos.views.iniciarSesion', name='login'),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('sucursales.views',
 	url(r'^mantenimientoSucursal/$', 'mantenimientoSucursal', name='mantenimientoSucursal'),
 	url(r'^mantenimientoSucursal/add/$', 'addSucursal', name='add'),
 	url(r'^mantenimientoSucursal/edit/$', 'editSucursal', name='edit'),
 	url(r'^mantenimientoSucursal/list/$', 'listSucursal', name='list'),
 	url(r'^mantenimientoSucursal/add/(?P<id>[\w-]+)/$', 'addSucursalA',name = 'addSucursalA'),
 	url(r'^mantenimientoSucursal/edit/(?P<id>[\w-]+)/$', 'editSucursalE',name='editSucursalE'),
 	url(r'^mantenimientoSucursal/list/(?P<id>[\w-]+)/$', 'listSucursalL',name='listSucursalL'),
 	url(r'^mantenimientoSucursal/dameStock/$', 'dameStock',name='stock'),
 	url(r'^mantenimientoSucursal/StockDetalleSucursalAlamcen/$', 'StockDetalleSucursalAlmacen',name='stockDetSecAl'),
 	url(r'^mantenimientoSucursal/addProductotoSucursal/$', 'addProductotoSucursal',name='addProductotoSucursal'),	
 	url(r'^mantenimientoSucursal/editProductotoSucursal/$', 'editProductotoSucursal',name='editProductotoSucursal'),	

 	

 )

urlpatterns += patterns('productos.views',

	url(r'^producto/filtroproducto/$', 'filtroproductos',name='filtroproductos'),
	url(r'^producto/filtrocriterio/$', 'filtrocriterio',name='filtrocriterio'),
	




	)