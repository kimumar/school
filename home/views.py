from django.shortcuts import render, redirect
from . models import ContactMessage, ContactForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        contact = ContactForm(request.POST)
        if contact.is_valid():
            data = ContactMessage()
            data.name = contact.cleaned_data['name']
            data.email = contact.cleaned_data['email']
            data.subject = contact.cleaned_data['subject']
            data.message = contact.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            contact.save()
            messages.success(request,"Your message has been sent! Our Customer Service Team Will reach you soon.")
            return HttpResponseRedirect('#contact')
    
    contact = ContactForm

    context = {
        'contact':contact,
    }

    return render(request, "school_app/index.html", context)

def login(request):
    return render(request, "school_app/login.html")

def register(request):
    return render(request, "school_app/register.html")