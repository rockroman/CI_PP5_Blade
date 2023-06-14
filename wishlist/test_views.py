# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase, Client
from django.urls import reverse, resolve
# Internal:
from .models import Wishlist
from products.models import Product, Category
from django.contrib.auth.models import User
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestWishlistView(TestCase):

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
        self.user.set_password('mypass799')
        self.user.save()

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
        self.user.delete()

    def test_rendering_right_template(self):
        """
        anonymous user trying to access wishlist view
        redirected to login
        """
        response = self.client.get('/wishlist/')
        self.assertEqual(response.status_code, 302)

        """
        logged in user accessing wishlist view
        """

        self.client.login(username='MyTestUser', password='mypass799')
        response = self.client.get('/wishlist/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wishlist/wishlist.html')


class TestAddingToWishlist(TestCase):

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
        self.user.set_password('mypass799')
        self.user.save()

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
            blade='Steel',
            id=23,
        )
        self.product.save()

    def test_removing_from_wishlist(self):
        self.client = Client()
        self.client.login(username='MyTestUser', password='mypass79')
        if self.client._login:
            print("User is logged in")
        else:
            print("User is not logged in")

        print(f"Product ID: {self.product.id}")
        wishlist_item = Wishlist.objects.create(user=self.user, product_id=23)
        wishlist_item_id = wishlist_item.id
        response = self.client.post('/wishlist/remove_from_wishlist/', data={'item-id': wishlist_item_id})
        print(f"Wishlist count: {Wishlist.objects.count()}")
        self.assertEqual(response.status_code, 302)
