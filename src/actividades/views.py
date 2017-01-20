from django.shortcuts import render

from django.core.urlresolvers import reverse_lazy

from .models import Actividad 


from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import( CreateView, UpdateView, DeleteView )

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from cis.models import Usuario 

class ListaActividades(ListView):
	template_name = "lista_Actividades.html"
	model = Actividad
	paginate_by = 3

	def get_context_data(self, *args, **kwargs):
		context = super(ListaActividades, self).get_context_data(*args, **kwargs)
		context["usuarios"] = Usuario.objects.all()
		return context

	
class DetalleActividad(DetailView):
	template_name = "detalle_actividad.html"
	model = Actividad


class CrearActividad(CreateView):
	template_name = "crear_actividad.html"
	model = Actividad
	success_url = reverse_lazy('actividades:list')
	fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_fin']

class ActualizarActividad(UpdateView):
	template_name = "crear_actividad.html"
	model = Actividad
	success_url = reverse_lazy('actividades:list')
	fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_fin']

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(ActualizarActividad, self).dispatch(*args, **kwargs)

class BorarActividad(DeleteView):
	template_name = "confirmar_borrar_actividad.html"
	model = Actividad
	success_url = reverse_lazy('actividades:list')

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(BorarActividad, self).dispatch(*args, **kwargs)


# # Sistema viejo
# def inicio(request):
#  	return render(request, "inicio.html", {} )



