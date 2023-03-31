from django.shortcuts import render
from Products.models import Product

def index(request):
    return render(request, "index.html")

def shop(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop.html', context)

def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")