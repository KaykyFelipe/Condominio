from django.shortcuts import render
from django.http import HttpResponse
from  django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect


def autorizar(request):
    return render(request, 'autorizacao.html')