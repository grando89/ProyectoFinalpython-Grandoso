from django import forms
from .models import Bebida_blanca , Vinos , Bebida_sa
from django.contrib.auth.forms import UserCreationForm

class Bebida_Blanca_Formulario(forms.ModelForm):
    class Meta:
        model = Bebida_blanca
        fields = ['nombre', 'cantidad',]
        

class VinoFormulario(forms.ModelForm):
    class Meta:
        model = Vinos
        fields = ['nombre', 'cantidad', ]

class Bebida_Sa_Formulario(forms.ModelForm):
    class Meta:
        model = Bebida_sa
        fields = ['nombre', 'cantidad', ]
        

     