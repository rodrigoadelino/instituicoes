from django.db import models

class Banco(models.Model):
    ispb = models.CharField(max_length=10)
    nome_reduzido = models.CharField(max_length=30)
    numero_codigo = models.CharField(max_length=4, blank=True, null=True, default='')
    participante_compensacao = models.CharField(max_length=4)
    acesso_principal = models.CharField(max_length=4)
    nome_extenso = models.CharField(max_length=100)
    inicio_operacao = models.CharField(max_length=30)

    def __str__(self):
        return self.nome_reduzido
