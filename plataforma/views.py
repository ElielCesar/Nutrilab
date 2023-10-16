# Utilitários para renderizar, responder e redirecionar
from datetime import datetime
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404

# verifica se o usuário está logado no sistema
from django.contrib.auth.decorators import login_required

# controla as mensagens para os usuarios
from django.contrib import messages
from django.contrib.messages import constants

# models utilizados nas vies
from .models import Pacientes, DadosPaciente

# vai desabilitar o csrf para os gráficos
from django.views.decorators.csrf import csrf_exempt

# importar Json para retornar para os gráficos
from django.http import JsonResponse

# Create your views here.
@login_required(login_url='/auth/logar/')
def pacientes(request):
    if request.method == 'GET':
        todos_pacientes = Pacientes.objects.filter(nutri=request.user)
        return render(request, 'pacientes.html', {'todos_pacientes':todos_pacientes})
    
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        sexo = request.POST.get('sexo')
        idade = request.POST.get('idade')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')

        if (len(nome.strip()) == 0) or  \
           (len(sexo.strip()) == 0) or  \
           (len(idade.strip()) == 0) or \
           (len(email.strip()) == 0) or \
           (len(telefone.strip()) == 0):
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/pacientes/')

        if not idade.isnumeric():
            messages.add_message(request, constants.ERROR, 'Digite uma idade válida')
            return redirect('/pacientes/')

        pacientes = Pacientes.objects.filter(email=email)

        if pacientes.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um paciente com esse E-mail')
            return redirect('/pacientes/')
        
        try:
            paciente_add = Pacientes(
                nome=nome,
                sexo=sexo,
                idade=idade,
                email=email,
                telefone=telefone,
                nutri= request.user,
            )
            paciente_add.save()
            messages.add_message(request, constants.SUCCESS, 'Paciente cadastrado com sucesso!')
            return redirect('/pacientes/')
        
        except:
             messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
             return redirect('/pacientes/')
        

@login_required(login_url='/auth/logar/')
def dados_paciente_listar(request):
    if request.method == "GET":
        todos_pacientes = Pacientes.objects.filter(nutri=request.user)
        return render(request, 'dados_paciente_listar.html', {'todos_pacientes': todos_pacientes})


@login_required(login_url='/auth/logar/')
def dados_paciente(request, id):
    paciente = get_object_or_404(Pacientes, id=id)
    if not paciente.nutri == request.user:
        messages.add_message(request, constants.ERROR, 'Esse paciente não é seu')
        return redirect('/dados_paciente/')

    if request.method == 'GET':
        dados_paciente = DadosPaciente.objects.filter(paciente=paciente)
        return render(request, 'dados_paciente.html', {'paciente':paciente, 'dados_paciente':dados_paciente})
    
    elif request.method == 'POST':
        peso = request.POST.get('peso')
        altura = request.POST.get('altura')
        gordura = request.POST.get('gordura')
        musculo = request.POST.get('musculo')
        hdl = request.POST.get('hdl')
        ldl = request.POST.get('ldl')
        colesterol_total = request.POST.get('ctotal')
        triglicerídios = request.POST.get('triglicerídios')

        paciente_add = DadosPaciente(
            paciente=paciente,
            data=datetime.now(),
            peso=peso,
            altura=altura,
            percentual_gordura=gordura,
            percentual_musculo=musculo,
            colesterol_hdl=hdl,
            colesterol_ldl=ldl,
            colesterol_total=colesterol_total,
            trigliceridios=triglicerídios)

        paciente_add.save()

        messages.add_message(request, constants.SUCCESS, 'Dados cadastrado com sucesso')

        return redirect('/dados_paciente/')


'''aqui vai ser uma espécie de "API" que vai trazer os dados
para o gráfico'''
@login_required(login_url='/auth/logar/')
@csrf_exempt
def grafico_peso(request, id):
    paciente = Pacientes.objects.get(id=id)
    dados = DadosPaciente.objects.filter(paciente=paciente).order_by("-data")
    
    pesos = [dado.peso for dado in dados]
    labels = [dado.data for dado in dados]
    data = {'peso': pesos,
            'labels': labels}
    return JsonResponse(data)