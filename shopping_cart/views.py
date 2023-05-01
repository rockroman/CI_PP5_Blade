# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, redirect, reverse, HttpResponse
from django.http import JsonResponse

# Internal:

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def cart(request):
    """
    view to render the shopping cart
    """
    template = 'shopping_cart/cart.html'

    return render(request, template)


# def add_to_cart(request):
#     # del request.session['cartdata']
#     cart_item = {}
#     cart_item[str(request.GET['id'])] = {
#         'name': request.GET['name'],
#         'image': request.GET['image'],
#         'qty': int(request.GET['qty']),
#         'price': request.GET['price'],
#     }
#     if 'cartdata' in request.session:
#         if str(request.GET['id']) in request.session['cartdata']:
#             cart_data = request.session['cartdata']
#             cart_data[str(request.GET['id'])]['qty'] = int(cart_item[str(request.GET['id'])]['qty'])
#             cart_data.update(cart_data)
#             request.session['cartdata'] = cart_data
#         else:
#             cart_data = request.session['cartdata']
#             cart_data.update(cart_item)
#             request.session['cartdata'] = cart_data

#     else:
#         request.session['cartdata'] = cart_item

#     return JsonResponse({'data': request.session['cartdata'], 'totalitems': len(request.session['cartdata'])})


def add_to_cart(request):

    cart_item = {}
    cart_item[str(request.POST['id'])] = {
        'name': request.POST['name'],
        'image': request.POST['image'],
        'qty': int(request.POST['qty']),
        'price': request.POST['price'],
    }
    if 'cart' in request.session:
        if str(request.POST['id']) in request.session['cart']:
            cart_data = request.session['cart']
            cart_data[str(request.POST['id'])]['qty'] += int(request.POST['qty'])
            cart_data.update(cart_data)
            request.session['cart'] = cart_data
        else:
            cart_data = request.session['cart']
            cart_data.update(cart_item)
            request.session['cart'] = cart_data

    else:
        request.session['cart'] = cart_item

    return JsonResponse({'data': request.session['cart'], 'total_items': len(request.session['cart'])})


def update_cart(request, product_id):
    """
    update quantty of tems in a bag to desired value
    """
    quantity = int(request.POST.get('quantity'))
    cart_data = request.session.get('cart', {})

    if quantity > 0:
        cart_data[product_id]['qty'] = quantity

    else:
        cart_data.pop(product_id)

    request.session['cart'] = cart_data

    return redirect(reverse('shopping_cart:cart'))


def remove_from_cart(request, product_id):
    """
    update quantty of tems in a bag to desired value
    """
    cart_data = request.session.get('cart', {})
    try:
        cart_data.pop(product_id)

        request.session['cart'] = cart_data

        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
