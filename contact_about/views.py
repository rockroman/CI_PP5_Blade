# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


# Internal:
from .models import Contact
from .forms import ContactForm

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def contact_about(request):
    """
    view rendering contact form and
    send mail functionality
    """
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            user_message = form.cleaned_data['message']
            subject = form.cleaned_data['inquiry_purpose']
            message = render_to_string(
                'contact_about/confirmation_email/email_confirmation.txt', {
                    'name': name,
                    'message': user_message
                })
            email_from = settings.DEFAULT_FROM_EMAIL
            email_to = [form.cleaned_data['email']]

            send_mail(
                subject,
                message,
                email_from,
                email_to
            )
            messages.success(request, f'Your message was sent successfuly')
            return redirect(reverse('contact_about:contact_about'))

        else:
            messages.error(request, f'An error occured please check the form')

    context = {
        'form': form,
    }
    return render(request, 'contact_about/contact_about.html', context)
