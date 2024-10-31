from django.urls import path
from . import views

urlpatterns = [
    path('', views.holaMundo, name='holaMundo'),
    path('experimentos', views.experimentsList,name="experimentosLista"),
    path('experimentos/<int:id>', views.experimentDetail, name = "experimentDetail" ),
    path('Products', views.productsList, name = "productsList"),
    path('Products/<int:id>', views.productDetail, name = "productDetail")
]