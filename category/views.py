from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from django.views.generic import ListView,UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy

class CategoryListView(ListView):
    model = Category
    template_name = 'category/category_list.html'
    context_object_name = 'categories'


class CategoryCreateView(CreateView):
    model = Category
    fields = ['name', 'description']
    template_name = 'category/new.html'
    success_url = reverse_lazy('category:category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name', 'description']
    template_name = 'category/category_form.html'
    success_url = reverse_lazy('category:category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category/category_confirm_delete.html'
    success_url = reverse_lazy('category:category_list')





