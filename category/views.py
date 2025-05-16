from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def catagory_list(requst):
    return HttpResponse('<h1>category list</h1>')
def catagory_new(requst):
    return HttpResponse('<h1>category added</h1>')
def catagory_update(requst ,id ):
    return HttpResponse(f'<h1>category Updated{id}</h1>')
