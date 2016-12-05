from django.shortcuts import render

from django.core.urlresolvers import reverse_lazy

from .models import Actividad 


from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import( CreateView, UpdateView, DeleteView )

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ListaActividades(ListView):
	template_name = "lista_Actividades.html"
	model = Actividad
	paginate_by = 3

	
class DetalleActividad(DetailView):
	template_name = "detalle_actividad.html"
	model = Actividad


class CrearActividad(CreateView):
	template_name = "crear_actividad.html"
	model = Actividad
	success_url = reverse_lazy('Actividad:list')
	fields = ['nombre','apellidos','email','sexo']

class ActualizarActividad(UpdateView):
	template_name = "crear_actividad.html"
	model = Actividad
	success_url = reverse_lazy('Actividad:list')
	fields = ['nombre','apellidos','email','sexo']

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(ActualizarActividad, self).dispatch(*args, **kwargs)

class BorarActividad(DeleteView):
	template_name = "confirmar_borrar_actividad.html"
	model = Actividad
	success_url = reverse_lazy('Actividad:list')

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(BorarActividad, self).dispatch(*args, **kwargs)


# Sistema viejo
def inicio(request):
 	return render(request, "inicio.html", {} )



