# D183 - DuckDB Direct Parquet Query

Motor analítico empresarial para la ejecución de consultas SQL de alta velocidad de **cero copia (Zero-Copy)** directamente sobre ficheros Parquet distribuidos en disco, sin la necesidad de cargarlos previamente en la memoria RAM.

## 🏛️ Arquitectura de Procesamiento Implementada
1. **Ingesta Corporativa Masiva:** Generación estructurada de datasets transaccionales a gran escala.
2. **Compresión ZSTD de Alta Densidad:** Almacenamiento columnar optimizado para reducir la E/S de disco y acelerar la recuperación de metadatos.
3. **Pushdown Predicate Engine:** El motor de DuckDB analiza y filtra los datos directamente desde el almacenamiento secundario mediante vectorización.

## 💡 Casos de Uso del Mundo Real
- **Arquitecturas de Data Lakes / Lakehouses:** Consultar petabytes de datos almacenados en formatos abiertos (Parquet/ORC) sin depender de bases de datos relacionales pesadas.
- **Analítica de Cero Copia (Zero-Copy Analytics):** Reducir drásticamente los cuellos de botella de memoria RAM al procesar datasets masivos en pipelines de Business Intelligence o Machine Learning.

## 📂 Estructura del Proyecto
```text
D183-DuckDB-Direct-Parquet-Query/
├── data_lake/             # Almacenamiento columnar temporal de ficheros Parquet
├── docs/
│   └── index.md           # Documentación interactiva (MkDocs) con resultados en vivo
├── src/
│   ├── __init__.py
│   ├── parquet_query_engine.py  # Lógica del motor analítico corporativo
│   └── main_demo.py       # Script ejecutable principal (Todo en uno)
├── tests/
│   ├── __init__.py
│   └── test_duckdb_parquet.py # Pruebas unitarias con pytest
├── mkdocs.yml             # Configuración de MkDocs
├── requirements.txt       # Dependencias del proyecto
└── README.md              # Documentación técnica del hito