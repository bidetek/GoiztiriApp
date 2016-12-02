from django.shortcuts import render

from django.core.urlresolvers import reverse_lazy

from .models import Usuario 


from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import( CreateView, UpdateView, DeleteView )

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ListaUsuarios(ListView):
	template_name = "lista_usuarios.html"
	model = Usuario
	paginate_by = 3

	# Pruebas de autenticacion 
	#
	# def get(self, request):
	# 	if request.user.is_authenticated():
	# 		print("Sí")
	# 	else:
	# 		print("Nope")
	# 	return super(ListaUsuarios, self).get(self,request)

class DetalleUsuario(DetailView):
	template_name = "detalle_usuario.html"
	model = Usuario

class CrearUsuario(CreateView):
	template_name = "alta_usuario.html"
	model = Usuario
	success_url = reverse_lazy('usuario:list')
	fields = ['nombre','apellidos','email']

class ActualizarUsuario(UpdateView):
	template_name = "alta_usuario.html"
	model = Usuario
	success_url = reverse_lazy('usuario:list')
	fields = ['nombre','apellidos','email']

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(ActualizarUsuario, self).dispatch(*args, **kwargs)

class BorarUsuario(DeleteView):
	template_name = "confirmar_borrar_usuario.html"
	model = Usuario
	success_url = reverse_lazy('usuario:list')

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(BorarUsuario, self).dispatch(*args, **kwargs)


# Sistema viejo
def inicio(request):
 	return render(request, "inicio.html", {} )


