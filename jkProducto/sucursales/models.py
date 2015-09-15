from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Sucursal(models.Model):
	codigo_puesto = models.CharField(max_length=20)
	nombre = models.CharField(max_length=60)
	direccion = models.CharField(max_length=120)
	todos_departamento = (('Ama','Amazonas'), ('Anc','Ancash'),('Apu','Apurimac'),('Are','Arequipa'),('Aya','Ayacucho'),('Caj','Cajamarca'),('Cal','Callao'),('Cuz','Cuzco'),('Hua','Huancavelica'),('Hun','Huanuco'),('Ica','Ica'),('Jun','Junin'),('Lal','La Libertad'),('Lam','Lambayeque'),('Lim','Lima'),('Lor','Loreto'),('Mad','Madre de Dios'),('Moq','Moquegua'),('Pas','Pasco'),('Piu','Piura'),('Pun','Puno'),('San','San Martin'),('Piu','Piura'),('Tac','Tacna'),('Tum','Tumbes'),('Uca','Ucayali'),)
	departamento = models.CharField(max_length=20, choices=todos_departamento, default='Lim')
	def clean(self):
		self.codigo_puesto = self.codigo_puesto.capitalize()
		self.nombre = self.nombre.capitalize()

	class Meta:
		unique_together = ('codigo_puesto', 'departamento',)

	def __unicode__(self):
		return " %s de la ciudad: %s con el codigo: %s" %(self.nombre,self.departamento,self.codigo_puesto)

class SucursalTrabajador(models.Model):
	sucursal = models.ForeignKey(Sucursal)
	trabajador = models.OneToOneField(User)
	fecha_ingreso = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return "%s , %s, %s" %(self.sucursal,self.trabajador,self.fecha_ingreso)