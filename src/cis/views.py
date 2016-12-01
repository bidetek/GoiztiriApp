from django.shortcuts import render

from django.core.urlresolvers import reverse_lazy

from .forms import RegForm, UsuarioModelForm
from .models import Usuario 


from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import( CreateView, UpdateView, DeleteView ) 

class ListaUsuarios(ListView):
	model = Usuario

class DetalleUsuario(DetailView):
	model = Usuario

class CrearUsuario(CreateView):
	model = Usuario
	success_url = reverse_lazy('usuario:list')
	fields = ['nombre','apellidos','email']

class ActualizarUsuario(UpdateView):
	model = Usuario
	success_url = reverse_lazy('usuario:list')
	fields = ['nombre','apellidos','email']

class BorarUsuario(DeleteView):
	model = Usuario
	success_url = reverse_lazy('usuario:list')


# Sistema viejo
def inicio(request):
 	return render(request, "inicio.html", {} )


