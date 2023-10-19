from django import forms
from .models import Usuario

class RegistroUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['Nombre', 'Edad', 'Genero', 'Preferencias_Contenido', 'Correo_Electronico', 'Password']
