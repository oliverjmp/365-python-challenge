# Etapa 1: Constructor / Compilación de dependencias
FROM python:3.11-slim AS builder

WORKDIR /app

# Instalar herramientas de compilación del sistema si se requieren
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Instalar dependencias en una ruta prefijada para aislarlas
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Etapa 2: Imagen final limpia y ligera
FROM python:3.11-slim

WORKDIR /app

# Instalar libreria cliente de postgres en runtime
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

# Copiar las librerías instaladas desde la etapa de construcción
COPY --from=builder /install /usr/local

# Copiar el código fuente de la aplicación
COPY ./src ./src

EXPOSE 8000

# Comando por defecto para arrancar Uvicorn
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]