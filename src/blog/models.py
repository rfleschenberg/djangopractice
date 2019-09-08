from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateField(auto_now=True)

    def get_absolute_url(self):
        return reverse('articles:article-detail', kwargs={'id': self.id})

class Comment(models.Model):
    author = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateField(auto_now=True)
    post_id = models.IntegerField(default=2)