from django.conf.urls import url

from django.contrib.auth.decorators import login_required, permission_required


from .views import ( 
    ListaUsuarios,
    DetalleUsuario,
    CrearUsuario,
    ActualizarUsuario,
    BorarUsuario
    )

urlpatterns = [

    url(r'^$', ListaUsuarios.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', DetalleUsuario.as_view(), name='detail'),
    url(r'^nuevo$', CrearUsuario.as_view(), name='new'),
    url(r'^editar/(?P<pk>\d+)$', ActualizarUsuario.as_view(), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', BorarUsuario.as_view(), name='delete'),

    ]