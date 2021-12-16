from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.title, name ="title"),
    path("search/", views.search, name = "search"),
    path("wiki/new/", views.newpage, name= "newpage"),
    path("wiki/<str:title>/edit", views.editpage, name = "editpage"),
    path("wiki/", views.randompage, name = "randompage")
]
