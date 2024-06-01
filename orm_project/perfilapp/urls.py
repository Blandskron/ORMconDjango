from django.urls import path
from . import views

urlpatterns = [
    path('', views.perfil_detalle, name='perfil_detalle'),
    path('perfil/editar/', views.perfil_editar, name='perfil_editar'),
    path('perfil/crear/', views.perfil_crear, name='perfil_crear'),
]
