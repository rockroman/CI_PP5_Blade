# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase, Client
from django.urls import reverse, resolve
import json
# Internal:
from django.contrib.auth.models import User
from products.models import Category, Product
from .forms import ProductForm
from reviews.models import Review
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestStoreProductsView(TestCase):
    @classmethod
    def setUp(self):
        """
        create test product
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
            blade='Steel',
            id='1'
        )

    def tearDown(self):
        self.product.delete()
        self.my_category.delete()

    def test_returning_the_template(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('/products/store_products.html/')


class TestProductDetailsView(TestCase):

    @classmethod
    def setUp(self):
        """
        create test product
        """
        self.user = User.objects.create(
            username='MyTestUser',
            password='mypass79',
            email='test@user.com',
            id='1',
        )
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
            id='1'
        )
        self.my_review = Review.objects.create(
            author=self.user,
            product=self.product,
            content='My New test review',
            id='5'

        )

    def tearDown(self):
        self.product.delete()
        self.my_category.delete()
        self.my_review.delete()

    def test_returning_the_template(self):
        response = self.client.get('/products/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_details.html')


class TestAddProduct(TestCase):

    def setUp(self):
        """
        create test product
        """
        self.user = User.objects.create(
            username='MyTestUser',
            password='mypass79',
            email='test@user.com',
            id='1',
            is_superuser=True
        )
        self.user.save()

        self.my_category = Category.objects.create(
            name='Savage',
            notes='test notes',
            slug='testslug',
            friendly_name='Hunter knife'
        )
        self.my_category.save()

    def test_add_product(self):
        self.client.force_login(self.user)

        form_data = {
            'category': self.my_category,
            'item_no': 'A221',
            'name': 'Test Hunter',
            'description': 'Test knife description',
            'price': 30.00,
            'bladelength': 10,
            'handlematerial': 'Wood',
            'blade': 'Steel',
            'image': 'noimg.jpg',
            'id': 6
        }
        form = ProductForm(data=form_data)
        self.assertTrue(form.is_valid())
        form.save()
        self.assertTrue(self.user.is_superuser)
        response = self.client.post(reverse('products:add_product'),
                                    data=form.data)
        self.assertEqual(response.status_code, 200)


class TestDeleteProduct(TestCase):

    @classmethod
    def setUp(self):
        """
        create test product
        """
        self.user = User.objects.create(
            username='MyTestUser',
            password='mypass79',
            email='test@user.com',
            id='1',
        )
        self.user.save()
        self.admin_user = User.objects.create(
            username='AdminTestUser',
            password='mypass799',
            email='testnew@user.com',
            id='3',
            is_superuser=True
        )
        self.admin_user.save()

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
            id='1'
        )

    def test_deleting_product_not_admin(self):
        self.client.force_login(self.user)
        response = self.client.post('/delete/1/', follow=True)
        self.assertContains(response, 'SORRY Only store owners have  access')

    def test_deleting_product_admin(self):
        self.client.force_login(self.admin_user)
        response = self.client.post('/delete/1/', follow=True)
        self.assertRedirects(response, reverse('products:store_products'))
