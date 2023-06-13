# Puxe a imagem base
FROM python:3.9

# Instale o utilitário crontab
RUN apt-get update && apt-get install -y cron

# Definir variáveis ​​de ambiente
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_ROOT_USER_ACTION=ignore

# Definir diretório de trabalho
WORKDIR /code

# Copia dos arquivos
COPY . /code

# Instalação das dependencias
RUN pip install -r requirements.txt && python manage.py migrate && python manage.py crontab add

# Expor a porta 
EXPOSE 8080

# Comando que rodara na imagem
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]

