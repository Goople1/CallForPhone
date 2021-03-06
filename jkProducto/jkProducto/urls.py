from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static 
from ventas import views 
admin.site.login = login_required(admin.site.login)
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jkProducto.views.home', name='home'),

    url(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root':settings.MEDIA_ROOT,}),
    url(r'^$', 'productos.views.home', name='home'),
    #url(r'^login/$', 'productos.views.iniciarSesion', name='login'),
    #url(r'^$',algo.iniciarSesion , name='iniciarSesion'),
    url(r'^login/', views.iniciarSesion , name='iniciarSesion'),
    url(r'^logout/', views.cerrarSesion , name='cerrarSesion'),
    url(r'^ventas/', include('ventas.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^public/', include('internetWeb.urls')),


    #url(r'^admin/', include('empleados_login.urls')),
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
    url(r'^mantenimientoSucursal/historialVentas/$', 'historialVentas',name='historialVentas'), 
    #url(r'^mantenimientoSucursal/historialVentas/$', 'historialVentas',name='historialVentas'), 
    url(r'^mantenimientoSucursal/historialVentas/(?P<id>[\w-]+)/$', 'Historial_ventas_Sucursal_Admin',name='histoSucursalVentasAdm'), 
    url(r'^mantenimientoSucursal/detalle/ver/$', 'prueba',name='algo1'), 
    url(r'^export/(?P<suc_id>[0-9]+)$', 'export',name='export'), 
   # url(r'^exportVentas/(?P<suc_id>[0-9]+)$', 'export123',name='export'), 





    

 )

urlpatterns += patterns('productos.views',

    url(r'^producto/filtroproducto/$', 'filtroproductos',name='filtroproductos'),
    url(r'^producto/filtrocriterio/$', 'filtrocriterio',name='filtrocriterio'),
    




    ) 




#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


