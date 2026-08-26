# D207 - Custom Decorator Query Metrics

Decorador avanzado en Python para la medición automática de latencias, auditoría de rendimiento y telemetría de recursos en consultas SQL ejecutadas sobre **DuckDB**.

## 🏛️ Estructura del Proyecto

D207-Custom-Decorator-Query-Metrics/
├── .coveragerc            # Configuración de políticas estrictas de cobertura (fail_under = 100)
├── data/
│   └── mock_metrics.csv   # Dataset sintético de control para telemetría
├── docs/
│   ├── index.md           # Página principal de documentación técnica del reto
│   └── architecture.md    # Arquitectura detallada del sistema de decoradores y flujos
├── src/
│   ├── __init__.py
│   └── metrics_decorator.py # Lógica del decorador avanzado y motor analítico con DuckDB
├── tests/
│   ├── __init__.py
│   └── test_metrics.py    # Pruebas unitarias estrictas con pytest y 100% de cobertura
├── app.py                 # Dashboard interactivo en Streamlit para auditoría de métricas
├── mkdocs.yml             # Configuración del portal web corporativo (Tema Índigo)
├── requirements.txt       # Dependencias y librerías del entorno
└── README.md              # Documentación principal en la raíz del proyecto

## 💼 Casos Prácticos de Uso

1. **Monitoreo de Latencia en Pipelines Analíticos:**
   - Interceptación transparente de consultas SQL pesadas de agregación (`SELECT`) para medir tiempos de ejecución en milisegundos mediante alta precisión temporal (`time.perf_counter`), identificando cuellos de botella sin contaminar la lógica de negocio.
2. **Observabilidad y Resiliencia ante Fallos:**
   - Auditoría automatizada de estados operacionales y manejo defensivo de excepciones ante errores de infraestructura o sintaxis SQL, registrando trazas de fallo antes de propagarlas al sistema.
3. **Gobierno de Calidad y Telemetría Operacional:**
   - Registro estructurado de logs en tiempo de ejecución para evaluar el rendimiento de motores analíticos in-memory bajo un estándar de metaprogramación con `functools.wraps`.

## ⚙️ Componentes Técnicos
- **Decorador de Telemetría (`src/metrics_decorator.py`):** Closure avanzado que envuelve funciones analíticas para capturar latencias, éxito operacional y excepciones mediante bloques `try...except...finally`.
- **Dashboard Interactivo (`app.py`):** Interfaz visual en **Streamlit** dotada de visualizaciones analíticas y reportes de rendimiento.
- **Documentación Formal:** Portal técnico estructurado con MkDocs bajo un esquema de color índigo corporativo.

## 🚀 Ejecución y Comandos de Pruebas

- **Instalación de dependencias:**
  `pip install -r requirements.txt`

- **Ejecución de pruebas unitarias (con cobertura estricta al 100%):**
  `python -m pytest --cov=src --cov-fail-under=100 --cov-report=term-missing --cache-clear`

- **Lanzamiento del Dashboard Interactivo:**
  `streamlit run app.py`

- **Lanzamiento del Portal de Documentación:**
  `mkdocs serve`