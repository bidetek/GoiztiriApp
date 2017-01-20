from django.db import models

from cis.models import Usuario

# Create your models here.

class Actividad(models.Model):
	"""
		Las actividades.
	"""
	nombre = models.CharField(max_length=100, blank=False, null=False)
	descripcion = models.TextField()
	fecha_inicio = models.DateField()
	fecha_fin = models.DateField()

	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	modified_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "Actividad"
		verbose_name_plural = "Actividades"
	
	def __unicode__(self): # Python 2 
		return(self.nombre)

	def __str__(self): # Python 3
		return(self.nombre)

class Participante(models.Model):
	"""
		Lista de subscritos.
	""" 
	actividad = models.ManyToManyField(Actividad)
	usuario = models.ManyToManyField(Usuario)

	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

	verbose_name_plural = "participantes"

	def __unicode__(self): # Python 2 
		return(self.pk)

	def __str__(self): # Python 3
		return(self.pk)



class Asistencia(models.Model): 
	"""
		Tabla de asistencias. 
	"""
	actividad = models.ManyToManyField(Actividad)
	usuario = models.ManyToManyField(Participante)

	fecha_actividad = models.DateTimeField()
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	modified_at = models.DateTimeField(auto_now=True)

	def __unicode__(self): # Python 2 
		return(self.pk)

	def __str__(self): # Python 3
		return(self.pk)


