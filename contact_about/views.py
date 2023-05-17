from django.shortcuts import render

# Create your views here.


def contact_about(request):
    return render(request, 'contact_about/contact_about.html')
