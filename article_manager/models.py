from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    article = models.CharField(max_length=5000)
    date_limite = models.DateField()
    admin_only = models.BooleanField()

