from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

def lista_productos(request):
    if Producto.objects.count() == 0:
        Producto(nombre="Producto demo", descripcion="Creado automáticamente", precio=1000, caracteristicas=["ejemplo", "demo"]).save()
    productos = Producto.objects.all()
    return render(request, 'productos/lista.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            caracteristicas = [c.strip() for c in data['caracteristicas'].split(',') if c.strip()]
            producto = Producto(
                nombre=data['nombre'],
                descripcion=data['descripcion'],
                precio=data['precio'],
                caracteristicas=caracteristicas
            )
            producto.save()
            return redirect('lista')
    else:
        form = ProductoForm()
    return render(request, 'productos/formulario.html', {'form': form})

def editar_producto(request, producto_id):
    producto = Producto.objects(id=producto_id).first()
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            producto.nombre = data['nombre']
            producto.descripcion = data['descripcion']
            producto.precio = data['precio']
            producto.caracteristicas = [c.strip() for c in data['caracteristicas'].split(',') if c.strip()]
            producto.save()
            return redirect('lista')
    else:
        form = ProductoForm(initial={
            'nombre': producto.nombre,
            'descripcion': producto.descripcion,
            'precio': producto.precio,
            'caracteristicas': ', '.join(producto.caracteristicas)
        })
    return render(request, 'productos/formulario.html', {'form': form})

def eliminar_producto(request, producto_id):
    producto = Producto.objects(id=producto_id).first()
    producto.delete()
    return redirect('lista')
