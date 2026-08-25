# D201 - DuckDB Spatial & Geospatial Extensions

Consultas geoespaciales avanzadas, manipulación de coordenadas y transformaciones geométricas utilizando la extensión **Spatial de DuckDB** integrada con Python y Streamlit.

## 🏛️ Estructura del Proyecto

D201-DuckDB-Spatial-Extensions/
├── docs/
│   ├── index.md           # Página principal de documentación técnica del reto
│   └── architecture.md    # Arquitectura detallada del motor geoespacial
├── src/
│   ├── __init__.py
│   └── spatial_runner.py  # Lógica de carga de extensión spatial y consultas geoespaciales
├── tests/
│   ├── __init__.py
│   └── test_spatial.py    # Pruebas unitarias estrictas con pytest y 100% de cobertura
├── app.py                 # Dashboard interactivo en Streamlit con visualización cartográfica
├── main.py                # Script CLI para la ejecución y auditoría de consultas espaciales
├── README.md              # Documentación principal en la raíz del proyecto
├── mkdocs.yml             # Configuración del portal web corporativo (Tema Índigo)
└── requirements.txt       # Dependencias y librerías del entorno

## 💼 Casos Prácticos de Uso

1. **Logística y Cadena de Suministro:**
   - Optimización de rutas y conversión automática de coordenadas de almacenes y puntos de entrega a formatos estándar como Well-Known Text (WKT).
2. **Análisis de Ubicación (Geomarketing):**
   - Procesamiento masivo de puntos de interés (POI) para identificar proximidades y agrupar sucursales comerciales geográficamente.
3. **Telemetría y IoT:**
   - Ingesta y validación rápida de posiciones geográficas emitidas por dispositivos móviles o sensores de flotas vehiculares directamente en el motor analítico de DuckDB.

## ⚙️ Componentes Técnicos
- **Motor Espacial (`src/spatial_runner.py`):** Configuración e instalación dinámica de la extensión espacial en DuckDB para operaciones geométricas eficientes.
- **Dashboard Interactivo (`app.py`):** Interfaz visual en **Streamlit** dotada de tablas de datos y mapas nativos de localización.
- **Documentación Formal:** Portal técnico estructurado con MkDocs bajo un esquema de color índigo corporativo.

## 🚀 Ejecución y Comandos de Pruebas

- **Instalación de dependencias:**
  `pip install -r requirements.txt`

- **Ejecución de pruebas unitarias (con reporte de cobertura):**
  `python -m pytest --cov=src --cov-report=term-missing --cache-clear`

- **Ejecución del Script CLI:**
  `python main.py`

- **Lanzamiento del Dashboard Interactivo:**
  `streamlit run app.py`

- **Lanzamiento del Portal de Documentación:**
  `mkdocs serve`