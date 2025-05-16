from django.shortcuts import render, redirect, get_object_or_404
from .models import Category

def category_list(request):
    categories = Category.getall()
    return render(request, 'category/category_list.html', {'categories': categories})

def category_new(request):
    errormsg = None
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')

        if not name:
            errormsg = "Name is required."
        else:
            Category.Add(name=name, description=description)
            return redirect('category:category_list')

    return render(request, 'category/new.html', {'errormsg': errormsg})

def category_update(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    errormsg = None

    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')

        if not name:
            errormsg = "Name is required."
        else:
            Category.update(id=category.id, name=name, description=description)
            return redirect('category:category_list')

    return render(request, 'category/new.html', {'category': category, 'is_update': True, 'errormsg': errormsg})

def category_soft_delete(request, category_id):
    Category.softdelete(category_id)
    return redirect('category:category_list')

def category_hard_delete(request, category_id):
    Category.harddelete(category_id)
    return redirect('category:category_list')

def deleted_categories(request):
    deleted = Category.objects.filter(is_deleted=True)
    return render(request, 'category/deleted_list.html', {'categories': deleted})

def category_restore(request, category_id):
    category = get_object_or_404(Category, id=category_id, is_deleted=True)
    category.is_deleted = False
    category.save()
    return redirect('category:deleted_categories')
