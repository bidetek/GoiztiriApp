from django.contrib import admin

from .models import Usuario
from .forms import UsuarioModelForm


class AdminUsuario(admin.ModelAdmin):
	list_display = ["__str__","apellidos","email","sexo","modified_at","timestamp"]
	form = UsuarioModelForm
	list_filter = ["timestamp","modified_at"]
	list_editable = ["email"]
	search_fields = ["email","nombre"]

	# class Meta:
	# 	model = Usuario 


admin.site.register(Usuario, AdminUsuario)

