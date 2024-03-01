#shopping/models.py
from django.shortcuts import render
from .models import Cart, Product, Shop
from django.http import JsonResponse
from django.views import View



def shopping(request):
    template_name = 'shopping.html'
    # Buscar produtos do banco de dados
    products = Product.objects.all()

    context = {'products': products}
    return render(request, template_name, context)


def cart_items(request, pk):
    template_name = 'cart_items.html'
    carts = Cart.objects.filter(shop=pk)

    qs = carts.values_list('price', 'quantity') or 0
    total = sum(map(lambda q: q[0] * q[1], qs))

    context = {'object_list': carts, 'total': total}
    return render(request, template_name, context)

class CustomerListView(View):
    def get(self, request, *args, **kwargs):
        shops = Shop.objects.all()
        customer_list = [{'pk': shop.pk, 'name': shop.customer} for shop in shops]
        return JsonResponse({'data': customer_list})
