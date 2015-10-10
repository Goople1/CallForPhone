from django.contrib import admin
from models import Sucursal, SucursalTrabajador ,Cliente, DetalleAlmacen,Almacen,EstadoSucursal
from productos.models import Producto, Marca, TipoProducto
from actions import export_as_csv
# Register your models here.
class DetalleAlmacenAdmin(admin.ModelAdmin):
	list_display = ('producto_id','stock','adicional_stock','precio_x_mayor','precio_x_menor','fecha_ingreso',)
	#field_options = {'fields': (('stock', 'adicional')),}
	list_filter = ('producto_id',)
	search_fields = ('producto_id__tipo_producto__nombre','producto_id',)
	list_editable =('adicional_stock',)
	actions = [export_as_csv]

class SucursalAdmin(admin.ModelAdmin):
	list_display = ('codigo_puesto', 'nombre', 'departamento', )
	list_filter = ('codigo_puesto', 'departamento','nombre',)
	search_fields = ('codigo_puesto', 'departamento')
	list_editable = ('codigo_puesto', 'departamento')

class SucursalTrabajadorAdmin(admin.ModelAdmin):
	list_display = ('sucursal','trabajador','fecha_ingreso',)
	list_filter = ('sucursal',)
	search_fields = ('sucursal',)
	list_editable = ('sucursal',)

class ClienteAdmin(admin.ModelAdmin):
	list_display = ('nombre','apellidos','telefono','dni','ruc' ,'correo' , 'direccion')

class AlmacenAdmin(admin.ModelAdmin):
	list_display = ('nombre_empresa','ruc','departamento','fecha_registro', 'descripcion','telefono','celular',)
	list_editable = ('nombre_empresa','ruc','departamento','descripcion','telefono','celular',)

#list_display = ('codigo','marca','tipo_producto','color','stock','adicional','mayor','menor','fecha_ingreso',)

admin.site.register(EstadoSucursal)
admin.site.register(Almacen, AlmacenAdmin)
admin.site.register(DetalleAlmacen,DetalleAlmacenAdmin)
admin.site.register(Sucursal, SucursalAdmin)
admin.site.register(SucursalTrabajador, SucursalTrabajadorAdmin)
admin.site.register(Cliente, ClienteAdmin)
