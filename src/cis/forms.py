from django import forms

from .models import Usuario 

class UsuarioModelForm(forms.ModelForm):
	class Meta:
		model = Usuario
		fields = ["nombre","apellidos","email"]

class RegForm(forms.Form):
	nombre = forms.CharField(max_length=100)
	apellidos = forms.CharField(max_length=100)
	email = forms.EmailField()