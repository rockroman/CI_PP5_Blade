# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


# Internal:
from .models import Contact
from .forms import ContactForm

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def contact_about(request):
    """
    """
    if request.method == 'POST':
        form = ContactForm()
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            subject = form.cleaned_data['inquiry_purpose']

        else:
            messages.error(request, f'An error occured please check the form')

    context = {
        'form': form,
    }
    return render(request, 'contact_about/contact_about.html', context)
