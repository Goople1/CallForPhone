from django.contrib import admin
from models import Sucursal, SucursalTrabajador 
from actions import export_as_csv
# Register your models here.
class SucursalAdmin(admin.ModelAdmin):
	list_display = ('codigo_puesto', 'nombre', 'departamento', 'direccion')
	list_filter = ('codigo_puesto', 'departamento','nombre',)
	search_fields = ('codigo_puesto', 'departamento')
	list_editable = ('codigo_puesto', 'departamento')

class SucursalTrabajadorAdmin(admin.ModelAdmin):
	list_display = ('sucursal','trabajador','fecha_ingreso',)
	list_filter = ('sucursal',)
	search_fields = ('sucursal',)
	list_editable = ('sucursal',)


admin.site.register(Sucursal, SucursalAdmin)
admin.site.register(SucursalTrabajador, SucursalTrabajadorAdmin)
