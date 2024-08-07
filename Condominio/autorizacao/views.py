from django.shortcuts import render
from django.http import HttpResponse
from  django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import condominio_tabela

def autorizar(request):
    return render(request, 'autorizacao.html')

def listar_condominios(request):
    if request.method == "GET":
        dados = condominio_tabela.objects.all()

    return render(request, 'autorizacao.html', {'dados': dados})    