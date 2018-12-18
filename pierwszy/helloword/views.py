from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request):
    return HttpResponse("HelloWorld")

def hello_name(request, name, last_name=""):

    out = f"Hello {name}"
    if last_name:
        out += f" {last_name}"

    return HttpResponse(out)