from django.urls import path

from .views import index

app_name = 'polls'
urlpatterns = [
    # hey, wenn eine Anfrage an reinkommt, dann überge dass der Funktion 
    # index aus der view.py
    path('', index),
]