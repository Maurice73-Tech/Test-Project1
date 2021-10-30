from django.urls import path

from .views import index

urlpattern = [
    # hey, wenn eine Anfrage an reinkommt, dann überge dass der Funktion 
    # index aus der view.py
    path('', index)
]