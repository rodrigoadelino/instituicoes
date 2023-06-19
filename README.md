# API contendo os bancos que operam no Brasil
O propósito desta API e trazer uma lista atualizada dos bancos que operam no Brasil.
Esta API disponibiliza as seguintes informações bancarias: ispb, nome_reduzido, numero_codigo, participante_compensacao, acesso_principal, nome_extenso, inicio_operacao.
Essas informações são atualizadas atraves do arquivo .csv disponibilizada pelo Bacen. 

### Testar a API
``` https://rodrigobonfim.pythonanywhere.com/api/bancos/
```

### Pré-requisitos
``` Python 3.9.x
```

### Setup Manual Linux
- Criar o ambiente virtual dev na pasta do projeto```python3.9 -m venv dev```
- Ativar o ambiente virtual ```source dev/bin/activate```
- Instalar as bibliotecas necessárias ```pip install -r requirements.txt```
- Criar Banco de dados ```python3.9 manage.py migrate```
- Criar usuario Admin ```python3.9 manage.py createsuperuser```
- subir o servidor local ```python3.9 manage.py runserver```
- A aplicação ficará disponivel em ```http://127.0.0.1:8000/api```

## Comandos Úteis 
- Parar o servidor local ```Ctrl + C```
- Desativar ambiente virtual(Linux) ```deactivate```

## Setup Docker 
docker build -t apibancos:1.0 .