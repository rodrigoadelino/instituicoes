from django.contrib import admin
from bancos.models import *

class Bancos(admin.ModelAdmin):
    list_display = ('id','ispb','nome_reduzido','numero_codigo','participante_compensacao','acesso_principal','nome_extenso','inicio_operacao')
    list_display_links = ('id', 'nome_reduzido')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Banco,Bancos)