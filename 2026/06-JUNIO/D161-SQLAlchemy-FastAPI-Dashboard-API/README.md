# D161 - SQLAlchemy FastAPI Dashboard API

Microservicio backend desarrollado con `FastAPI` y persistencia relacional mediante `SQLAlchemy`, optimizado para procesar y servir datos analíticos agregados a tableros web ejecutivos.

## Características Principales
- **Arquitectura RESTful Robusta:** Endpoints diseñados bajo buenas prácticas para la inserción, consulta paginada y resumen agregado de métricas.
- **Persistencia en Memoria para Testing:** Configuración avanzada con bases de datos SQLite en memoria mediante `StaticPool` para pruebas unitarias limpias y ultrarrápidas con `TestClient`.
- **Validación Estricta:** Uso de esquemas tipados con `Pydantic v2` para garantizar la integridad de los datos entrantes.

## 📂 Estructura del Proyecto
```text
D161-SQLAlchemy-FastAPI-Dashboard-API/
│
├── src/
│   ├── __init__.py
│   ├── database.py
│   ├── models.py
│   └── schemas.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_api.py
├── requirements.txt
└── README.md