# Generated by Django 3.2 on 2023-05-14 22:37

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Whislist',
            new_name='Wishlist',
        ),
    ]
