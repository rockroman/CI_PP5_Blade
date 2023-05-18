# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Internal:
from .models import Review
from .forms import ReviewForm
from products.models import Product
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def create_review(request):
    """
    """
    if request.method == 'POST':
        product_id = int(request.POST['product_id'])
        product = Product.objects.get(id=product_id)
        username = request.POST['user']
        content = request.POST['content']
        user = User.objects.get(username=username)

        review = Review.objects.create(
            author=user,
            product=product,
            content=content
        )
        my_message = f'Review succesfully added'
        data = {'id': review.id, 'author': review.author.username,
                'product': review.product.name, 'content': review.content, 'message': my_message}
    else:
        error = {
            'message': 'An Error ocurred!!'
        }
        return JsonResponse(error)

    return JsonResponse(data)

