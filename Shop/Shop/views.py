from django.shortcuts import render
from product.models import Product, ProductImage


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True)
    return render(request, 'product/index.html', locals())
