from django.shortcuts import render

from django.core.urlresolvers import reverse_lazy

from .models import Usuario 


from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import( CreateView, UpdateView, DeleteView ) 

class ListaUsuarios(ListView):
	template_name = "lista_usuarios.html"
	model = Usuario
	paginate_by = 3

class DetalleUsuario(DetailView):
	template_name = "detalle_usuario.html"
	model = Usuario

class CrearUsuario(CreateView):
	template_name = "alta_usuario.html"
	model = Usuario
	success_url = reverse_lazy('usuario:list')
	fields = ['nombre','apellidos','email']

class ActualizarUsuario(UpdateView):
	model = Usuario
	success_url = reverse_lazy('usuario:list')
	fields = ['nombre','apellidos','email']

class BorarUsuario(DeleteView):
	template_name = "confirmar_borrar_usuario.html"
	model = Usuario
	success_url = reverse_lazy('usuario:list')


# Sistema viejo
def inicio(request):
 	return render(request, "inicio.html", {} )


