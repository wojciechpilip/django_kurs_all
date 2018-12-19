from django.db import models

# Create your models here.
# from blog.models import Wpis


class Komentarz(models.Model):
    nick = models.CharField(max_length=100)
    email = models.EmailField()
    tytul = models.CharField(max_length=200)
    tresc = models.TextField()
    wpis = models.ForeignKey('blog.Wpis', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
