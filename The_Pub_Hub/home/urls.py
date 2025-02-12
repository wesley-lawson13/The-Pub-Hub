from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("posts", views.posts, name="posts"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("about", views.about, name="about")
]