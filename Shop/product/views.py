from django.shortcuts import render, redirect
from cart.models import Order
from account.models import Profile
from product.models import Product


def product(request, product_id):
    product_single = Product.objects.get(id=product_id)
    return render(request, 'product/product_single.html', locals())
