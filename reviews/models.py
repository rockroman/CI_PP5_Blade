# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from django.contrib.auth.models import User

# Internal:
from products.models import Product

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Review(models.Model):
    """
    class that is handling user reviews of a store
    product
    """
    author = models.ForeignKey(User,
                               on_delete=models.SET_NULL,
                               null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.CharField(max_length=1024)
    time_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time_posted']

    def __str__(self) -> str:
        return f'Review by {self.author.username} for {self.product.name}: {self.content}'
