
from django.http.response import Http404


class Post():

    POSTS = [
    {'id':1,'title':'First article','body':'This is the first article'},
    {'id':2,'title':'Second article','body':'This is the second article'},
    {'id':3,'title':'Third article','body':'This is the third article'},
    ]    

    @classmethod
    def all(cls):

        return cls.POSTS



    @classmethod
    def find(cls, id):

        try:
            return cls.POSTS[int(id) - 1]
            
        except:
            raise Http404(f"Sorry, post #{id} not found")
