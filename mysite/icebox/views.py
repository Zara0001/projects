from django.shortcuts import render
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> f027bc0ea78b2cc7cb7ba6bbb7db901e08f14dcf
from .models import Product

def product_list(request):
    products = Product.objects.order_by('date')
    return render(request, 'icebox/product_list.html', {'products':products})
<<<<<<< HEAD
=======
=======

>>>>>>> b76ad898fa57d9957aa004cee1efdb91f190f550
>>>>>>> f027bc0ea78b2cc7cb7ba6bbb7db901e08f14dcf
# Create your views here.
