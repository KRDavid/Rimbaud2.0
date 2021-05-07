from django.shortcuts import render
import datetime
from .method import Post
from .models import *

# Create your views here.

posts = [
    {'id':1,'title':'First article','body':'This is the first article'},
    {'id':2,'title':'Second article','body':'This is the second article'},
    {'id':3,'title':'Third article','body':'This is the third article'},
]

def index(request):

    posts = Post.objects.all()
    return render(request,'index.html', {'posts':posts})



def show(request, id):

    post = Post.objects.filter(id = id)
    return render(request, 'show.html', { 'post': post.values()[0]})


def create(request):
    
    article = Post.objects.create(title = "First Article", body = 'This is the first article', article = 'Artcile  #1', created_at = datetime.datetime.now(), updated_at = datetime.datetime.now())
    article.save()


def check_articles(request):
    query = Post.objects.filter(limit_date__range=[datetime.datetime.utcnow(),"9999-12-31"])
    data = []
    for item in query.values():
        data.append(item)
    responseitem = {"data" : data}
    return render(request, template_name='check_articles.html', context=responseitem)