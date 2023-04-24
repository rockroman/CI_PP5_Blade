# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, get_object_or_404

# Internal:
from .models import Product

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def store_products(request):

    products = Product.objects.all()
    template = 'products/store_products.html'

    context = {
        'products': products,
    }

    return render(request,template, context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    template = 'products/product_details.html'

    context = {
        'product': product,
    }

    return render(request,template, context)
