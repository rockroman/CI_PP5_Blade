# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import (render, get_object_or_404,
                              redirect, reverse, HttpResponseRedirect)
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils import timezone

# Internal:
from .models import Review
from .forms import ReviewForm
from products.models import Product
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@login_required
def create_review(request):
    """
    view responsible for creating a product review
    """
    if request.method == 'POST':
        product_id = int(request.POST['product_id'])
        product = Product.objects.get(id=product_id)
        username = request.POST['user']
        content = request.POST['content']
        current_time = request.POST['current_time']
        user = User.objects.get(username=username)

        review = Review.objects.create(
            author=user,
            product=product,
            content=content,
            time_posted=current_time
        )

        my_message = f'Review succesfully added'
        data = {'id': review.id, 'author': review.author.username,
                'product': review.product.name, 'content': review.content,
                'time_posted': review.time_posted,  'message': my_message,
                'status': 'created'}
    else:
        error = {
            'message': 'An Error ocurred!!'
        }
        return JsonResponse(error)

    return JsonResponse(data)


@login_required
def update_review(request):
    if request.method == 'POST':
        content = request.POST['content']
        id = int(request.POST['product_id'])
        current_time = request.POST['current_time']
        review = Review.objects.get(id=id)

        try:
            review = get_object_or_404(Review, pk=id)

        except review.DoesNotexist:
            error = {
                'message': 'An Error ocurred!!',
                'status': 'error'
            }
            return JsonResponse(error)

        if request.user == review.author:
            review.content = content
            review.time_posted = timezone.now()
            review.save()
            my_message = f'Review succesfully updated'
        else:
            my_message = f"CAN'T UPDATE REVIEW!! NOT AUTHOR "

        data = {'id': review.id, 'author': review.author.username,
                'product': review.product.name, 'content': review.content,
                'time_posted': review.time_posted, 'message': my_message,
                'status': 'edited'}

        return JsonResponse(data)


def delete_review(request):
    """
    daleting the review
    """
    if request.method == 'POST':
        review_id = request.POST.get('review_id')
        review = get_object_or_404(Review, id=review_id)

        print(review.author)

        if request.user == review.author:
            review.delete()
            messages.info(request, f' Your Review is deleted')

        else:
            messages.error(request,
                           'CANT DELETE!! TOU ARE NOT AUTHOR OF A REVIEW ')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
