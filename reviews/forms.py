# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django import forms
from django.forms import Textarea


# Internal:
from .models import Review
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class ReviewForm(forms.ModelForm):
    """
    simple form to render product reviews
    """
    class Meta:
        model = Review
        fields = ['id', 'content']
        widgets = {
            'content': forms.Textarea(attrs={"rows": 4})
        }
