from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('add/', views.add_product, name='add_product'),
]