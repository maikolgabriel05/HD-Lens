from django.shortcuts import render, redirect
from customers.forms import CustomerForm
from customers.models import Customers

def customers_list(request):
    template_name = 'customers.html'
    customers = Customers.objects.all()
    context = {'customers': customers}
    return render(request, template_name=template_name, context=context)

def create_customer(request):
    template_name = 'create_customer.html'
    form = CustomerForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('customers:customers_list')  # Alterado para 'customers_list'
        else:
            print(form.errors)
    return render(request, template_name=template_name, context=context)

def edit_customer(request, pk):
    customer = Customers.objects.get(pk=pk)
    form = CustomerForm(request.POST or None, instance=customer)
    template_name = 'edit_customer.html'
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('customers:customers_list')  # Alterado para 'customers_list'
        else:
            print(form.errors)
    context = {'form': form}
    return render(request, template_name=template_name, context=context)

def delete_customer(request, pk):
    customer = Customers.objects.get(pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customers:customers_list')  # Alterado para 'customers_list'
    return render(request, 'delete_customer.html', {'customer': customer})
