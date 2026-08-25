# D203 - Dockerized DuckDB Pipeline

Contenorización optimizada de pipelines analíticos basados en DuckDB y Python utilizando una estrategia de construcción multi-etapa (`Multi-stage Dockerfile`).

## 🏛️ Estructura del Proyecto

D203-Dockerized-DuckDB-Pipeline/
├── docs/
│   ├── index.md           # Página principal de documentación técnica del hito
│   └── architecture.md    # Arquitectura de la imagen multi-etapa
├── src/
│   ├── __init__.py
│   └── pipeline_runner.py # Lógica del pipeline analítico in-process
├── tests/
│   ├── __init__.py
│   └── test_pipeline.py   # Pruebas unitarias estrictas con pytest y 100% de cobertura
├── app.py                 # Dashboard interactivo en Streamlit
├── main.py                # Script CLI para la ejecución del pipeline
├── Dockerfile             # Configuración multi-etapa optimizada para producción
├── .dockerignore          # Archivos excluidos del contexto de Docker
├── README.md              # Documentación principal en la raíz del proyecto
├── mkdocs.yml             # Configuración del portal web corporativo (Tema Índigo)
└── requirements.txt       # Dependencias del entorno

## 💼 Casos Prácticos de Uso

1. **Despliegue de Microservicios Analíticos:**
   - Empaquetado limpio de motores de datos para ejecución idéntica en cualquier entorno de nube (AWS, GCP, Azure).
2. **Optimización de Imágenes de Contenedor:**
   - Reducción drástica del tamaño final de la imagen separando las herramientas de compilación de la capa de ejecución mediante *multi-stage builds*.
3. **Portabilidad de Pipelines ETL:**
   - Ejecución garantizada de consultas analíticas basadas en DuckDB sin dependencias externas del sistema operativo anfitrión.

## ⚙️ Componentes Técnicos
- **Docker Multi-stage (`Dockerfile`):** Imagen dividida en etapas de construcción y ejecución para máxima seguridad y eficiencia.
- **CLI y Dashboard (`main.py` / `app.py`):** Ejecución por consola y visualización web interactiva con Streamlit.
- **Documentación Formal:** Portal técnico estructurado con MkDocs bajo un esquema de color índigo corporativo.

## 🚀 Ejecución y Comandos

- **Instalación local de dependencias:**
  `pip install -r requirements.txt`
- **Pruebas unitarias (con cobertura):**
  `python -m pytest --cov=src --cov-report=term-missing --cache-clear`
- **Ejecutar CLI localmente:**
  `python main.py`
- **Construir la imagen de Docker:**
  `docker build -t d203-duckdb-pipeline .`
- **Ejecutar el contenedor:**
  `docker run --rm d203-duckdb-pipeline`