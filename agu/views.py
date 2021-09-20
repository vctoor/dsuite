from django.http import HttpResponse
from django.shortcuts import render
name = 'Victor'

def home(request):
    return render(request, 'home.html', {'name' : name})
