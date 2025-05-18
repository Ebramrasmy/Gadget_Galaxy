from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from django.core.exceptions import ValidationError

def product_list(request):
    products = Product.getall()
    return render(request, 'product/product_list.html', {'products': products})

def product_new(request):
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
                    product = Product.Add(
                        name=name,
                        description=description,
                        price=price,
                        stock=stock,
                        sku=sku,
                        image=image,
                        category=category
                    )
                    return Product.go_to_product_list()
                except Category.DoesNotExist:
                    errormsg = "Selected category does not exist."
                except ValidationError as e:
                    errormsg = e.messages

    return render(request, 'product/new.html', {'categories': categories, 'errormsg': errormsg})

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
                    Product.update(
                        id=product_id,
                        name=name,
                        description=description,
                        price=price,
                        stock=stock,
                        sku=sku,
                        image=image,
                        category=category
                    )
                    return Product.go_to_product_list()
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
    Product.softdelete(product_id)
    return Product.go_to_product_list()

def product_hard_delete(request, product_id):
    Product.harddel(product_id)
    return Product.go_to_product_list()

def deleted_products(request):
    deleted = Product.objects.filter(is_deleted=True)
    return render(request, 'product/deleted_list.html', {'products': deleted})

def product_restore(request, pk):
    product = get_object_or_404(Product, pk=pk, is_deleted=True)
    product.is_deleted = False
    product.save()
    return Product.go_to_product_list()

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id, is_deleted=False)
    return render(request, 'product/product_detail.html', {'product': product})



#######################insert using model form######################
def product_createf(request):
    context={'form':ProductForm()}
    if(request.method=='POST'):
        form=ProductForm(data=request.POST,files=request.FILES)
        if form.is_bound and form.is_valid():
            form.save()
            return redirect('product:product_list')
        else:
            context['msg']=form.errors
            context['form']=form

    return render(request, 'product/product_form.html', context)



#######################update using form######################

from .forms import ProductForm

def product_updatef(request, id):
    old_product = Product.objects.get(pk=id)
    initial_data = {
        'name': old_product.name,
        'price': old_product.price,
        'description': old_product.description,
        'image': old_product.image,
        'category': old_product.category.id
    }

    context = {'form': ProductForm(initial=initial_data)}

    if request.method == 'POST':
        form = ProductForm(data=request.POST, files=request.FILES, initial=initial_data)
        if form.is_valid():
            old_product.name = form.cleaned_data['name']
            old_product.price = form.cleaned_data['price']
            old_product.description = form.cleaned_data['description']
            old_product.image = form.cleaned_data['image']
            old_product.category = form.cleaned_data['category']
            old_product.save()
            return redirect('product:product_list')
        else:
            context['msg'] = form.errors

    return render(request, 'product/product_updateform.html', context)



