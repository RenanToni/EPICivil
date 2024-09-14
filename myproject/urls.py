from django.urls import path
from myproject.views import home, cadastrar, atualizar, usuarios

urlpatterns = [
    path('', home),
    path('cadastrar/', cadastrar),
    path('atualizar/', atualizar),
    path('usuarios/', usuarios),
]
