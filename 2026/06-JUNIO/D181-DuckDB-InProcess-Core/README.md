# D181 - DuckDB In-Process Core

Inicialización de base de datos analítica *in-process* y ejecución de consultas SQL de alta velocidad con Python.

## Características Principales
- **Motor Analítico Embebido:** Procesamiento de consultas pesadas directamente en memoria sin dependencias de servidores externos (como PostgreSQL o MySQL).
- **Integración Nativa con Python:** API sencilla para ejecutar sentencias SQL y retornar resultados en estructuras estándar.
- **Cobertura Total:** Validado mediante pruebas unitarias con `pytest` y `pytest-cov`.

## 💡 Casos de Uso Prácticos
1. **Pipelines de Datos Locales (ETL):** Transformación rápida de archivos CSV o Parquet mediante SQL puro antes de cargarlos en modelos de Machine Learning.
2. **Analítica en Memoria:** Consultas agregadas de alta velocidad sobre conjuntos de datos medianos en aplicaciones de escritorio o microservicios.

## Estructura del Proyecto
```text
D181-DuckDB-InProcess-Core/
├── docs/
│   └── index.md
├── src/
│   ├── __init__.py
│   └── db_engine.py
├── tests/
│   ├── __init__.py
│   └── test_db.py
├── mkdocs.yml
├── requirements.txt
└── README.md