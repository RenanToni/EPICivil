from django.shortcuts import render

colaboradores = [
        {"nome": "Joaquim"},
        {"cpf": "543.321.156.23"},
        {"cargo": "servente"},
        {"telefone": "(49) 91359-1461"},
    ]
def home(request):
    
    return render(request, 'myapp/globals/home.html')

def cadastrar(request):
    return render(request, 'myapp/globals/cadastrar.html')

def atualizar(request):
    return render(request, 'myapp/globals/atualizar.html')

def colaboradores (request):

    contexto = {'colaboradores': colaboradores}
    return render(request, 'myapp/globals/colaboradores.html')
    

