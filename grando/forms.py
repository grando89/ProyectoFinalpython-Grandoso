from django import forms
from .models import Cursos , Alumnos , Profesores

class CursoFormulario(forms.ModelForm):
    class Meta:
        model = Cursos
        fields = ['nombre', 'camada',]
        

class AlumnoFormulario(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = ['nombre', 'apellido', 'email']

class ProfesorFormulario(forms.ModelForm):
    class Meta:
        model = Profesores
        fields = ['nombre', 'apellido', 'email']
        