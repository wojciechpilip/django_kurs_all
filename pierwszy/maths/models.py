from django.db import models

# Create your models here.

class Math(models.Model):

    operation = models.CharField(max_length=3)
    arg1 = models.IntegerField()
    arg2 = models.IntegerField()

