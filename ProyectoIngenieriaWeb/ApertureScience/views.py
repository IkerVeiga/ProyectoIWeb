from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.

def holaMundo(request):
    return HttpResponse("Hola Mundo")

# def experimentsList(request):
#     returnText = ""
#     for experiment in Experiment.objects.all():
#         returnText += experiment.__str__() + "\n"
#     return HttpResponse(returnText)
def index(request):
    return render(request, "index.html")


# def experimentDetail(request ,id):
#     experiment = Experiment.objects.get(id = id)
#     returnText = "Nombre: "+experiment.name + "\n\tDescripcion:" + experiment.description + "\n\tPorcentaje de exito: " + str(experiment.successRate) + "\n\tSujetos involucrado:"
#     for testSubject in experiment.testSubjects.all():
#         returnText+= "\n\t\t" + testSubject.name
#     returnText += "\n\tProducto:" + experiment.products.name
#     return HttpResponse(returnText)

def experimentsList(request):
    context = {"experiments":Experiment.objects.all}
    return render(request,"experimentList.html",context)

def experimentDetail(request ,id):
    experiment = Experiment.objects.get(id = id)
    context = {"experiment": experiment,
               "successPercentaje": experiment.successRate * 100}
    return render(request, "experimentDetail.html", context)

# def productsList(request):
#     returnText = ""
#     for product in Product.objects.all():
#         returnText += product.__str__() + "\n"
#     return HttpResponse(returnText)

def productsList(request):
    context = {"products":Product.objects.all}
    return render(request, "productList.html", context)

# def productDetail(request, id):
#     product = Product.objects.get(id = id)
#     returnText = "Nombre: " + product.name + "\n\tDescripcion: " + product.description + "\n\tPrecio: " + str(product.price) + "$" +"\n\tVersión: " + product.version

def productDetail(request, id):
    product = Product.objects.get(id = id)
    context = {"product": product}
    return render(request, "productDetail.html", context)

# def testSubjectsList(request):
#     returnText = ""
#     for testSubject in TestSubject.objects.all():
#         returnText += testSubject.__str__() + "\n"
#     return HttpResponse(returnText)

def testSubjectsList(request):
    context = {"testSubjects":TestSubject.objects.all}
    return render(request, "testSubjectList.html", context)

# def testSubjectDetail(request, number):
#     testSubject = TestSubject.objects.get(number = number)
#     returnText = "Nombre: "+testSubject.name + "\n\tApellido:" + testSubject.surname + "\n\tFecha de nacimiento: " + str(testSubject.birthdate) + "\n\tLugar de nacimiento: " + testSubject.birthplace

#     return HttpResponse(returnText)

def testSubjectDetail(request, number):
    testSubject = TestSubject.objects.get(number = number)
    # print("Primary key: "+ str(testSubject.pk) + " - Number : " + str(testSubject.number))
    context = {"testSubject": testSubject}
    return render(request, "testSubjectDetail.html", context)

