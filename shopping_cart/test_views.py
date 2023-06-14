# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase, Client, RequestFactory
from django.urls import reverse, resolve
from django.shortcuts import get_object_or_404
from django.http import HttpRequest
from django.contrib.messages import get_messages
import json
# Internal:
from products.models import Product, Category
from .views import remove_from_cart

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestCartView(TestCase):

    def test_view_returning_template(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shopping_cart/cart.html')


class TestAddToCartView(TestCase):

    def test_adding_product_to_cart(self):
        response = self.client.post('/add_to_cart/', data={
            'id': '1',
            'name': 'Dark Moon',
            'qty': '2',
            'image': 'dark_moon.jpg',
            'price': '245.50',
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        cart_data = response_data['data']
        self.assertTrue(cart_data)
        cart_item = cart_data['1']
        self.assertEqual(cart_item['name'], 'Dark Moon')
        self.assertEqual(cart_item['qty'], 2)
        self.assertEqual(cart_item['price'], 245.50)
        self.assertEqual(cart_item['image'], 'dark_moon.jpg')


# class TestRemoveFromCartView(TestCase):

#     def test_remove_product_from_cart(self):
#         self.client = Client()
#         category = Category.objects.create(
#             id=1,
#             name='Explorer',
#             notes='test notes',
#             slug='test slug',
#             friendly_name='Explorer'
#         )
#         category.save()

#         product = Product.objects.create(
#             id=1,
#             category=category,
#             item_no="B123",
#             name="Dark Moon",
#             description="The Dark Moon  a custom folding knife that embodies the sharpness and sophistication of a true gentleman,With a 9.2 cm high carbon steel blade and a stylish camel bone handle, this knife is both sharp and elegant. Perfect for formal occasions or everyday use, the Dark Moonblade is a must-have for any gentleman who values style and functionality in their knife collection.",
#             price=245.50,
#             bladelength="9.2",
#             blade="Damaskus steel",
#             handlematerial="Camel bone",
#             image_url="",
#             image="dark_moon.jpg")
#         cart_data = {
#             '1': {

#                 'name': 'Dark Moon',
#                 'qty': '2',
#                 'image': 'dark_moon.jpg',
#                 'price': '245.50',

#             }
#         }
#         self.client.session['cart'] = cart_data
#         self.assertTrue(product)
#         self.assertTrue(len(cart_data),1)

        # response = self.client.post('/remove/1/')
        # if response.status_code != 200:
        #     print(response.content)
        # self.assertEqual(response.status_code, 200)
