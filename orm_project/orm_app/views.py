from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Perfil
from .forms import PerfilForm


def perfil_detalle(request):
    perfil = get_object_or_404(Perfil, usuario=request.user)
    return render(request, 'orm_app/perfil_detalle.html', {'perfil': perfil})

def perfil_editar(request):
    perfil = get_object_or_404(Perfil, usuario=request.user)
    if request.method == "POST":
        form = PerfilForm(request.POST, instance=perfil)
        if form.is_valid():
            perfil = form.save(commit=False)
            perfil.usuario = request.user
            perfil.save()
            return redirect('perfil_detalle')
    else:
        form = PerfilForm(instance=perfil)
    return render(request, 'orm_app/perfil_editar.html', {'form': form})

def perfil_crear(request):
    if request.method == "POST":
        form = PerfilForm(request.POST)
        if form.is_valid():
            perfil = form.save(commit=False)
            perfil.usuario = request.user
            perfil.save()
            return redirect('perfil_detalle')
    else:
        form = PerfilForm()
    return render(request, 'orm_app/perfil_crear.html', {'form': form})
