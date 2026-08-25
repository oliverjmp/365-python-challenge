# D204 - Docker Compose Analytics Stack

Orquestación local de microservicios analíticos basados en **FastAPI**, **DuckDB** y **Docker Compose** utilizando volúmenes de datos montados.

## 🏛️ Estructura del Proyecto

D204-Docker-Compose-Analytics-Stack/
├── data/
│   └── source_data.csv    # Dataset compartido montado como volumen
├── docs/
│   ├── index.md           # Documentación técnica principal
│   └── architecture.md    # Arquitectura de contenedores y volúmenes
├── src/
│   ├── __init__.py
│   └── analytics_service.py # Lógica analítica con DuckDB
├── tests/
│   ├── __init__.py
│   └── test_api.py        # Pruebas con pytest (100% cobertura)
├── app.py                 # Dashboard interactivo en Streamlit
├── main.py                # Aplicación FastAPI
├── Dockerfile             # Imagen de la API analítica
├── docker-compose.yml     # Orquestación y volúmenes compartidos
├── .dockerignore          # Archivos excluidos
├── README.md              # Documentación general
├── mkdocs.yml             # Portal web de documentación (Tema Índigo)
└── requirements.txt       # Dependencias