from django.shortcuts import render
from django.shortcuts import HttpResponse


def home(request):
    return HttpResponse("<h1>Home Pages</h1>")


def news(request):
    return HttpResponse("<h1>This is our lastest news</h1>")


def contact(request):
    return  HttpResponse("<h1>This is contact page</h2>")