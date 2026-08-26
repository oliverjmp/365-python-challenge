# D213 - Advanced Aggregation Pipelines

Ejecución de agregaciones multidimensionales complejas (`CUBE`, `ROLLUP`) en una sola pasada con **DuckDB** y Python.

## 🏛️ Estructura del Proyecto

D213-Advanced-Aggregation-Pipelines/
├── .coveragerc            # Configuración de políticas estrictas de cobertura (fail_under = 100)
├── docs/
│   ├── index.md           # Página principal de documentación técnica del hito
│   └── architecture.md    # Arquitectura detallada de agregaciones avanzadas DuckDB
├── src/
│   ├── __init__.py
│   └── aggregation_manager.py # Lógica central de consultas CUBE y ROLLUP
├── tests/
│   ├── __init__.py
│   └── test_aggregation.py    # Pruebas unitarias estrictas con pytest y 100% de cobertura
├── app.py                 # Dashboard interactivo en Streamlit
├── main.py                # Script CLI de demostración y pruebas analíticas
├── mkdocs.yml             # Configuración del portal web corporativo (Tema Indigo)
├── requirements.txt       # Dependencias y librerías del entorno
└── README.md              # Documentación principal en la raíz del proyecto

## 💼 Casos Prácticos de Uso

1. **Informes Financieros Jerárquicos (`ROLLUP`):**
   - Generación de reportes de ventas por región, categoría y subtotales acumulados de forma automática.
2. **Análisis Multidimensional Cruzado (`CUBE`):**
   - Exploración de cubos de datos donde cualquier combinación de dimensiones requiere métricas consolidadas.
3. **Optimización de Consultas Analíticas:**
   - Reducción drástica de líneas de código SQL complejas mediante el uso de operadores nativos de agregación avanzada.

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