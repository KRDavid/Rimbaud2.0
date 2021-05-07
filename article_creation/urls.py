from django.urls import path

from . import views

urlpatterns = [

    path('posts/<int:id>/', views.show, name='show'),
    path('posts/create/', views.create, name='create'),
    path('posts/check_articles/', views.check_articles, name='check_articles'),           
    path('', views.index, name='index'),

    
]