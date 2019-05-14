from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.order_by('date')
    return render(request, 'icebox/product_list.html', {'products':products})
# Create your views here.
