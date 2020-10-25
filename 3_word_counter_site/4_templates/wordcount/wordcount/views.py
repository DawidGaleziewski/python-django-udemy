from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'greet': "motherfucker"})


def eggs(request):
    return HttpResponse('Eggs')