# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase, Client
from django.urls import reverse, resolve
import json
# Internal:
from django.contrib.auth.models import User
from .models import Review
from products.models import Category, Product
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestReviewViews(TestCase):

    @classmethod
    def setUp(self):
        """
        creating and saving a new test review
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

    def test_review_creation(self):
        self.client.force_login(self.user)
        response = self.client.post('/review/create_review/', data={
            'id': '3',
            'user': self.user.username,
            'product_id': self.product.id,
            'content': 'My test Review',
            'current_time': '2023-06-13T12:00:00'
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(Review.objects.filter(author=self.user).exists())

    def test_update_review(self):
        self.client.force_login(self.user)
        self.my_review = Review.objects.create(
            author=self.user,
            product=self.product,
            content='My New test review',
            id='5'

        )
        response = self.client.post('/review/update_review/',data={
            'product_id': self.my_review.id,
            'content': 'just Review',
            'current_time': '2023-06-13T12:00:20',
            'id': '5'

        })
        self.assertEqual(response.status_code, 200)

    def test_delete_review(self):
        self.client.force_login(self.user)
        self.my_review = Review.objects.create(
            author=self.user,
            product=self.product,
            content='My New test review',
            id='5'

        )
        # user author of review deleting review
        response = self.client.post('/review/delete_review/',data={
                'review_id': self.my_review.id

        })
        self.assertEqual(response.status_code, 302)

        self.new_user = User.objects.create(
            username='MyNewTestUser',
            password='mypass719',
            email='teste@user.com',
            id='3',
        )
        self.new_user.save()
        self.my_new_review = Review.objects.create(
            author=self.new_user,
            product=self.product,
            content='My New test review',
            id='5'

        )
        # user  NOT author of review trying to delete review
        response = self.client.get('/review/delete_review/',
                                   data={
                                    'review_id': self.my_new_review.id,
                                    'product_id': self.product.id,

                                                                    })
        self.assertTrue(Review.objects.filter(content='My New test review').exists())
        self.assertEqual(response.status_code, 302)
