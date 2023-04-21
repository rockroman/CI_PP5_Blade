"""
home views test module
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase, Client
from django.urls import reverse, resolve
# Internal:



class TestHomeView(TestCase):

    def test_home_page_loads(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
