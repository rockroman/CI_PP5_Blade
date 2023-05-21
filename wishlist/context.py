# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import AnonymousUser

# Internal:
from .models import Wishlist


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def wishlist_objects(request):
    """
    handling wishlist objects for
    navbar counter
    """
    context = {}
    if request.user.is_authenticated:
        wishlist_count = Wishlist.objects.filter(user=request.user).count()
        context = {
            'wishlist_count': wishlist_count
            }
    else:
        wishlist_count = 0
        context = {
            'wishlist_count': wishlist_count

        }

    return context
