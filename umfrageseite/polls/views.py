from django.shortcuts import render

from django.http import HttpResponse

from .models import Poll

def index(request):
    antwort = " "
    for umfrage in Poll.objects.all():
        antwort = antwort + "<br /> " + umfrage.name
    return HttpResponse("Hallo Welt!")
