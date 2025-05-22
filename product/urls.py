from django.urls import path
from .views import *
from .views_api import *

app_name = 'product'

urlpatterns = [
    path('api/products/', product_list_api, name='product_list_api'),
    path('api/products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update_api'),
    path('api/products/<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail_api'),
    path('api/products/update/<int:pk>/', ProductUpdateAPIView.as_view(), name='product_update_api'),
    path('api/products/<int:pk>/delete/', ProductDeleteAPIView.as_view(), name='product_delete_api'),




    path('', product_list, name='product_list'),
    path('New/', product_new, name='product_new'),
    path('Update/<int:product_id>/', product_update, name='product_update'),
    path('<int:product_id>/', product_detail, name='product_detail'),
    path('sdelete/<int:product_id>/', product_soft_delete, name='product_soft_delete'),
    path('hdelete/<int:product_id>/', product_hard_delete, name='product_hard_delete'),
    path('deleted/', deleted_products, name='deleted_products'),
    path('restore/<int:pk>/', product_restore, name='product_restore'),
    path('newf/', product_createf, name='product_createf'),
    path('updatef/<int:id>/', product_updatef, name='product_updatef'),
    path('list', ProductListView.as_view(), name='product_listc'),
    path('deletec/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

]
