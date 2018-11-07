from django.contrib import admin
from proyecto.models import Marca, Cliente, Carro, CarroAdmin, Venta, VentaAdmin

admin.site.register(Marca)
admin.site.register(Cliente)
admin.site.register(Carro, CarroAdmin)
admin.site.register(Venta, VentaAdmin)
