# -*- encoding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
#from django.contrib.auth import get_user_model
 
# Create your models here.

class TipoProducto(models.Model):
	nombre = models.CharField(max_length=60)
	tipo_general = (('Cel','Celular'), ('Tab','Tablets'),)
	tipo_especifico = models.CharField(max_length=10, choices=tipo_general, default='Cel')
	def __unicode__(self):
		return "  %s de %s"%(self.nombre ,self.tipo_especifico)

class Marca(models.Model):
	nombre = models.CharField(max_length=60,unique=True)
	
        def clean(self):
            self.nombre = self.nombre.capitalize()

	def __unicode__(self):
		return self.nombre
	
class ProductoAlmacen(models.Model):
	codigo = models.CharField(max_length=20)
	marca = models.ForeignKey(Marca)
	color_todos = (('Sc',''),('Az','Azul'), ('Bl','Blanco'), ('Ne','Negro'), ('Pl','Plomo'),)
	color = models.CharField(max_length=2, choices=color_todos, default='Sc')
	stock = models.PositiveSmallIntegerField(default=0)
	adicional = models.PositiveSmallIntegerField(default=0)
	mayor = models.PositiveSmallIntegerField()
	menor = models.PositiveSmallIntegerField()
	tipo_producto = models.ForeignKey(TipoProducto)
	fecha_ingreso = models.DateTimeField(auto_now=True)

        def save(self):
            self.stock += self.adicional
            self.adicional = 0
            super(ProductoAlmacen, self).save()


        def NuevoAlgo(self):
        	pass



	class Meta:
		unique_together = ('codigo', 'color',)
		
	def __unicode__(self):
		return "  %s , %s , %s, %s, %s, %s, %s"%(self.codigo ,self.marca,self.color,self.tipo_producto,self.stock,self.mayor,self.menor)

class Tienda(models.Model):
	codigo_puesto = models.CharField(max_length=20)
	nombre = models.CharField(max_length=60)
	departamento = models.CharField(max_length=60)
	ciudad = models.CharField(max_length=60)
	distrito = models.CharField(max_length=60)
	#direccion = models.CharField(max_length=60)

	def clean(self):
		self.codigo_puesto = self.codigo_puesto.capitalize()
		self.nombre = self.nombre.capitalize()

	class Meta:
		unique_together = ('codigo_puesto', 'nombre',)

	def __unicode__(self):
		return " %s de la ciudad: %s con el codigo: %s" %(self.nombre,self.ciudad,self.codigo_puesto)

class TiendaTrabajador(models.Model):
	tienda = models.ForeignKey(Tienda)
	trabajador = models.OneToOneField(User)
	fecha_ingreso = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return "%s , %s, %s" %(self.tienda,self.trabajador,self.fecha_ingreso)


#User._meta.get_field_by_name('email')[0]._unique = True
#User._meta.get_field_by_name('username')[0]._unique = True


