from django import forms
from .models import Marca, Cliente, Carro, Venta

class CarroForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = ('Marca', 'anio', 'linea', 'precio')

        
