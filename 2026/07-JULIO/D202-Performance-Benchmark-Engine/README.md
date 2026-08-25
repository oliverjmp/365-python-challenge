# D202 - Performance Benchmark Engine (Python Timeit + DuckDB)

Benchmark comparativo de rendimiento analítico entre el procesamiento tradicional en memoria con Pandas y la velocidad columnar de DuckDB utilizando Python y Streamlit.

## 🏛️ Estructura del Proyecto

D202-Performance-Benchmark-Engine/
├── docs/
│   ├── index.md           # Página principal de documentación técnica del reto
│   └── architecture.md    # Arquitectura detallada del motor de rendimiento
├── src/
│   ├── __init__.py
│   └── benchmark_runner.py # Lógica de medición con timeit y comparación Pandas vs DuckDB
├── tests/
│   ├── __init__.py
│   └── test_benchmark.py  # Pruebas unitarias estrictas con pytest y 100% de cobertura
├── app.py                 # Dashboard interactivo en Streamlit para visualización de métricas
├── main.py                # Script CLI para la ejecución y auditoría de benchmarks por consola
├── README.md              # Documentación principal en la raíz del proyecto
├── mkdocs.yml             # Configuración del portal web corporativo (Tema Índigo)
└── requirements.txt       # Dependencias y librerías del entorno

## 💼 Casos Prácticos de Uso

1. **Optimización de Pipelines ETL:**
   - Selección informada de motores de procesamiento basándose en métricas de tiempo real para transformar grandes volúmenes de datos transaccionales.
2. **Auditoría de Rendimiento de Consultas:**
   - Evaluación cuantitativa del impacto de migrar lógicas de negocio desde DataFrames tradicionales hacia motores analíticos in-process basados en SQL columnar.
3. **Gobierno de Recursos Computacionales:**
   - Identificación de cuellos de botella en memoria y CPU durante operaciones de agregación y filtrado masivo.

## ⚙️ Componentes Técnicos
- **Motor de Medición (`src/benchmark_runner.py`):** Utilización de la librería nativa `timeit` para calcular de manera precisa los tiempos de ejecución iterativos entre Pandas y DuckDB.
- **Dashboard Interactivo (`app.py`):** Interfaz visual en **Streamlit** para ajustar volúmenes de filas y comparar rendimientos gráficamente.
- **Documentación Formal:** Portal técnico estructurado con MkDocs bajo el esquema de color índigo corporativo.

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