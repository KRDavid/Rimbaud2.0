from django.shortcuts import render
from django.http import HttpResponse, response
from .models import *
import datetime


def homepage(request):
    return render(request, template_name='homepage.html')

def add(request):
    return render(request, template_name="add.html")

def add_article(request):
    article = Article.objects.create(title='test',
        description='oskour sauvez moi',
        article='mange tes morts anaconda',
        date_limite="2051-05-07",
        admin_only=True)
    article.save()

def check_articles(request):
    query = Article.objects.filter(date_limite__range=[datetime.datetime.utcnow(),"9999-12-31"])
    data = []
    for item in query.values():
        data.append(item)
    responseitem = {"data" : data}
    return render(request, template_name='check_articles.html', context=responseitem)

def view_article(request, id):
    query = Article.objects.filter(id= id)
    responseitem = {"data": query.values()[0]}
    return render(request, template_name='article.html', context=responseitem)