from django.shortcuts import render, redirect ,get_object_or_404
from .models import Product, Category
from django.core.exceptions import ValidationError

def product_list(request):
    products = Product.objects.filter(is_deleted=False)
    return render(request, 'product/product_list.html', {'products': products})

def product_new(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        sku = request.POST.get('sku')
        image = request.FILES.get('image')
        category_id = request.POST.get('category')

        errormsg = None

        if not all([name, description, price, stock, sku, category_id]):
            errormsg = "Please fill all required fields."
        else:
            try:
                price = float(price)
                stock = int(stock)
            except ValueError:
                errormsg = "Price must be a number and Stock must be an integer."

            if not errormsg:
                try:
                    category = Category.objects.get(id=category_id)
                    product = Product(
                        name=name,
                        description=description,
                        price=price,
                        stock=stock,
                        sku=sku,
                        image=image,
                        category=category
                    )
                    product.full_clean()
                    product.save()
                    return redirect('product:product_list')
                except Category.DoesNotExist:
                    errormsg = "Selected category does not exist."
                except ValidationError as e:
                    errormsg = e.messages

        return render(request, 'product/new.html', {'errormsg': errormsg, 'categories': categories})

    return render(request, 'product/new.html', {'categories': categories})

def product_update(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    categories = Category.objects.all()
    errormsg = None

    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        sku = request.POST.get('sku')
        image = request.FILES.get('image')
        category_id = request.POST.get('category')

        if not all([name, description, price, stock, sku, category_id]):
            errormsg = "Please fill all required fields."
        else:
            try:
                price = float(price)
                stock = int(stock)
            except ValueError:
                errormsg = "Price must be a number and Stock must be an integer."

            if not errormsg:
                try:
                    category = Category.objects.get(id=category_id)
                    product.name = name
                    product.description = description
                    product.price = price
                    product.stock = stock
                    product.sku = sku
                    product.category = category

                    if image:
                        product.image = image

                    product.full_clean()
                    product.save()
                    return redirect('product:product_list')
                except Category.DoesNotExist:
                    errormsg = "Selected category does not exist."
                except ValidationError as e:
                    errormsg = e.messages

    context = {
        'categories': categories,
        'product': product,
        'errormsg': errormsg,
        'is_update': True,
    }
    return render(request, 'product/new.html', context)

def product_soft_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.is_deleted = True
    product.save()
    return redirect('product:product_list')

def product_hard_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('product:product_list')

def deleted_products(request):
    deleted = Product.objects.filter(is_deleted=True)
    return render(request, 'product/deleted_list.html', {'products': deleted})


def product_restore(request, pk):
    product = get_object_or_404(Product, pk=pk, is_deleted=True)
    product.is_deleted = False
    product.save()
    return redirect('product:deleted_products')
