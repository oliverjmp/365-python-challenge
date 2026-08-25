# --- Etapa 1: Construcción e instalación de dependencias ---
FROM python:3.11-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# --- Etapa 2: Imagen final ligera para producción ---
FROM python:3.11-slim AS runner

WORKDIR /app

# Copiar dependencias instaladas desde el builder
COPY --from=builder /root/.local /root/.local
COPY --from=builder /app/requirements.txt .

# Copiar el código fuente del proyecto
COPY . /app

# Asegurar que los ejecutables de Python estén en el PATH
ENV PATH=/root/.local/bin:$PATH

EXPOSE 8501

CMD ["python", "main.py"]