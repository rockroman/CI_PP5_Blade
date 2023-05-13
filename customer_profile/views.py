# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import (render, redirect,
                              reverse, HttpResponse, get_object_or_404)
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.conf import settings


# Internal:
from customer_profile.models import CustomerProfile
from .forms import CustomerProfileForm
from checkout.models import Order


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def profile(request):
    """
    view handling user profile
    """

    customer_profile = get_object_or_404(CustomerProfile, user=request.user)
    form = CustomerProfileForm(instance=customer_profile)

    orders = customer_profile.orders.all()
    template = 'customer_profile/profile.html'
    context = {

        'form': form,
        'orders': orders,
        'customer_profile': customer_profile,

    }
    return render(request, template, context)
