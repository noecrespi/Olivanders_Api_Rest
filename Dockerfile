
# Lenguaje utilizado de la api 
FROM python:3.8-slim

# Puertos que usa la api rest
EXPOSE 5000/udp
EXPOSE 5000/tcp

# Crea la carpeta app
WORKDIR /app
# A partir de aqui puede ocasionar problemas

# Comando para actualizar el sistema apt :gestor de paquetes comprueba el paquete y si hay nuevas actualizciones
RUN apt update

# Si hay modicficaciones o actualizaciones lo ejecuta y lo actualiza
RUN apt upgrade -y

#Copia app
COPY . /app


# Inicializa el archivo requirements.txt que contiene todas las dependencias
RUN pip install -r requirements.txt

# Inicializar la app,podemos ver el funcionamineto 
ENTRYPOINT flask run --host=0.0.0.0 --port=5000
