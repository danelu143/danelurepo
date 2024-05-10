from django.shortcuts import render
from django.http import HttpResponse
import datetime
def first(request):
    return HttpResponse("<h1> This is First App</h1>")
def second(request):
    return HttpResponse("<H1> This is Second App</h1>")
def third(request):
    return HttpResponse("<h1> This is Third App "+str(datetime.datetime.now())+"</h1>")
