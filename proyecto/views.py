
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import CarroForm
from proyecto.models import Marca, Cliente, Carro, Venta
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def post_list(request):
    return render(request, 'blog/post_list.html', {})

@login_required

def listar_vehiculo(request):
    carro = Carro.objects.all()
    return render(request, 'blog/listarvehiculos.html', {'carro': carro})

def crear_vehiculo(request):
    if request.method == "POST":
        form = CarroForm(request.POST)
        if form.is_valid():
            carro = form.save(commit=False)
            carro.save()
            return redirect('listar_vehiculo')
    else:
        form = CarroForm()
        return render(request, 'blog/carro_new.html', {'form': form})

def vehiculo_detail(request, pk):
    carro = get_object_or_404(Carro, pk=pk)
    return render(request, 'blog/datelle_vehiculo.html', {'carro': carro})

def vehiculos_edit(request, pk):
    carro = get_object_or_404(Carro, pk=pk)
    if request.method == "POST":
        form = CarroForm(request.POST, instance=carro)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('vehiculo_detail', pk=post.pk)
    else:
        form = CarroForm(instance=carro)
    return render(request, 'blog/carro_new.html', {'form': form})

def vehiculos_remove(request, pk):
    carro = get_object_or_404(Carro, pk=pk)
    carro.delete()
    return redirect('listar_vehiculo')
