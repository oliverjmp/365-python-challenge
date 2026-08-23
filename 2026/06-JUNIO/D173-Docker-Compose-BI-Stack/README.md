# D173 - Docker Compose BI Stack

Orquestación local de un stack completo de Business Intelligence compuesto por una base de datos relacional PostgreSQL y una aplicación analítica desarrollada en Streamlit, unificados mediante `Docker Compose`.

## Características Principales
- **Orquestación Multi-contenedor:** Gestión simultánea y automatizada de los servicios de base de datos y la interfaz de usuario mediante `docker-compose`.
- **Conectividad Robusta:** Conexión segura a PostgreSQL mediante `psycopg2` con manejo de reintentos y variables de entorno.
- **Visualización de BI:** Panel interactivo en Streamlit para la consulta, filtrado y análisis de métricas almacenadas en la base de datos relacional.

## Estructura del Proyecto
```text
D173-Docker-Compose-BI-Stack/
├── src/
│   ├── __init__.py
│   └── db_connector.py
├── tests/
│   ├── __init__.py
│   └── test_db.py
├── app_bi.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md