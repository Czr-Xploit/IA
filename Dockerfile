# Usar una imagen base de Python 3.9
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar todos los archivos de la app al contenedor
COPY . /app

# Instalar las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto 5005 (puerto por defecto de Rasa)
EXPOSE 5005

# Comando para iniciar Rasa con la API habilitada
CMD ["rasa", "run", "--enable-api", "--cors", "*"]
FROM rasa/rasa:latest

# Copiar los archivos de tu proyecto
COPY . /app

# Instalar dependencias adicionales
RUN pip install -r /app/requirements.txt

# Comando para iniciar Rasa
CMD ["rasa", "run", "--model", "models/"]
