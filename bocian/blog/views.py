from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context, loader

from .models import Wpis


# Create your views here.

def index(request):
    wpisy = Wpis.objects.all()
    wybrany_wpis = wpisy.first()

    paginator = Paginator(wpisy, 20)  # pokaż 1 wpisie na stronie
    page = request.GET.get('page')
    wpisy = paginator.get_page(page)
    context = {
        'wpisy': wpisy,
        'wybrany_wpis': wybrany_wpis

    }
    return render(
        request=request,
        template_name='blog/index.html',
        context=context
    )


def details(request, id_wpisu):
    wpis = Wpis.objects.get(pk=id_wpisu)

    return render(
        request=request,
        template_name='blog/index.html',
        context={'wybrany_wpis': wpis}
    )




# def index_temp(request):
#     ostatni_wpis = Wpis.objects.last()
#     t = loader.get_template('blog/index.html')
#     liczby = [x for x in range(10)]
#     context = {
#         'chleb': '1,90',
#         'woda': 2.5,
#         'wpis': ostatni_wpis,
#         'liczby': liczby
#     }
#     wynik = t.render(context)
#     return HttpResponse(wynik)


def index_temp(request):
    ostatni_wpis = Wpis.objects.last()

    liczby = [x for x in range(10)]

    context = {
        'chleb': '1,90',
        'woda': 2.5,
        'wpis': ostatni_wpis,
        'liczby': liczby
    }

    return render(
        request=request,
        template_name='blog/index.html',
        context=context
    )
