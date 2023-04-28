from django.urls import path
from .views import *


urlpatterns = [
     path('', index, name='index'),
     
     path('products', product_list, name='products'),
     path('contacts/', contacts, name='contacts'),
     path('liked/', liked, name='liked'),

     path('products/item-<int:pk>/', product_detail, name='detail'),

     path('<slug:category_slug>', category, name='category')
]
