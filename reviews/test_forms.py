# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase, Client
from django.urls import reverse, resolve
import json
# Internal:
from django.contrib.auth.models import User
from .models import Review
from .forms import ReviewForm
from products.models import Category, Product
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestReviewForm(TestCase):
    def test_review_form(self):
        form_data = {
            'id': 1,
            'content': 'Test review content'
        }
        form = ReviewForm(data=form_data)
        self.assertTrue(form.is_valid())