# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import AnonymousUser
from django.http import JsonResponse

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


# def wishlist_total(request):
#     """
#     handling wishlist objects for
#     navbar counter
#     """

#     if request.user.is_authenticated:
#         wishlist_count = Wishlist.objects.filter(user=request.user).count()
#         # request.session['wishlist_count'] = wishlist_count

#     else:
#         wishlist_count = 0
#         # request.session['wishlist_count'] = wishlist_count

#     return JsonResponse({
#         'wishlist_count': wishlist_count,

#     })
