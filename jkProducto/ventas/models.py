from django.db import models
from sucursales.models import  SucursalTrabajador
from sucursales.models import Sucursal,DetalleSucursalAlmacen
# Create your models here.

#Boletao/Factura
class Venta(models.Model):

	#cliente  = models.ForeignKey(Cliente)
	empleado = models.ForeignKey(SucursalTrabajador)
	sucursal = models.ForeignKey(Sucursal)	
	fecha_emision = models.DateTimeField(auto_now=True, editable=False)
	# igv = models.FloatField()
	# subtotal = models.FloatField()
	estado = models.BooleanField(default=True)
	total  = models.FloatField( blank=True , default=0.0)

	def __unicode__(self):
		pass
	

class DetalleVenta(models.Model):
	
	venta_id = models.ForeignKey(Venta)
	detalle_Sucursal_almacen_id=models.ForeignKey(DetalleSucursalAlmacen)
	tipo_precio = models.CharField(max_length=20)
	cantidad = models.PositiveIntegerField()
	precio_real = models.FloatField()
	precio = models.FloatField()
	descripcion = models.CharField(max_length=50 ,blank=True)
	importe = models.FloatField(default=0.0)

	def __unicode__(self):
		pass
	
	


