import urllib.request
import pandas as pd
from django.db import connection
import os
import django


def my_scheduled_job():
  print('Iniciando')
  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "listabancos.settings")
  django.setup()

  url = "http://www.bcb.gov.br/pom/spb/estatistica/port/ParticipantesSTRport.csv"
  nome_arquivo = "instituicoes.csv"

  urllib.request.urlretrieve(url, nome_arquivo)

  df = pd.read_csv('instituicoes.csv', header=None)

  # Convertendo o DataFrame em uma lista de dicionários
  dados = df.to_dict('records')[1:]  # Ignorando a primeira linha

  # Obtendo o cursor do banco de dados
  cursor = connection.cursor()

  # Executando as inserções no banco de dados
  for dado in dados:
      # Verificar se os dados já existem no banco de dados
      cursor.execute("SELECT COUNT(*) FROM bancos_banco WHERE ispb = %s AND nome_reduzido = %s",
                    (dado[0], dado[1]))
      result = cursor.fetchone()

      if result[0] == 0:
          # Os dados não existem, então realizar a inserção
          cursor.execute("INSERT INTO bancos_banco (ispb, nome_reduzido, numero_codigo, participante_compensacao, acesso_principal, nome_extenso, inicio_operacao) \
                        VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        (dado[0], (dado[1].strip()), dado[2], dado[3], dado[4], dado[5], dado[6]))

  # Salvando as alterações
  connection.commit()

  # Fechando o cursor
  cursor.close()

  # Apagar o arquivo utilizado
  os.remove('instituicoes.csv')

  print('Finalizado')
