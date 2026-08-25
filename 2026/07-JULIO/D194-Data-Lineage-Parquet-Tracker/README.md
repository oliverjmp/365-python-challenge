# D194 - Data Lineage Parquet Tracker

Sistema de rastreo automatizado de metadatos y linaje de datos para transformaciones con ficheros **Parquet**, persistencia en el **Data Lake** y visualización interactiva mediante **Streamlit**.

## 🏛️ Arquitectura Implementada
1. **Persistencia en Data Lake:** Gestión de ficheros analíticos en formato Parquet y metadatos asociados en `data_lake/`.
2. **Motor de Linaje:** Captura de esquemas, conteo de filas y dependencias upstream/downstream.
3. **Dashboard Ejecutivo:** Interfaz web interactiva en Streamlit para auditar el árbol de transformación de los datos.

## 📂 Estructura del Proyecto
```text
D194-Data-Lineage-Parquet-Tracker/
├── data_lake/
│   ├── raw_data.parquet
│   └── processed_data.parquet
├── docs/
│   └── index.md
├── src/
│   ├── __init__.py
│   └── lineage_engine.py
├── tests/
│   ├── __init__.py
│   └── test_lineage_engine.py
├── dashboard_lineage.py
├── mkdocs.yml
├── requirements.txt
└── README.md