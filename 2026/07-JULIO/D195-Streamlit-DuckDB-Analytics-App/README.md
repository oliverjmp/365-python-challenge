# D195 - Streamlit DuckDB Analytics App

Tablero web interactivo de alto rendimiento impulsado por **DuckDB** como motor analítico subyacente y **Streamlit** para la visualización de métricas de negocio.

## 🏛️ Arquitectura Implementada
1. **Data Lake Analítico:** Persistencia estructurada en `data_lake/analytics_warehouse.db`.
2. **Motor SQL optimizado:** Consultas analíticas ultrarrápidas mediante DuckDB.
3. **Interfaz Gráfica Interactiva:** Dashboard corporativo en Streamlit.

## 📂 Estructura del Proyecto
```text
D195-Streamlit-DuckDB-Analytics-App/
├── data_lake/
│   └── analytics_warehouse.db
├── docs/
│   └── index.md
├── src/
│   ├── __init__.py
│   └── analytics_engine.py
├── tests/
│   ├── __init__.py
│   └── test_analytics_engine.py
├── app_analytics.py
├── mkdocs.yml
├── requirements.txt
└── README.md