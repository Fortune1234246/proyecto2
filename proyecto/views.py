
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import CarroForm, MarcaForm, VentaForm
from proyecto.models import Marca, Cliente, Carro, Venta
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

#STYLE AND CSS
def post_list(request):
    return render(request, 'blog/post_list.html', {})


#Vehiculos
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


#MARCAAAAAAAAAAAAAAAAAAAAAAAAAS
def listar_marcas(request):
    marca = Marca.objects.all()
    return render(request, 'blog/listarmarcas.html', {'marca': marca})

def crear_marca(request):
    if request.method == "POST":
        form = MarcaForm(request.POST)
        if form.is_valid():
            marca = form.save(commit=False)
            marca.save()
            return redirect('listar_marcas')
    else:
        form = MarcaForm()
        return render(request, 'blog/marca_new.html', {'form': form})

def marcas_detail(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    return render(request, 'blog/detelle_marca.html', {'marca': marca})


#Ventaaaaaaaaaaaaaaaaaaaaaaaaaaaaas
def listar_ventas(request):
    venta = Venta.objects.all()
    return render(request, 'blog/listarventa.html', {'venta': venta})

def ventas_new(request):
    if request.method == "POST":
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = Venta.objects.create(nombre=form.cleaned_data['nombre'], descripcion=form.cleaned_data['descripcion'], album=form.cleaned_data['album'], artista=form.cleaned_data['artista'])
            post = form.save(commit=False)
            post.save()
            return redirect('listar_ventas', pk=post.pk)
    else:
        form = VentaForm()
        return render(request, 'blog/listarventa.html', {'form': form})
