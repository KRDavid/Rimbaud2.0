from django.urls import path

from . import views

urlpatterns = [
    path('hello_world', views.hello),
    path('add', views.add_article),
]