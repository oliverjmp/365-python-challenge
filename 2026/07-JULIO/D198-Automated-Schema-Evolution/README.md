# D198 - Automated Schema Evolution (PyArrow Dataset Schema)

Sistema avanzado de **gestión y evolución automática de esquemas** utilizando **PyArrow Datasets**, diseñado para procesar y unificar de forma transparente fuentes de datos tabulares incrementales (archivos Parquet) que experimentan cambios estructurales a lo largo del tiempo.

## 🏛️ Arquitectura Implementada
1. **Capa de Dataset Distribuido (`pyarrow.dataset`):** Inspección y escaneo dinámico de múltiples particiones o fragmentos de datos directamente sobre el Data Lake local.
2. **Reconciliación Automática de Esquemas (Schema Evolution):** Mecanismo nativo de PyArrow capaz de unificar esquemas dispares entre diferentes versiones de lotes de datos, rellenando automáticamente las columnas faltantes o nuevas con valores nulos (`null`).
3. **Persistencia Columnar Eficiente (`pyarrow.parquet`):** Almacenamiento optimizado de lotes de datos estructurados bajo el formato columnar estándar de la industria.

## 💼 Casos de Uso Empresariales
1. **Ingesta de Datos Evolving-Schema:** Permite a los pipelines de datos absorber cambios evolutivos en las fuentes de origen sin romper los procesos analíticos posteriores.
2. **Consolidación Analítica Transparente:** Facilita la creación de vistas unificadas combinando datos históricos con nuevos flujos enriquecidos sin necesidad de costosas migraciones manuales.
3. **Interoperabilidad con Motores OLAP:** Prepara conjuntos de datos perfectamente homogeneizados para ser consultados por motores analíticos de alto rendimiento.

## 🚀 Valor Añadido: Resiliencia y Gobernanza
- **Auditoría Estructural en Tiempo Real:** Inspección transparente de los campos y tipos de datos resultantes.
- **Cobertura de Pruebas Unitarias Estrictas:** Integración nativa con `pytest` y `pytest-cov` apuntando al 100% de cobertura mediante directorios temporales (`tmp_path`).
- **Interfaz Interactiva de Analítica:** Incorporación de un dashboard web analítico desarrollado con **Streamlit**.

## 📂 Estructura del Proyecto
```text
D198-Automated-Schema-Evolution/
├── data_lake/
│   ├── raw_lote_1.parquet          # Lote inicial de clientes (esquema base v1)
│   └── raw_lote_2.parquet          # Lote evolucionado con columnas adicionales (v2)
├── docs/
│   └── architecture.md             # Documentación técnica corporativa del pipeline
├── src/
│   ├── __init__.py
│   └── schema_evolution.py         # Motor de gestión y unificación de esquemas PyArrow
├── tests/
│   ├── __init__.py
│   └── test_schema_evolution.py    # Suite de pruebas unitarias con pytest (100% cobertura)
├── app.py                          # Dashboard interactivo con Streamlit
├── main.py                         # Script ejecutable de consola para demostración del pipeline
└── requirements.txt                # Dependencias del entorno
└── README.md 