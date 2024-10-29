from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.

def holaMundo(request):
    return HttpResponse("Hola Mundo")

def experimentsList(request):
    returnText = ""
    for experiment in Experiment.objects.all():
        returnText += experiment + "\n"
        