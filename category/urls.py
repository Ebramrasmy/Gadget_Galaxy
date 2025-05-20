from django.urls import path
from . import views
from .views import *

app_name = 'category'

urlpatterns = [
    path('', CategoryListView.as_view(), name='category_list'),
    path('new/', CategoryCreateView.as_view(), name='category_new'),
    path('update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    # path('<int:category_id>/hard_delete/', views.category_hard_delete, name='category_hard_delete'),
    # path('deleted/', views.deleted_categories, name='deleted_categories'),
    # path('<int:category_id>/restore/', views.category_restore, name='category_restore'),
]