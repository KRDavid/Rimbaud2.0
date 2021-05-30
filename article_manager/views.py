from django.shortcuts import render
from django.http import HttpResponse, response
from .models import *
import datetime


def homepage(request):
    return render(request, template_name='homepage.html')

def add(request):
    return render(request, template_name="add.html")

def add_article(request):
    title = request.POST.get("titre")
    article = request.POST.get("article")
    desc = request.POST.get("desc")
    date = request.POST.get("date")
    
    article = Article.objects.create(title=title,
        description=desc,
        article=article,
        date_limite=date,
        admin_only=True)
    article.save()

    return HttpResponse("200")

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

def search(request):
    titre = request.POST.get("titre")
    query = Article.objects.filter(title = titre)
    responseitem = {"data": query.values()[0]}
    return render(request, template_name='article.html', context=responseitem)

def searchid(request):
    id = request.POST.get("id")
    query = Article.objects.filter(id = id)
    responseitem = {"data": query.values()[0]}
    return render(request, template_name='article.html', context=responseitem)