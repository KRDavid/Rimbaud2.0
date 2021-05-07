from django.shortcuts import render
from django.http import HttpResponse, response
from .models import *


def hello(request):
    content = {"test_variable" : "blablabla"}
    return render(request, template_name='index.html', context=content)

def add_article(request):
    article = Article.objects.create(title='test',
        description='test description',
        article='blablablablablabla',
        date_limite="2021-05-07",
        admin_only=True)

    article.save()