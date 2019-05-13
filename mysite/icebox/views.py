from django.shortcuts import render


def product_list(request):
    return render(request, 'icebox/product_list.html', {})
# Create your views here.
