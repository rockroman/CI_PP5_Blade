# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase, Client
from django.urls import reverse, resolve
# Internal:
from .views import contact_about
from .forms import ContactForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestContactView(TestCase):

    def test_template_used(self):
        response = self.client.get('/contact_about/')
        self.assertTemplateUsed(response, 'contact_about/contact_about.html')

    def test_mail_sent(self):
        response = self.client.post('/contact_about/', data={
            'inquiry_purpose ': 'PRODUCT',
            'name': 'tester',
            'email': 'test@net.com',
            'phone': '12456',
            'message': 'test message'
        }, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_mail_not_sent(self):
        """
        user inputs invalid e mail address
        """
        response = self.client.post('/contact_about/', data={
            'inquiry_purpose ': 'PRODUCT',
            'name': 'tester',
            'email': 'testnet.com',
            'phone': '12456',
            'message': 'test message'
        }, follow=True)
        self.assertContains(response, 'An error occured please check the form')
