from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
def Home(request):
    return HttpResponse("<h1>This our home page</h1>")

def News(request):
    return HttpResponse("<h1>This is our lastets news</h1>")

def Contact(request):
    return HttpResponse("<h1>This is contact us page</h1>")