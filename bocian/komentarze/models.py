from django.db import models

from blog.models import Wpis


class Komentarz(models.Model):
    nick = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    tytul = models.CharField(max_length=50)
    tresc = models.TextField()
    create_data = models.DateTimeField(auto_now_add=True)
    wpis = models.ForeignKey(Wpis, on_delete=models.CASCADE)
