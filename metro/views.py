from django.shortcuts import render
from .models import Product


def product_list(request):
    products = Product.objects.all()
    
    total_price = sum(float(product.unit_price) * product.quantity for product in products)
    return render(request, 'metro/index.html', {'products': products, 'total_price': total_price})
