# D191 - Async DuckDB Query Runner

Motor de ejecución concurrente y no bloqueante para consultas analíticas pesadas, integrando el bucle de eventos de **asyncio** con la lectura de archivos físicos de **DuckDB** almacenados en el Data Lake.

## 🏛️ Arquitectura de Procesamiento Implementada
1. **Persistencia Física en Data Lake:** Lectura y escritura concurrente sobre bases de datos en disco (`data_lake/async_analytics.db`).
2. **Concurrencia No Bloqueante (`asyncio.to_thread`):** Aislamiento de operaciones de bases de datos bloqueantes en hilos independientes para evitar congelar el bucle principal.
3. **Ejecución en Lote Paralela (`asyncio.gather`):** Lanzamiento simultáneo de consultas analíticas para optimizar los tiempos globales de respuesta.

## 💡 Casos de Uso del Mundo Real
- **APIs Analíticas de Alto Tráfico:** Atender múltiples solicitudes concurrentes de reportes pesados sin que una consulta lenta bloquee a los demás usuarios.
- **Orquestación de Pipelines de Datos:** Procesar fragmentos de grandes almacenes de datos en paralelo.

## 📂 Estructura del Proyecto
```text
D191-Async-DuckDB-Query-Runner/
├── data_lake/
│   └── async_analytics.db   # Base de datos física generada automáticamente
├── docs/
│   └── index.md             # Documentación técnica corporativa (MkDocs)
├── src/
│   ├── __init__.py
│   └── async_engine.py      # Motor analítico asíncrono con asyncio + DuckDB
├── tests/
│   ├── __init__.py
│   └── test_async_engine.py # Pruebas unitarias asíncronas con pytest-asyncio
├── run_async_queries.py     # Script ejecutable principal por consola
├── mkdocs.yml               # Configuración del portal MkDocs
├── requirements.txt         # Dependencias del entorno
└── README.md                # Documentación técnica avanzada del hito