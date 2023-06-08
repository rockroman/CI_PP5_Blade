# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import (render,
                              get_object_or_404, HttpResponseRedirect,
                              redirect, reverse)
# Internal:
from .models import Wishlist
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def wishlist_objects(request):
    """
    handling wishlist objects for
    navbar counter throughout entire project
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
