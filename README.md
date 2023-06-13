## Setup Manual Linux
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