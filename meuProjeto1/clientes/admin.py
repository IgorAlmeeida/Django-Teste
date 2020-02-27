from django.contrib import admin
from .models import Cliente, Departamento, CPF, Telefone
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    fields = ('name','endereco','salario','idade','email','cpf')
    list_display = ('name', 'cpf', 'email')
    list_filter = ('departamento',)
    search_fields = ('name', 'cpf', 'email', 'departamento')

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Departamento)
admin.site.register(CPF)
admin.site.register(Telefone)