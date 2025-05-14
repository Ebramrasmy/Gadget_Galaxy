from django.shortcuts import render, redirect
from .forms import ProductForm
# Create your views here.
from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_product')
    else:
        form = ProductForm()
    return render(request, 'product/add_product.html', {'form': form})