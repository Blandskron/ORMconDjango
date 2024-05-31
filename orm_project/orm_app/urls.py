from django.urls import path
from . import views

urlpatterns = [
    # URLs para vistas de etiquetas
    path('etiquetas/', views.EtiquetaListView.as_view(), name='etiqueta_lista'),
    path('etiquetas/<int:pk>/', views.EtiquetaDetailView.as_view(), name='etiqueta_detalle'),
    path('etiquetas/crear/', views.etiqueta_crear, name='etiqueta_crear'),
    path('etiquetas/<int:pk>/editar/', views.etiqueta_editar, name='etiqueta_editar'),

    # URLs para vistas de perfil
    path('perfil/', views.perfil_detalle, name='perfil_detalle'),
    path('perfil/editar/', views.perfil_editar, name='perfil_editar'),
    path('perfil/crear/', views.perfil_crear, name='perfil_crear'),
]
