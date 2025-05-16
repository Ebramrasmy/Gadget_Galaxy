from django.urls import path
from .views import *



urlpatterns = [
    path('', catagory_list, name='catagory_list'),
    path('New/', catagory_new, name='catagory_new'),
    path('update/<int:id>', catagory_update, name='catagory_added'),

]