# D185 - Pandas-DuckDB-Bridge

Plataforma analítica avanzada para el intercambio optimizado de estructuras de datos en memoria mediante Zero-Copy con Apache Arrow y DuckDB.

## 🏛️ Arquitectura de Procesamiento Implementada
1. **Modelado Vectorial con Arrow:** Eliminación de serializaciones costosas entre Pandas y motores SQL analíticos.
2. **Bajo Consumo de Memoria RAM:** Arquitectura orientada a bloques columnares contiguos de alto rendimiento.
3. **Ecosistema Completo:** Pruebas unitarias estrictas con pytest, documentación técnica en MkDocs y panel visual interactivo con Streamlit.

## 💼 Casos Prácticos en el Mundo Real
- **Ingesta y Analítica Financiera de Alta Frecuencia:** Procesamiento instantáneo de millones de registros de transacciones generados en Pandas, permitiendo consultas SQL analíticas complejas (agregaciones, filtrados y cruces) sin incurrir en penalizaciones de deserialización en memoria.
- **Pipelines de Machine Learning y Preparación de Features:** Transferencia eficiente de datasets vectoriales masivos desde entornos de limpieza basados en DataFrames hacia motores analíticos in-process para la extracción rápida de variables de negocio y reportes ejecutivos.

## 📂 Estructura del Proyecto
```text
D185-Pandas-DuckDB-Bridge/
├── data_lake/             # Repositorio temporal de artefactos de datos
├── docs/
│   └── index.md           # Portal de documentación técnica (MkDocs)
├── src/
│   ├── __init__.py
│   ├── arrow_bridge_engine.py  # Motor vectorial Zero-Copy (Arrow + DuckDB)
│   ├── dashboard.py       # Aplicación ejecutiva interactiva (Streamlit)
│   └── main_demo.py       # Script ejecutable principal de consola
├── tests/
│   ├── __init__.py
│   └── test_arrow_bridge.py   # Suite de pruebas unitarias con pytest
├── mkdocs.yml             # Configuración del portal MkDocs
├── requirements.txt       # Dependencias del entorno de desarrollo
└── README.md              # Documentación técnica avanzada del hito