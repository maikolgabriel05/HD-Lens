#shopping/urls.py
from django.urls import path
from shopping import views as v
from .views import CustomerListView


app_name = 'shopping'


urlpatterns = [
    path('shopping/', v.shopping, name='shopping'),
    path('cart-items/<int:pk>/', v.cart_items, name='cart_items'),
    path('api/customers/', CustomerListView.as_view(), name='customer-list'),
]
