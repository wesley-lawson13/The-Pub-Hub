from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "home/homepage.html")

def posts(request):
    return render(request, "home/posts.html") 

def login(request):
    return render(request, "home/login.html")

def register(request):
    return render(request, "home/register.html")

def about(request):
    return render(request, "home/about.html")