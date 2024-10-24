from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def holaMundo(request):
    return HttpResponse("Hola Mundo")
