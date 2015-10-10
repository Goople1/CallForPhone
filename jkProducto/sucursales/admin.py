from django.contrib import admin
from models import Sucursal, SucursalTrabajador ,Cliente
from actions import export_as_csv
# Register your models here.
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


admin.site.register(Sucursal, SucursalAdmin)
admin.site.register(SucursalTrabajador, SucursalTrabajadorAdmin)
admin.site.register(Cliente, ClienteAdmin)
