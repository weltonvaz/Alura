from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse('Bem Vindo ao Django')
    return render(request, 'index.html')

def perfis(request):
    return render(request, 'perfil.html')