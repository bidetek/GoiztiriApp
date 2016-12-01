from django.db import models

class Usuario(models.Model):
	nombre = models.CharField(max_length=100, blank=False, null=False)
	apellidos = models.CharField(max_length=100, blank=True, null=True)
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self): # Python 2 
		return(self.nombre)

	def __str__(self): # Python 3
		return(self.nombre)
