# Día 64: Star Schema Staging (DuckDB + SQLModel)

## 🎯 Enfoque Técnico y Propósito
Este módulo implementa un pipeline ETL de nivel empresarial orientado a transformar datos transaccionales planos (OLTP) en un **Modelo Dimensional en Estrella (Star Schema)** optimizado para analítica (OLAP). 

Para garantizar alto rendimiento y tipado estricto, utilizamos:
* **DuckDB**: Como motor analítico in-process columnar de ultra alta velocidad.
* **SQLModel**: Para la definición declarativa y tipada de las tablas de dimensiones y hechos con restricciones estrictas de clave primaria y ajena.
* **Pytest**: Para la validación automatizada de la integridad referencial y prevención de registros huérfanos.
* **Logging Estructurado**: Para la monitorización de tiempos de ejecución y captura controlada de errores.

---

## 🏗️ Arquitectura del Proyecto

```text
D64-Star-Schema-Staging/
├── data/
│   └── source_transactions.csv
├── src/
│   ├── __init__.py
│   ├── models.py       # Modelos relacionales con SQLModel
│   ├── pipeline.py     # Lógica ETL y logging estructurado
│   └── database.py     # Gestor de conexión DuckDB
├── tests/
│   ├── __init__.py
│   └── test_staging.py # Pruebas unitarias de integridad referencial
├── requirements.txt
└── README.md