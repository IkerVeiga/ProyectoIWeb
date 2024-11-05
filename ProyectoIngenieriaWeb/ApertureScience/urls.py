from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('experiments', views.experimentsList,name="experimentosLista"),
    path('experiments/<int:id>', views.experimentDetail, name = "experimentDetail" ),
    path('products', views.productsList, name = "productsList"),
    path('products/<int:id>', views.productDetail, name = "productDetail"),
    path('testSubjects', views.testSubjectsList, name = "testSubjectsList"),
    path('testSubjects/<int:number>', views.testSubjectDetail, name = "testSubjectDetail"),
]