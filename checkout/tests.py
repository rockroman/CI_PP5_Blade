"""
A module for testing models
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase
# Internal:
from .models import Order, OrderLineItem
from customer_profile.models import CustomerProfile
from products.models import Product
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestOrderModel(TestCase):
    """
    creating a test order
    """
    # @classmethod
    # def setUp(self):
    #     """
    #     creating and saving a new test user
    #     """
    #     self.customer_profile = CustomerProfile.objects.create(
    #         user=,
    #         password='mypass7900',
    #         email='test@user.com',
    #         id='0',

    #     )
    #     self.user.save()

    def test_string_method_return_orde_num(self):
        new_order = Order.objects.create(
            order_number='A7AEF9E2B7E44986BEB538E58EE25BBE',
            full_name='Test user',
            email='test@bo.com',
            phone_number='353231245',
            country='Ireland',
            postcode='P12RE44',
            street_address1='Sowhere',
            street_address2='Sowhere2',
            county='Laois',
            date='12.05.2023',
            order_total='220.00',
            grand_total='220.00',
            original_cart='',
            stripe_pid='12we'

        )
        self.assertEqual(str(new_order), 'A7AEF9E2B7E44986BEB538E58EE25BBE')


class TestOrderLineItem(TestCase):

    def test_str_method(self):
        my_order = Order.objects.create(
            order_number='A7AEF9E2B7E44986BEB538E58EE25BBE',
            full_name='Test user',
            email='test@bo.com',
            phone_number='353231245',
            country='Ireland',
            postcode='P12RE44',
            street_address1='Sowhere',
            street_address2='Sowhere2',
            county='Laois',
            date='12.05.2023',
            order_total='220.00',
            grand_total='220.00',
            original_cart='',
            stripe_pid='12we',

        )
        test_product = Product.objects.create()

        new_line_item = OrderLineItem.objects.create(
            order=my_order,

        )
