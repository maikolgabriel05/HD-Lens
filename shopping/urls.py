# shopping/urls.py
from django.urls import path
from . import views as v
from .views import get_products


app_name = 'shopping'


urlpatterns = [
    path('shopping/', v.shopping, name='shopping'),
    path('cart-items/<int:pk>/', v.cart_items, name='cart_items'),
    path('api/products/', get_products, name='get_products'),
]