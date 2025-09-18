# Imagen base de Python
FROM python:3.11-slim

# Setear directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema necesarias para psycopg2 y compilaciones
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar dependencias de Python
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código del proyecto
COPY . .

# Exponer el puerto en el que corre Gunicorn
EXPOSE 8000

# Comando para levantar la app con Gunicorn
CMD ["gunicorn", "ecom.wsgi:application", "--bind", "0.0.0.0:8000"]
