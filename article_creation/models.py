from django.db import models

# Create your models here.


class Post(models.Model):

    title = models.CharField(max_length=255)
    body = models.TextField()
    article = models.TextField()
    created_at = models.DateTimeField()
    limit_date = models.DateTimeField()

    # def __str__(self):
    #     return self.title