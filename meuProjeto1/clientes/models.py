from django.db import models

# Create your models here.


class CPF (models.Model):
    numero = models.CharField(max_length=11, null= False, blank= False)
    data_exp = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.numero

class Departamento(models.Model):
    name = models.CharField(max_length = 50, blank=False, null = False)

    def __str__(self):
        return self.name
    
class Cliente (models.Model):
    name = models.CharField(max_length=200, blank= True, null=True)
    endereco = models.CharField(max_length=200, blank= False, null= False)
    salario = models.DecimalField(max_digits=8,decimal_places=2)
    idade = models.IntegerField()
    email = models.EmailField()
    cpf = models.OneToOneField('CPF', on_delete = models.CASCADE)
    departamento = models.ManyToManyField('Departamento')
   
    def __str__(self):
        return self.name

class Telefone(models.Model):
    numero = models.CharField(max_length=20)
    descricao = models.CharField(max_length=80)

    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)

    def __str__(self):
        return self.numero + " - " + self.descricao