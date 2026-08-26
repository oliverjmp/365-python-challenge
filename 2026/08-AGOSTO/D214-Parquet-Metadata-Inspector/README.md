# D214 - Parquet Metadata Inspector

Inspector programático de esquemas, metadatos y estadísticas internas de ficheros **Apache Parquet** utilizando **PyArrow** y Python.

## 🏛️ Estructura del Proyecto

D214-Parquet-Metadata-Inspector/
├── .coveragerc            # Configuración de políticas estrictas de cobertura (fail_under = 100)
├── docs/
│   ├── index.md           # Página principal de documentación técnica del hito
│   └── architecture.md    # Arquitectura detallada del inspector de metadatos
├── src/
│   ├── __init__.py
│   └── parquet_inspector.py   # Lógica central de lectura de esquemas y estadísticas Parquet
├── tests/
│   ├── __init__.py
│   └── test_inspector.py      # Pruebas unitarias estrictas con pytest y 100% de cobertura
├── app.py                     # Dashboard interactivo en Streamlit
├── main.py                    # Script CLI de demostración y validación
├── mkdocs.yml             # Configuración del portal web corporativo (Tema Deep Orange)
├── requirements.txt       # Dependencias y librerías del entorno
└── README.md              # Documentación principal en la raíz del proyecto

## 💼 Casos Prácticos de Uso

1. **Auditoría de Esquemas en Data Lakes:**
   - Verificación automática de la compatibilidad de esquemas entre múltiples ficheros Parquet antes de ingestas masivas.
2. **Optimización de Performance Analítica:**
   - Análisis del tamaño de los *Row Groups* para garantizar un rendimiento óptimo de lectura columnar.
3. **Monitoreo de Calidad de Datos:**
   - Detección de cambios inesperados en tipos de datos o campos nulos dentro de pipelines de datos.

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