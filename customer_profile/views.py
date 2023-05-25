# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import (render, redirect,
                              reverse, HttpResponse, get_object_or_404)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.conf import settings


# Internal:
from customer_profile.models import CustomerProfile
from .forms import CustomerProfileForm
from checkout.models import Order


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@login_required
def profile(request):
    """
    view handling user profile

    """
    customer_profile = get_object_or_404(CustomerProfile, user=request.user)
    if request.method == 'POST':
        form = CustomerProfileForm(request.POST, instance=customer_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile is updated")
        else:
            messages.error(request, 'Failed to update profile please check your form for errors')
    else:
        form = CustomerProfileForm(instance=customer_profile)
    orders = customer_profile.orders.all()
    template = 'customer_profile/profile.html'
    context = {

        'form': form,
        'orders': orders,
        'customer_profile': customer_profile,
        'on_profile_page': True

    }
    return render(request, template, context)


def order_history(request, order_number):

    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
