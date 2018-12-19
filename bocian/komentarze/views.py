from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from komentarze.models import Komentarz


def dodaj_komentarz(request):
    if request.method == 'GET':
        return HttpResponse('Nic nie robie')
    else:
        nick = request.POST['nick']
        email = request.POST['email']
        tytul = request.POST['tytul']
        tresc = request.POST['tresc']
        create_data = request.POST['create_date']
        komentarz = Komentarz(nick=nick, email=email, tytul=tytul, tresc=tresc, create_data=create_data)
        komentarz.save()
    return HttpResponse('dodane')
