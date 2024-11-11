from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Welcome to the Home page!")

def hello_world(request):
    return render(request, 'hello_world.html')
