from django.shortcuts import render
from django.http import HttpResponse, response
from .models import *
import datetime


def hello(request):
    content = {"test_variable" : "blablabla"}
    return render(request, template_name='index.html', context=content)

def add_article(request):
    article = Article.objects.create(title='test',
        description='test description',
        article='blablablablablabla',
        date_limite="2011-05-07",
        admin_only=True)

    article.save()

def check_articles(request):
    query = Article.objects.filter(date_limite__range=[datetime.datetime.utcnow(),"9999-12-31"])
    responseitem = {}
    i = 0
    for item in query.values():
        responseitem[i] = item
        i += 1
    
    return render(request, template_name='index.html', context=responseitem)
