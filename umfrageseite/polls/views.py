from django.shortcuts import render

from django.http import HttpResponse

from .models import Poll

def index(request):
    context = {'umfragen': Poll.objects.all(), 'titel': "Umfrageseite"}
    return render(request=request, template_name='polls/index.html',
                context=context)
