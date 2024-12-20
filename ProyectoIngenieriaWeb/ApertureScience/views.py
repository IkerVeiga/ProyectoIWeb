from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView

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

class ExperimentsList(ListView):
	model = Experiment
	template_name = 'experimentList.html'
	context_object_name = 'experiments'
	queryset = Experiment.objects.order_by('name')


class ExperimentDetail(DetailView):
    model = Experiment
    template_name = 'experimentDetail.html'
    context_object_name = 'experiment'

    def get_context_data(self, **kwargs):
        # Cargar el contexto base
        context = super().get_context_data(**kwargs)
        # Añadir un listado de departamentos
        context['successPercentaje'] = self.get_object().successRate * 100
        return context

class ProductsList(ListView):
    model = Product
    template_name = 'productList.html'
    context_object_name = 'products'
    queryset = Product.objects.order_by('name')

class ProductDetail(DetailView):
    model = Product
    template_name = 'productDetail.html'
    context_object_name = 'product'

class TestSubjectsList(ListView):
    model = TestSubject
    template_name = 'testSubjectList.html'
    context_object_name = 'testSubjects'
    queryset = TestSubject.objects.order_by('number')

class TestSubjectDetail(DetailView):
    model = TestSubject
    template_name = 'testSubjectDetail.html'
    context_object_name = 'testSubject'

def newPost(request):
    if (request.method == "POST"):
        #print(request.POST["name"])
        from django.utils import timezone
        post = Post(creatorName = request.POST["name"], title = request.POST["title"], message = request.POST["message"], publicationDate = timezone.now())
        post.save()
        context = {'post': post}
        return render(request, "post.html", context)
    if (request.method == "GET"):
        context = {'posts' : Post.objects.all().order_by('publicationDate')}
        # print(Post.objects.all()[1].date)
        return render(request, "posts.html", context)
