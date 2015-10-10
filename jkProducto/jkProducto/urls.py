from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jkProducto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'productos.views.home', name='home'),
    url(r'^login/$', 'productos.views.iniciarSesion', name='login'),
    url(r'^sucursales/$', 'sucursales.views.listarSucusarles', name='sucursales'),
    url(r'^admin/', include(admin.site.urls)),
)
