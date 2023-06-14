# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase, Client
from django.urls import reverse, resolve
# Internal:
from django.contrib.auth.models import User
from .models import CustomerProfile
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestCustomerProfile(TestCase):

    @classmethod
    def setUp(self):
        """
        creating and saving a new test user
        """
        self.user = User.objects.create(
            username='MyTestUser',
            password='mypass79',
            email='test@user.com',
            id='1',
        )
        self.user.save()

        self.customer_profile = CustomerProfile.objects.update(
            default_phone_number='16553',
            default_country='Croatia',
        )

    def test_is_profile_created(self):
        customer_profile = CustomerProfile.objects.filter().last()
        self.assertEqual(customer_profile.user.username, 'MyTestUser')
        self.assertEqual(customer_profile.default_phone_number, '16553')

    def test_string_method_return(self):
        customer_profile = CustomerProfile.objects.get(user=self.user)
        self.assertEqual(str(customer_profile), 'MyTestUser')
