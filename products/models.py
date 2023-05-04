# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
import random
import string

# Internal:

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Create your models here.

class Category(models.Model):
    """
    class for category model
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    notes = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=254, blank=True, null=True)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


def random_generated_string():
    not_unique = True
    while not_unique:
        key = random.choice(string.ascii_uppercase) + str(random.randrange(100,999))
        if not Product.object.filter(item_no=key):
            not_unique = False
    return str(key)


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    item_no = models.CharField(max_length=254, default=random_generated_string,unique=True )
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    blade_length = models.DecimalField(max_digits=5, decimal_places=2 )
    handle_material = models.CharField(max_length=254)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name



