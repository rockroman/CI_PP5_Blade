# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models

# Internal:

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Contact(models.Model):
    """
    class that handles contacting the store
    """

    # options for  Purpose of Inquiry

    INQUIRY_CHOICES = [
        ('', 'Purpose of Inquiry'),
        ('PRODUCT', 'Poduct Inquiry'),
        ('ORDER', 'Order Inquiry'),
        ('SUGGESTIONS', 'Suggestions'),
        ('OTHER', 'Other'),

    ]

    inquiry_purpose = models.CharField(max_length=24, choices=INQUIRY_CHOICES)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField(max_length=1000)
    date_submmited = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_submmited']

    def __str__(self) -> str:
        return f'Contact {self.name} and message created'
