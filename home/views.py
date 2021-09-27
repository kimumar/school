from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "school_app/index.html")

def login(request):
    return render(request, "school_app/login.html")

def register(request):
    return render(request, "school_app/register.html")