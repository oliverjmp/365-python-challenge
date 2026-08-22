# Imagen base oficial de Python liviana
FROM python:3.11-slim

# Establecer directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalar dependencias del sistema necesarias para compilaciones si aplica
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copiar e instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente y scripts
COPY src/ ./src/
COPY run_service.py .

# Exponer puerto predeterminado (opcional para microservicios web futuros)
EXPOSE 8000

# Comando por defecto para ejecutar el microservicio
CMD ["python", "run_service.py"]