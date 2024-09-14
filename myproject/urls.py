from django.urls import path
from myproject.views import home, cadastrar, atualizar, colaboradores

urlpatterns = [
    path('', home),
    path('cadastrar/', cadastrar),
    path('atualizar/', atualizar),
    path('colaboradores/', colaboradores),
]
