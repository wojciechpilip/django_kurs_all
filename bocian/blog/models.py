from django.db import models

# Create your models here.

class Wpis(models.Model):

    tytul = models.CharField(max_length=200)
    tresc = models.TextField()

    def __str__(self):
        return f"id: {self.id} | {self.tytul}"