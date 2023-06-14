# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase, Client
from django.urls import reverse, resolve
import json
# Internal:

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
