# api/serializers.py
from rest_framework import serializers
from customers.models import Customers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['id', 'name']
