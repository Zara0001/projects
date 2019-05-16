from django.shortcuts import render
from .models import Product
from .carry import carry

def product_list(request):
    products = Product.objects.order_by('date')
    return render(request, 'icebox/product_list.html', {'products':products})
    return carry(file='../../email/search')
# Create your views here.
