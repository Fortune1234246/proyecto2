from django import forms
from .models import Marca, Cliente, Carro, Venta

class CarroForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = ('Marca', 'anio', 'linea', 'precio')

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ('nombre', 'anio_fundacion', 'capital')

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ('Cliente', 'numeroVenta', 'fecha', 'detalleVenta')
