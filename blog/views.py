from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all().order_by('id')[:5]  # Первые 5 изделий
    return render(request, 'products/product_list.html', {'products': products})