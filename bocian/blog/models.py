from django.db import models


# Create your models here.

class TimestampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tag(models.Model):
    nazwa = models.CharField(max_length=200)

    def __str__(self):
       return self.nazwa

    class Meta:
        verbose_name_plural = "Tagi"


class Wpis(TimestampModel):
    tytul = models.CharField(max_length=200)
    tresc = models.TextField()
    tagi = models.ManyToManyField(Tag, blank=True)

    @property
    def czy_modyfikowany(self):
        if self.created < self.modified:
            return True

    def __str__(self):
        return f"id: {self.id} | {self.tytul}"

    class Meta:
        verbose_name_plural = "Wpisy"
