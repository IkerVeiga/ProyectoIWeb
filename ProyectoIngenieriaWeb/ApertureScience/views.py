from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.

def holaMundo(request):
    return HttpResponse("Hola Mundo")

def experimentsList(request):
    returnText = ""
    for experiment in Experiment.objects.all():
        returnText += experiment.__str__() + "\n"
    return HttpResponse(returnText)

def experimentDetail(request ,id):
    experiment = Experiment.objects.get(id = id)
    returnText = "Nombre: "+experiment.name + "\n\tDescripccion:" + experiment.description + "\n\tPorcentaje de exito: " + str(experiment.successRate) + "\n\tSujetos involucrado:"
    for testSubject in experiment.testSubjects.all():
        returnText+= "\n\t\t" + testSubject.name
    returnText += "\n\tProducto:" + experiment.products.name
    return HttpResponse(returnText)