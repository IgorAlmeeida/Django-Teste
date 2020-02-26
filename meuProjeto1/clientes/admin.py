from django.contrib import admin
from .models import Cliente, Departamento, CPF, Telefone
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Departamento)
admin.site.register(CPF)
admin.site.register(Telefone)