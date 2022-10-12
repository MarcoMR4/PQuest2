

from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('registro/', views.registro, name="registro"),
    path('inicioSesion/', views.signin, name="inicioSesion"),
    path('logout/', views.signout, name='logout'),
    path('catalogo/', views.catalogo, name="catalogoMas"),
     path('registroMascota/', views.registroMascota, name="registroMas"),
    
]