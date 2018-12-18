from django.db import models

# Create your models here.

class TimestampModel(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract= True

class Wpis(TimestampModel):

    tytul = models.CharField(max_length=200)
    tresc = models.TextField()

    @property
    def czy_modyfikowany(self):
        if self.created < self.modified:
            return True

    def __str__(self):
        return f"id: {self.id} | {self.tytul}"

    class Meta:
        verbose_name_plural = "Wpisy"