from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template import Template, Context, loader

from django import forms

from comments.forms import FormKomentarz, FormKomentarz2
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
    errors = ""
    wpis = Wpis.objects.get(pk=id_wpisu)
    if request.method == 'POST':
        komentarz = Komentarz()
        komentarz.tytul = request.POST['tytul']
        komentarz.nick = request.POST['nick']
        komentarz.email = request.POST['email']
        komentarz.tresc = request.POST['tresc']
        komentarz.wpis_id = wpis.id
        try:
            komentarz.clean_fields()
            komentarz.save()
        except ValidationError as e:
            errors = e

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
            'errors': errors

        }
    )

def details_with_form(request, id_wpisu):
    errors = ""
    wpis = Wpis.objects.get(pk=id_wpisu)
    if request.method == 'POST':
        form = FormKomentarz(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.wpis_id = wpis.id
            obj.save()
    else:
        form = FormKomentarz()

    tagi = wpis.tagi.all()
    wpisy = Wpis.objects.all()

    paginator = Paginator(wpisy, 20)  # pokaż 1 wpisie na stronie
    page = request.GET.get('page')
    wpisy = paginator.get_page(page)

    return render(
        request=request,
        template_name='blog/index2.html',
        context={
            'wybrany_wpis': wpis,
            'wpisy': wpisy,
            'page': page,
            'tagi': tagi,
            'form': form,
            'errors': errors

        }
    )

def details_with_form_model_form(request, id_wpisu):
    errors = ""
    wpis = Wpis.objects.get(pk=id_wpisu)
    if request.method == 'POST':
        form = FormKomentarz2(request.POST)
        data = form.data
        data['wpis_id'] = wpis.id
        komentarz = Komentarz(data)
        komentarz.save()
    else:
        form = FormKomentarz2()

    tagi = wpis.tagi.all()
    wpisy = Wpis.objects.all()

    paginator = Paginator(wpisy, 20)  # pokaż 1 wpisie na stronie
    page = request.GET.get('page')
    wpisy = paginator.get_page(page)

    return render(
        request=request,
        template_name='blog/index2.html',
        context={
            'wybrany_wpis': wpis,
            'wpisy': wpisy,
            'page': page,
            'tagi': tagi,
            'form': form,
            'errors': errors

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