from django.http import HttpResponse

def home (request):
    return HttpResponse ('Olá mundo')

def clientes (request):
    return HttpResponse ('Maria, José, João')

def cliente_num (request, id):
    return HttpResponse(id)

def cliente_nome(request, nome):
    return HttpResponse(nome)