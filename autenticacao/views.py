# utilitários para renderizar, redirecionar e responder
from django.shortcuts import render, HttpResponse, redirect

# arquivo externo para validar password
from .utils import password_is_valid

# model do django para criar usuários no admin
from django.contrib.auth.models import User

# modulos para tratar as mensagens de usuário
from django.contrib.messages import constants
from django.contrib import messages

# controla login, logout, se usuário existe no banco
from django.contrib import auth

# Create your views here.

def cadastro(request):
    if request.method == 'GET':
        # se já está autenticado não pode se cadastrar
        if request.user.is_autenticated:  
            return redirect('/')
        
        return render(request, 'cadastro.html')
    
    elif request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        email = request.POST.get('email')
    
        if not password_is_valid(request, senha, confirmar_senha):
            return redirect('/auth/cadastro')
        
        try:
            user = User.objects.create_user(username=usuario,
                                            email=email,
                                            password=senha,
                                            is_active=False)
            user.save()
            messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso!')
            return redirect('/auth/logar')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/auth/cadastro')



def login(request):
    if request.method == 'GET':
        # se ja está autenticado não pode acessar a página de login
        if request.user.is_autenticated: 
            return redirect('/') 
        
        return render(request, 'login.html')
    
    elif request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        usuario_existe = auth.authenticate(username=usuario, password=senha)

        if not usuario_existe:
            messages.add_message(request, constants.ERROR, 'Usuário ou Senha inválidos')
            return redirect('/auth/login')
        else:
            auth.login(request, usuario_existe)
            return redirect('/')

def sair(request):
    auth.logout(request)
    return redirect('/auth/login/')

