from django import forms
from .models import Perfil, Etiqueta


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = '__all__'

class EtiquetaForm(forms.ModelForm):
    class Meta:
        model = Etiqueta
        fields = '__all__'
