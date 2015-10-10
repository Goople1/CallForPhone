# -*- encoding:utf-8 -*-
from django.db import models
#from django.contrib.auth.models import User
from django.conf import settings
#from django.contrib.auth import get_user_model

# Create your models here.

class TipoProducto(models.Model):
    nombre = models.CharField(max_length=60,unique=True)
#tipo_general = (('Cel','Celular'), ('Tab','Tablets'),)
#tipo_especifico = models.CharField(max_length=10, choices=tipo_general, default='Cel')
    class Meta:
		verbose_name_plural = "Tipos de Productos"
    def clean(self):
        self.nombre = self.nombre.capitalize()
    def __str__(self):
    	return self.nombre


class Marca(models.Model):
    nombre = models.CharField(max_length=60,unique=True)	
    def clean(self):
        self.nombre = self.nombre.capitalize()
    def __str__(self):
        return self.nombre


class Producto(models.Model):
	codigo = models.CharField(max_length=20)
	color_todos = (('Sc',''),('Az','Azul'), ('Bl','Blanco'), ('Ne','Negro'),('Ot','Otro'), ('Pl','Plomo'),)
	color = models.CharField(max_length=2, choices=color_todos, default='Ot')	
	marca = models.ForeignKey(Marca)
	tipo_producto = models.ForeignKey(TipoProducto)
	class Meta:
		verbose_name_plural = "Mantenimiento de Productos"
		unique_together = ('codigo', 'color','marca','tipo_producto')

"""
class ProductoAlmacen(models.Model):
	codigo =
	
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

"""




#User._meta.get_field_by_name('email')[0]._unique = True
#User._meta.get_field_by_name('username')[0]._unique = True


