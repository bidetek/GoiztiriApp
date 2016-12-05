from django.conf.urls import url

from django.contrib.auth.decorators import login_required, permission_required

from .views import ( 
    ListaActividades,
    DetalleActividad,
    CrearActividad,
    ActualizarActividad,
    BorarActividad
    )

urlpatterns = [

    url(r'^$', ListaActividades.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', DetalleActividad.as_view(), name='detail'),
    url(r'^nuevo$', CrearActividad.as_view(), name='new'),
    url(r'^editar/(?P<pk>\d+)$', ActualizarActividad.as_view(), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', BorarActividad.as_view(), name='delete'),

    ]