from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from auta.models import Auto


def dodaj(request):

    if request.method == 'GET':
        return HttpResponse("A ja sobie tu po prostu siedzę")
    elif request.method == "POST":

        marka = request.POST['marka']
        model = request.POST['model']
        auto = Auto(
            marka=marka,
            model=model
        )
        auto.save()
    return HttpResponse('dodane')