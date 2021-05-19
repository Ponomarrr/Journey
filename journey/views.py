from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    name = 'Are you ready to travel?!!!'
    return render(request, 'home.html', {'name': name})
