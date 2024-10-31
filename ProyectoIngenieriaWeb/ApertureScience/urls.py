from django.urls import path
from . import views

urlpatterns = [
    path('', views.holaMundo, name='holaMundo'),
    path('experiments', views.experimentsList,name="experimentosLista"),
    path('experiments/<int:id>', views.experimentDetail, name = "experimentDetail" ),
    path('products', views.productsList, name = "productsList"),
    path('products/<int:id>', views.productDetail, name = "productDetail"),
    path('subjects', views.testSubjectsList, name = "testSubjectsList"),
    path('subjects/<int:number>', views.testSubjectDetail, name = "testSubjectDetail"),
]