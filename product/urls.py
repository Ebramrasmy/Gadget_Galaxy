from django.urls import path
from .views import *

app_name = 'product'

urlpatterns = [
    path('', product_list, name='product_list'),
    path('New/', product_new, name='product_new'),
    path('Update/<int:product_id>/', product_update, name='product_update'),
    # path('<int:product_id>/', product_details, name='product_details'),
    path('sdelete/<int:product_id>/', product_soft_delete, name='product_soft_delete'),
    path('hdelete/<int:product_id>/', product_hard_delete, name='product_hard_delete'),
    path('deleted/', deleted_products, name='deleted_products'),
    path('restore/<int:pk>/', product_restore, name='product_restore'),

]
