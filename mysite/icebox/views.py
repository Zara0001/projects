from django.shortcuts import render
<<<<<<< HEAD
from .models import Product

def product_list(request):
    products = Product.objects.order_by('date')
    return render(request, 'icebox/product_list.html', {'products':products})
=======

>>>>>>> b76ad898fa57d9957aa004cee1efdb91f190f550
# Create your views here.
