from django.db import models
from django.contrib.auth.models import User
from productoapp.models import Producto


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=100)
    productos = models.ManyToManyField(Producto)
    
    def __str__(self):
        return self.nombre

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre_completo = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    
    def __str__(self):
        return self.usuario.username
    