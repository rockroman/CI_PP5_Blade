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
    """
    class Meta:
        model = Review
        fields = ['id', 'content']
        widgets = {
            'content': forms.Textarea(attrs={"rows": 4})
        }
