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
#todos los campos de Evento
    class Meta:
        model = Venta
        fields = ('Cliente', 'numeroVenta', 'fecha', 'detalleVenta')
        def __init__ (self, *args, **kwargs):
            super(VentaForm, self).__init__(*args, **kwargs)
            self.fields["detalleVenta"].widget = forms.widgets.CheckboxSelectMultiple()
            self.fields["detalleVenta"].help_text = "Ingrese los actores que asistiran al evento"
            self.fields["detalleVenta"].queryset = Carro.objects.all()
