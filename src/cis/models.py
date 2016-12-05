from django.db import models

# Algunas variables de estados 

VARON = "V" 
MUJER =	"M"

GENERO = (
	(VARON, "Hombre"),
	(MUJER, "Mujer"),
)


class Usuario(models.Model):
	nombre = models.CharField(max_length=100, blank=False, null=False)
	apellidos = models.CharField(max_length=100, blank=True, null=True)
	email = models.EmailField()
	sexo = models.CharField(max_length=1, choices=GENERO, default="M")

	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	modified_at = models.DateTimeField(auto_now=True)

	def __unicode__(self): # Python 2 
		return(self.nombre)

	def __str__(self): # Python 3
		return(self.nombre)

