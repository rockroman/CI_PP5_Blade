# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django import forms

# Internal:
from .models import Contact
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class ContactForm(forms.ModelForm):
    """
    Contact model form
    """

    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        """
        overriding init method and adding placeholders to
        form fields
        """
        placeholders = {
            'name': 'Name',
            'email': 'Email Address',
            'phone': 'Phone number',
            'message': 'message',
        }

        for field in self.fields:
            if field != 'inquiry_purpose':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            # add class to fields
            # self.fields[field].widget.attrs['class'] = 'my-2'