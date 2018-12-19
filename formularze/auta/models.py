from django.db import models

# Create your models here.

class Auto(models.Model):

    marka = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
        # wpis = models.ForeignKey(Wpis, on_delete=models)