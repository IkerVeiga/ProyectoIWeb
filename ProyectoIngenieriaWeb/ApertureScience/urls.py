from django.urls import path
from . import views

urlpatterns = [
    path('', views.holaMundo, name='holaMundo'),
    path('experimentos', views.experimentsList,name="experimentosLista"),
    path('experimentos/<int:id>', views.experimentDetail, name = "experimentDetail" ),
    path('sujetos', views.testSubjectsList, name = "testSubjectsList"),
    path('sujetos/<int:number>', views.testSubjectDetail, name = "testSubjectDetail"),
]