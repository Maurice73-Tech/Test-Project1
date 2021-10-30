from django.shortcuts import render

from django.http import HttpResponse

from .models import Poll

def index(request):
    antwort = " "
    for umfrage in Poll.objects.all():
        serverantwort = serverantwort + "<br />"
        serverantwort += umfrage.name + " ("
        for antwortwortmoeglichkeit in umfrage.choice_set.all():
            serverantwort += antwortwortmoeglichkeit.name + " ,"
        serverantwort += ")"
    return HttpResponse("Hallo Welt!")
