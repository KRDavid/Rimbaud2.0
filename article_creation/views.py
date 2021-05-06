from django.shortcuts import render

# Create your views here.

def index(request):

    posts = [
        {'id':1,'title':'First article','body':'This is the first article'},
        {'id':2,'title':'Second article','body':'This is the second article'},
        {'id':3,'title':'Third article','body':'This is the third article'},
    ]
    return render(request,'index.html', {'posts':posts})