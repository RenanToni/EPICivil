from django.shortcuts import render
def home(request):
    return render(request, 'myapp/globals/home.html')

def cadastrar(request):
    return render(request, 'myapp/globals/cadastrar.html')

def atualizar(request):
    return render(request, 'myapp/globals/atualizar.html')

def usuarios (request):
    return render(request, 'myapp/globals/usuarios.html')

