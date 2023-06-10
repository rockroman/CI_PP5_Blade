# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase, Client
from django.urls import reverse, resolve
# Internal:
from .models import Contact
from customer_profile.models import User
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestContactModel(TestCase):

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

    def tearDown(self):
        self.user.delete()

    def test_string_method_return(self):
        self.contact = Contact.objects.create(
            inquiry_purpose='ORDER',
            name=self.user.username,
            email='test@user.com',
            phone='122445',
            message='test message'

        )
        self.assertEqual(str(self.contact),
                         'Contact MyTestUser and message created')
