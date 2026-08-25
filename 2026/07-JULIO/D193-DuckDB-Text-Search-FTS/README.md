# D193 - DuckDB Full-Text Search (FTS)

Motor de búsqueda de texto completo optimizado para el análisis de registros masivos de logs, utilizando la extensión FTS de **DuckDB**, persistencia en el **Data Lake** y visualización interactiva avanzada con **`rich`**.

## 🏛️ Arquitectura de Procesamiento Implementada
1. **Persistencia Estructurada en Data Lake:** Gestión de bases de datos persistentes en la ruta `data_lake/logs_fts.db`.
2. **Índices Invertidos FTS:** Carga de la extensión nativa de DuckDB para indexar grandes volúmenes de texto y realizar búsquedas de alta velocidad.
3. **Interfaz CLI con Rich:** Exposición de resultados mediante paneles y tablas formateadas con métricas de rendimiento en milisegundos.

## 💡 Casos de Uso del Mundo Real
- **Análisis de Logs de Servidores e Infraestructura:** Localización inmediata de errores críticos, advertencias o trazas de seguridad entre millones de líneas de logs.
- **Búsquedas de Texto en Data Warehouses:** Indexación de campos descriptivos o metadatos textuales para analítica avanzada sin penalización de rendimiento.

## 📂 Estructura del Proyecto
```text
D193-DuckDB-Text-Search-FTS/
├── data_lake/
│   └── logs_fts.db          # Base de datos persistente con índice FTS
├── docs/
│   └── index.md             # Documentación técnica corporativa (MkDocs)
├── src/
│   ├── __init__.py
│   └── fts_engine.py        # Motor lógico de búsqueda FTS con DuckDB
├── tests/
│   ├── __init__.py
│   └── test_fts_engine.py   # Pruebas unitarias con pytest
├── run_fts_search.py        # Script ejecutable principal con rich
├── mkdocs.yml               # Configuración del portal MkDocs
├── requirements.txt         # Dependencias del entorno
└── README.md                # Documentación técnica avanzada del hito