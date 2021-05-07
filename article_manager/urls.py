from django.urls import path

from . import views

urlpatterns = [
    path('homepage', views.homepage),
    path('add', views.add),
    path('addart', views.add_article),
    path('check', views.check_articles),
    path('id/<int:id>', views.view_article),
]