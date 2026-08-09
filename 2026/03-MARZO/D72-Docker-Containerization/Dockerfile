# ==========================================
# ETAPA 1: Constructor y dependencias
# ==========================================
FROM python:3.13-slim AS builder

WORKDIR /app

# Instalar dependencias del sistema necesarias si hay compilaciones
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependencias de Python en un directorio local (/install)
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ==========================================
# ETAPA 2: Imagen final limpia y ligera
# ==========================================
FROM python:3.13-slim AS final

WORKDIR /app

# Copiar solo las librerías de Python ya instaladas desde la etapa de construcción
COPY --from=builder /install /usr/local

# Copiar el código fuente del microservicio
COPY src/ ./src/

# Comando por defecto para ejecutar pruebas o el microservicio
CMD ["python", "-m", "src.analyzer"]