from django.shortcuts import render
from .models import Product
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def product_list(request):
    products = Product.objects.all().order_by('id')[:5]  # Первые 5 изделий
    return render(request, 'products/product_list.html', {'products': products})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # авторизовать сразу после регистрации
            return redirect('home')  # путь куда перенаправить
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})