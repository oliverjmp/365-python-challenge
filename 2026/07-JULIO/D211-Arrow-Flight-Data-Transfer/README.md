# D211 - Arrow Flight Data Transfer

Transferencia ultrarrápida de datasets distribuidos y optimizados en memoria mediante el protocolo **Apache Flight** y Python.

## 🏛️ Estructura del Proyecto

D211-Arrow-Flight-Data-Transfer/
├── .coveragerc            # Configuración de políticas estrictas de cobertura (fail_under = 100)
├── docs/
│   ├── index.md           # Página principal de documentación técnica del hito
│   └── architecture.md    # Arquitectura detallada del protocolo Flight y gRPC
├── src/
│   ├── __init__.py
│   └── flight_server.py   # Implementación del servidor y gestión de streams Arrow
├── tests/
│   ├── __init__.py
│   └── test_flight.py     # Pruebas unitarias estrictas con pytest y 100% de cobertura
├── app.py                 # Dashboard interactivo en Streamlit para simulación de transferencia
├── main.py                # Script CLI de demostración y pruebas de rendimiento
├── mkdocs.yml             # Configuración del portal web corporativo (Tema Índigo)
├── requirements.txt       # Dependencias y librerías del entorno
└── README.md              # Documentación principal en la raíz del proyecto

## 💼 Casos Prácticos de Uso

1. **Transferencia Masiva Inter-Nodos en Data Lakes:**
   - Movimiento de petabytes de información entre nodos de cómputo y almacenamiento sin los costos de serialización de JSON o CSV.
2. **Pipelines de Datos de Baja Latencia:**
   - Streaming analítico en tiempo real entre servicios de micro-arquitecturas empresariales.
3. **Optimización de Memoria en Cómputo Distribuido:**
   - Uso de formato columnar estándar para interoperabilidad inmediata entre motores analíticos.

## ⚙️ Componentes Técnicos
- **Servidor Flight (`src/flight_server.py`):** Encapsulación de gRPC y manejo de Streams de registros con Apache Arrow.
- **CLI Demostrativo (`main.py`):** Script ejecutable de validación de conexión y transporte de datos.
- **Documentación Formal:** Portal técnico estructurado con MkDocs bajo un esquema de color índigo corporativo.

## 🚀 Comandos para Ejecutar

- **Instalación de dependencias:**
  `pip install -r requirements.txt`

- **Ejecución de pruebas unitarias (con cobertura estricta al 100%):**
  `python -m pytest --cov=src --cov-fail-under=100 --cov-report=term-missing --cache-clear`

- **Ejecución del Script CLI Demostrativo:**
  `python main.py`

- **Lanzamiento del Dashboard Interactivo (Streamlit):**
  `streamlit run app.py`

- **Lanzamiento del Portal de Documentación (MkDocs):**
  `mkdocs serve`