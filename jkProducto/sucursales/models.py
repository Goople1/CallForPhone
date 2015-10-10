from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from datetime import date
# Create your models here.
class Almacen(models.Model):
	nombreEmpresa = models.CharField(max_length=80)
	ruc = models.CharField(unique=True, max_length = 8 ,validators=[ RegexValidator(regex = '\d{11}', message="Ruc no tiene 11 digitos", code="invalido")])
	todos_departamento = (('Ama','Amazonas'), ('Anc','Ancash'),('Apu','Apurimac'),('Are','Arequipa'),('Aya','Ayacucho'),('Caj','Cajamarca'),('Cal','Callao'),('Cuz','Cuzco'),('Hua','Huancavelica'),('Hun','Huanuco'),('Ica','Ica'),('Jun','Junin'),('Lal','La Libertad'),('Lam','Lambayeque'),('Lim','Lima'),('Lor','Loreto'),('Mad','Madre de Dios'),('Moq','Moquegua'),('Pas','Pasco'),('Piu','Piura'),('Pun','Puno'),('San','San Martin'),('Piu','Piura'),('Tac','Tacna'),('Tum','Tumbes'),('Uca','Ucayali'),)
	departamento = models.CharField(max_length=20, choices=todos_departamento, default='Lim')
	fecha_registro = models.DateTimeField(auto_now=True)
	descripcion = models.CharField(max_length=400)
	def clean(self):
		self.nombre = self.nombre.capitalize()

class EstadoSucursal(models.Model):
	nombre_estado = models.CharField(max_length=60)
	def clean(self):
		self.nombre_estado = self.nombre_estado
		
class Sucursal(models.Model):
	id_almacen = models.ForeignKey(Almacen)
	codigo_puesto = models.CharField(max_length=20)
	nombre = models.CharField(max_length=60)
	descripcion = models.CharField(max_length=400)
	fecha_registro = models.DateTimeField(auto_now=True)
	todos_departamento = (('Ama','Amazonas'), ('Anc','Ancash'),('Apu','Apurimac'),('Are','Arequipa'),('Aya','Ayacucho'),('Caj','Cajamarca'),('Cal','Callao'),('Cuz','Cuzco'),('Hua','Huancavelica'),('Hun','Huanuco'),('Ica','Ica'),('Jun','Junin'),('Lal','La Libertad'),('Lam','Lambayeque'),('Lim','Lima'),('Lor','Loreto'),('Mad','Madre de Dios'),('Moq','Moquegua'),('Pas','Pasco'),('Piu','Piura'),('Pun','Puno'),('San','San Martin'),('Piu','Piura'),('Tac','Tacna'),('Tum','Tumbes'),('Uca','Ucayali'),)
	departamento = models.CharField(max_length=20, choices=todos_departamento, default='Lim')
	id_estadoSucursal = models.ForeignKey(EstadoSucursal)

	def clean(self):
		self.codigo_puesto = self.codigo_puesto.capitalize()
		self.nombre = self.nombre.capitalize()
	class Meta:
		unique_together = ('codigo_puesto', 'departamento',)

	def __unicode__(self):
		return " %s de la ciudad: %s con el codigo: %s" %(self.nombre,self.departamento,self.codigo_puesto)


#Se Registra cuando se cambia de estado la sucursal
class HistorialSucursal(models.Model):
	fecha = models.DateTimeField(auto_now=True)
	id_sucursal = models.ForeignKey(Sucursal)

class SucursalTrabajador(models.Model):
	sucursal = models.ForeignKey(Sucursal)
	trabajador = models.OneToOneField(User)
	fecha_ingreso = models.DateTimeField(auto_now=True)
	todos_cargo= (("admi","Administrador"),("empl" ,"Empleado"),	 )
	cargo = models.CharField(max_length=20 , choices= todos_cargo ,  default="empl")
	dni = models.CharField(max_length=8, unique=True)
	fecha_nacimiento = models.DateField(blank=True , null=True,default=date(1990,01,01))
	sexo = models.CharField( max_length =1, choices= (("m","Masculino") , ("f","Femenino")) , default="m")

	def __unicode__(self):
		return " Trabjador: %s , %s, %s" %(self.trabajador,self.fecha_ingreso ,self.sucursal,)

#Modelo Cliente  , no deberia estar  aqui pero por el momento
class Cliente(models.Model):
	razon_social = models.CharField(max_length=50 , blank=True);
	nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	telefono = models.CharField(max_length=10)
	dni = models.CharField(unique=True, max_length = 8 ,validators=[ RegexValidator(regex = '\d{8}', message="DNI no tiene 8 digitos", code="invalido")])
	direccion = models.CharField(max_length=50 , blank=True)	
	ruc = models.CharField(max_length=11 , blank=True)
	correo = models.EmailField(blank=True)


	def __unicode__(self):
		return "Cliente : [%s] %s %s " %(self.razon_social,self.nombre , self.apellidos)






    