# shopping/views.py
from django.shortcuts import render
from shopping.models import Cart
from django.http import JsonResponse
from .models import Product


def shopping(request):
    template_name = 'shopping.html'
    return render(request, template_name)

def cart_items(request, pk):
    template_name = 'cart_items.html'
    carts = Cart.objects.filter(shop=pk)

    qs = carts.values_list('price', 'quantity') or 0
    total = sum(map(lambda q: q[0] * q[1], qs))

    context = {'object_list': carts, 'total': total}
    return render(request, template_name, context)

def get_products(request):
    products = Product.objects.all()
    data = [{'pk': product.pk, 'name': product.name} for product in products]
    return JsonResponse({'data': data})