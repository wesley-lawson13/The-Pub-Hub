from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "home/homepage.html")

def posts(request):
    return render(request, "home/posts.html")
