from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductoListView.as_view(), name='producto_lista'),
    path('productos/<int:pk>/', views.ProductoDetailView.as_view(), name='producto_detalle'),
    path('productos/crear/', views.producto_crear, name='producto_crear'),
    path('productos/<int:pk>/editar/', views.producto_editar, name='producto_editar'),
]
