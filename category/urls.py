from django.urls import path
from . import views

app_name = 'category'

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('new/', views.category_new, name='category_new'),
    path('<int:category_id>/edit/', views.category_update, name='category_update'),
    path('<int:category_id>/delete/', views.category_soft_delete, name='category_soft_delete'),
    path('<int:category_id>/hard_delete/', views.category_hard_delete, name='category_hard_delete'),
    path('deleted/', views.deleted_categories, name='deleted_categories'),
    path('<int:category_id>/restore/', views.category_restore, name='category_restore'),
]