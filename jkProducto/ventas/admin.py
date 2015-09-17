from django.contrib import admin
from ventas.models import Venta,DetalleVenta

# Register your models here.
class VentasAdmin(admin.ModelAdmin):
	list_display = ("cliente","empleado", 'fecha_emision','igv','subtotal','total',)

class DetalleVentaAdmi(admin.ModelAdmin):
	list_display = 	('referencia_venta', 'referecia_producto','cantidad','precio',)




admin.site.register(Venta, VentasAdmin)
admin.site.register(DetalleVenta , DetalleVentaAdmi)