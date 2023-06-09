from rest_framework import serializers
from bancos.models import * 

class BancoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banco
        fields = ['ispb','nome_reduzido','numero_codigo','participante_compensacao','acesso_principal','nome_extenso','inicio_operacao']