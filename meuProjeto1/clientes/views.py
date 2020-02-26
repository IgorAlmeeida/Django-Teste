from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def clientes (request):
    return HttpResponse ('Maria, José, João')

def cliente_num (request, id):
    return HttpResponse(id)

def cliente_nome(request, nome):
    return HttpResponse(nome)