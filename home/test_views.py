"""
home views test module
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase, Client
from django.urls import reverse, resolve
# Internal:
from customer_profile.models import User

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestHomeView(TestCase):

    def test_home_page_loads(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_load_right_template(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, 'home/index.html')
