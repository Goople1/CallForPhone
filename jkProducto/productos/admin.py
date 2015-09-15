from django.contrib import admin
from models import TipoProducto, ProductoAlmacen, Marca, Tienda, TiendaTrabajador
from actions import export_as_csv

class TipoProductoAdmin(admin.ModelAdmin):
	list_display = ('tipo_especifico','nombre',)
	list_filter  = ('tipo_especifico','nombre',)
	search_fields = ('tipo_especifico','nombre',)


class ProductoAdmin(admin.ModelAdmin):
	list_display = ('codigo','marca','tipo_producto','color','stock','adicional','mayor','menor','fecha_ingreso',)
	#field_options = {'fields': (('stock', 'adicional')),}
	list_filter = ('codigo','tipo_producto__nombre','tipo_producto__tipo_especifico','marca',)
	search_fields = ('codigo','tipo_producto__nombre','tipo_producto__tipo_especifico','marca',)
	list_editable =('adicional',)
	actions = [export_as_csv]

class TiendaAdmin(admin.ModelAdmin):
	list_display = ('codigo_puesto','nombre','departamento','ciudad','distrito',)

class TiendaTrabajadorAdmin(admin.ModelAdmin):
	list_display = ('tienda','trabajador','fecha_ingreso',)

# Register your models here.
admin.site.register(TipoProducto,TipoProductoAdmin)
admin.site.register(Marca)
admin.site.register(Tienda,TiendaAdmin)
admin.site.register(TiendaTrabajador,TiendaTrabajadorAdmin)
admin.site.register(ProductoAlmacen,ProductoAdmin)



