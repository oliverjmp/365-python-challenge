# D215 - FastAPI Streaming Parquet Response

Servicio web optimizado para la descarga directa y fluida de grandes ficheros **Apache Parquet** utilizando **FastAPI StreamingResponse**.

## 🏛️ Estructura del Proyecto

D215-FastAPI-Streaming-Parquet-Response/
├── .coveragerc            # Configuración de cobertura estricta (fail_under = 100)
├── docs/
│   ├── index.md           # Documentación técnica del hito
│   └── architecture.md    # Arquitectura y diagrama de flujo
├── src/
│   ├── __init__.py
│   └── streaming_api.py   # Lógica del servidor FastAPI y chunks de streaming
├── tests/
│   ├── __init__.py
│   └── test_api.py        # Pruebas unitarias estrictas con pytest (100% Cobertura)
├── main.py                # Script CLI de validación de llamadas HTTP
├── mkdocs.yml             # Configuración del portal web corporativo
├── requirements.txt       # Dependencias del proyecto
└── README.md              # Documentación principal

## 💼 Casos Prácticos de Uso

1. **Exportación de Reportes Masivos en Data Lakes:**
   - Permite a los usuarios o sistemas analíticos descargar ficheros Parquet de gran tamaño (cientos de megabytes o gigabytes) bajo demanda sin agotar la memoria RAM del servidor web.
2. **Transferencias Eficientes en Arquitecturas Cloud / Microservicios:**
   - Facilita el intercambio rápido de datasets tabulares comprimidos entre servicios distribuidos mediante transferencia basada en bloques (*chunks*) de bytes por HTTP.
3. **Optimización de Ancho de Banda y Latencia:**
   - Reduce el tiempo de respuesta inicial (*Time to First Byte*) al comenzar a transmitir los datos de forma fluida e inmediata conforme se van leyendo del almacenamiento.

## 🚀 Comandos de Ejecución

- **Instalar dependencias:**
  `pip install -r requirements.txt`

- **Ejecutar pruebas unitarias (con cobertura al 100%):**
  `python -m pytest --cov=src --cov-fail-under=100 --cov-report=term-missing --cache-clear`

- **Ejecutar script CLI de validación:**
  `python main.py`

- **Levantar servidor local de la API:**
  `uvicorn src.streaming_api:app --reload`

- **Servir documentación técnica:**
  `mkdocs serve`