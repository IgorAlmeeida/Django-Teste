from django.db import models

# Create your models here.

class Cliente (models.Model):
    name = models.CharField(max_length=200, blank= False, null=False)
    endereco = models.CharField(max_length=200, blank= False, null= False)
    salario = models.DecimalField(max_digits=8,decimal_places=2)
    idade = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name