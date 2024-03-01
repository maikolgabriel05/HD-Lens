# api/urls.py
from django.urls import path
from .views import CustomerListView

urlpatterns = [
    path('api/customers/', CustomerListView.as_view(), name='customer-list'),
]
