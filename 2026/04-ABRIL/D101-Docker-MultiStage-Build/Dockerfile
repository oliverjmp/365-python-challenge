# --- ETAPA 1: Constructor / Compilación ---
FROM python:3.11-slim AS builder

WORKDIR /app

# Instalar dependencias del sistema necesarias para compilaciones si aplica
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependencias de Python en un directorio local (/install)
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# --- ETAPA 2: Imagen Final de Producción (Ligera) ---
FROM python:3.11-slim AS runner

WORKDIR /app

# Copiar solo las librerías instaladas desde la etapa de construcción
COPY --from=builder /install /usr/local

# Copiar el código fuente de la aplicación
COPY ./src ./src

# Exponer el puerto del microservicio
EXPOSE 8000

# Comando por defecto para arrancar la aplicación con Uvicorn
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]