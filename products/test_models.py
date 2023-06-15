# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase, Client
from django.urls import reverse, resolve
# Internal:
from django.contrib.auth.models import User
from .models import Category, Product
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class TestCategoryModel(TestCase):

    @classmethod
    def setUp(self):
        """
        creating and saving a new test category
        """
        self.my_category = Category.objects.create(
            name='Hunter',
            notes='test notes',
            slug='test slug',
            id='1',
            friendly_name='Hunter'
        )
        self.my_category.save()

    def tearDown(self):
        self.my_category.delete()

    def test_string_method_return(self):
        self.assertEqual(str(self.my_category), 'Hunter')

    def test_get_friendly_name(self):
        self.assertTrue(self.my_category.get_friendly_name())


class TestProductModel(TestCase):

    @classmethod
    def setUp(self):
        """
        creating and saving a new test Product
        """
        self.my_category = Category.objects.create(
            name='Savage',
            notes='test notes',
            slug='testslug',
            friendly_name='Hunter knife'
        )
        self.my_category.save()
        self.product = Product.objects.create(
            category=self.my_category,
            item_no='A221',
            name='Test Hunter',
            description='Test knife description',
            price=230.00,
            bladelength=10,
            handlematerial='Wood',
            blade='Steel'

        )

    def tearDown(self):
        self.my_category.delete()
        self.product.delete()

    def test_string_method_return(self):
        self.assertEqual(str(self.product), 'Test Hunter')



