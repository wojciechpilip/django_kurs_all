from django.core.paginator import Paginator
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template import Template, Context, loader

from .models import Wpis, Tag
from comments.models import Komentarz

# Create your views here.

def index(request):
    order_param = request.GET.get('orderby')
    if order_param in ['created', 'id', 'modified', 'tagi', 'tresc', 'tytul']:
        wpisy = Wpis.objects.all().order_by(order_param)
    else:
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

    if request.method == 'POST':
        return HttpResponse("Na razie nie umiem dodać.")
    wpis = Wpis.objects.get(pk=id_wpisu)
    tagi = wpis.tagi.all()
    wpisy = Wpis.objects.all()

    paginator = Paginator(wpisy, 20)  # pokaż 1 wpisie na stronie
    page = request.GET.get('page')
    wpisy = paginator.get_page(page)

    return render(
        request=request,
        template_name='blog/index.html',
        context={
            'wybrany_wpis': wpis,
            'wpisy': wpisy,
            'page': page,
            'tagi': tagi,

        }
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


def wpisy_taga(request, nazwa_taga):
    #tag = Tag.objects.get(nazwa=nazwa_taga)
    # try:
    #     tag = Tag.objects.get(nazwa=nazwa_taga)
    # except Tag.DoesNotExist:
    #     raise Http404

    tag = get_object_or_404(Tag, nazwa=nazwa_taga)

    wpisy = tag.wpis_set.all()

    context = {

        'wpisy': wpisy,
        'tag': tag
    }

    return render(
        request=request,
        template_name='blog/wpisy_po_tagu.html',
        context=context
    )