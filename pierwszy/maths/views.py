from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from maths.lib import obliczenia
from maths.models import Math


def operacje(request, operacja, arg1, arg2):
    wynik = obliczenia(operacja, arg1, arg2)
    m = Math.objects.create(
        operation=operacja,
        arg1=arg1,
        arg2=arg2
    )
    m.save()
    return HttpResponse(wynik)
