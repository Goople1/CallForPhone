from django.db import models
from sucursales.models import Cliente , SucursalTrabajador as Empleado
from productos.models import ProductoAlmacen as Producto
# Create your models here.

#Boletao/Factura
class Venta(models.Model):

	cliente  = models.ForeignKey(Cliente)
	empleado = models.ForeignKey(Empleado)
	fecha_emision = models.DateTimeField(auto_now=True)
	igv = models.FloatField()
	subtotal = models.FloatField()
	total  = models.FloatField()

	def __unicode__(self):
		pass



class DetalleVenta(models.Model):

	referencia_venta = models.ForeignKey(Venta)
	referecia_producto =models.ForeignKey(Producto)
	cantidad = models.PositiveIntegerField()
	precio = models.FloatField()

	def __unicode__(self):
		pass



