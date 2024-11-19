from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('experiments', views.ExperimentsList.as_view(),name="experimentosLista"),
    path('experiments/<int:pk>', views.ExperimentDetail.as_view(), name = "experimentDetail" ),
    path('products', views.ProductsList.as_view(), name = "productsList"),
    path('products/<int:pk>', views.ProductDetail.as_view(), name = "productDetail"),
    path('testSubjects', views.TestSubjectsList.as_view(), name = "testSubjectsList"),
    path('testSubjects/<int:pk>', views.TestSubjectDetail.as_view(), name = "testSubjectDetail"),
]