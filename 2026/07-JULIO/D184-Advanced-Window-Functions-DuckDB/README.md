# D184 - Advanced Window Functions DuckDB

Implementación de SQL analítico avanzado utilizando **funciones de ventana (*Window Functions*)** en DuckDB para el cálculo de métricas financieras, acumulados anuales (*Running Totals*) y variaciones de crecimiento intermensual (MoM).

## 🏛️ Arquitectura de Procesamiento Implementada
1. **Particionamiento Lógico (`PARTITION BY`):** Aislamiento de cálculos por dimensiones de negocio sin duplicar estructuras físicas.
2. **Ventanas Deslizantes (`ROWS BETWEEN`):** Computación eficiente de sumas acumuladas secuenciales.
3. **Retraso Temporal (`LAG`):** Acceso directo a filas anteriores sobre almacenamiento columnar ZSTD para calcular tasas de variación porcentual.

## 💡 Casos de Uso del Mundo Real
- **Analítica Financiera Automatizada:** Generación de reportes ejecutivos de ingresos y tendencias plurianuales en tiempo real.
- **Dashboards de Negocio Interactivos:** Desacoplamiento de motores de procesamiento analítico in-process con interfaces visuales ligeras para la toma de decisiones.

## 📂 Estructura del Proyecto
```text
D184-Advanced-Window-Functions-DuckDB/
├── data_lake/             # Almacenamiento columnar temporal de ficheros Parquet
├── docs/
│   └── index.md           # Documentación técnica (MkDocs) del hito
├── src/
│   ├── __init__.py
│   ├── window_analytics_engine.py  # Motor de SQL analítico avanzado
│   ├── dashboard.py       # Aplicación ejecutiva interactiva (Streamlit + Plotly)
│   └── main_demo.py       # Script ejecutable principal de terminal
├── tests/
│   ├── __init__.py
│   └── test_window_analytics.py # Pruebas unitarias con pytest
├── mkdocs.yml             # Configuración de MkDocs
├── requirements.txt       # Dependencias del proyecto
└── README.md              # Documentación técnica del hito