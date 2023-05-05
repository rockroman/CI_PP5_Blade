# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import (render, redirect,
                              reverse, HttpResponse, get_object_or_404)
from django.contrib import messages
from django.http import JsonResponse
import math

# Internal:
from .forms import OrderForm

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def store_checkout(request):
    cart_data = request.session.get('cart', {})
    if not cart_data:
        messages.error(request, "Your Shopping cart is empty")
        return redirect(reverse('products:store_products'))

    order_form = OrderForm()
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Mu1otHnuSLdtSyi5NC1phkRtR0eb4nxnXlX8bQpYVv3YPoBk7FAN9mDNlDz3e75pTDyWg7BTJ2s9eYikIYk5ToC0081myun6k',
        'client_secret':' test client secret'
    }

    return render(request, 'checkout/checkout.html', context)
