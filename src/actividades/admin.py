from django.contrib import admin


from .models import Actividad 

# Register your models here.

class AdminActividad(admin.ModelAdmin):
	list_display = ["__str__","modified_at","created_at"]
	#form = ActividadModelForm
	list_filter = ["created_at","modified_at"]
	# list_editable = ["email"]
	# search_fields = ["email","nombre"]

	# class Meta:
	# 	model = Usuario
	verbose_name_plural = "Actividades"


admin.site.register(Actividad, AdminActividad)

