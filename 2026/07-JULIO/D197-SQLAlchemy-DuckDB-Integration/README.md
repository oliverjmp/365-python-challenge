# D197 - SQLAlchemy DuckDB Integration

Sistema avanzado de **Mapeo Objeto-Relacional (ORM)** utilizando **SQLAlchemy 2.0** en combinación con el dialecto de **DuckDB**, diseñado para proveer persistencia transaccional de alto rendimiento sobre el Data Lake corporativo.

## 🏛️ Arquitectura Implementada
1. **Capa Declarativa de Modelos (`Base`):** Definición estricta de esquemas y entidades de negocio mediante clases tipadas en Python moderno (`Mapped` y `mapped_column`), asegurando consistencia de tipos en tiempo de compilación.
2. **Motor de Conectividad Transaccional (`create_engine`):** Conexión directa al Data Lake local mediante el dialecto `duckdb://`, optimizando la ejecución de sentencias SQL bajo un entorno ACID ligero.
3. **Gestión de Sesiones (`sessionmaker`):** Patrón de diseño para el ciclo de vida de transacciones, garantizando aislamiento, gestión de errores y control de *commit/rollback* automáticos.

## 💼 Casos de Uso Empresariales
1. **Modelado de Datos Orientado a Objetos:** Permite a los ingenieros de datos abstraer tablas complejas en clases de Python legibles, facilitando la mantenibilidad del código.
2. **Transaccionalidad Confiable:** Asegura que operaciones masivas de inserción o actualización de registros de clientes se realicen de forma atómica, evitando estados corruptos en el almacén de datos.
3. **Interoperabilidad Analítica:** Facilita la transición entre flujos transaccionales relacionales y consultas analíticas masivas impulsadas por la arquitectura columnar de DuckDB.

## 🚀 Valor Añadido: Resiliencia y Gobernanza
- **Auto-creación de Entornos:** El gestor detecta automáticamente si el directorio del Data Lake y los esquemas relacionales existen, inicializándolos de forma transparente para evitar fallos de arranque en frío.
- **Cobertura de Pruebas Unitarias:** Integración nativa con `pytest` y `pytest-cov` para validar el comportamiento del ORM mediante bases de datos efímeras creadas en memoria o directorios temporales (`tmp_path`).

## 📂 Estructura del Proyecto
```text
D197-SQLAlchemy-DuckDB-Integration/
├── data_lake/
│   └── orm_warehouse.db      # Base de datos transaccional DuckDB
├── docs/
│   └── index.md              # Portal de documentación MkDocs
├── src/
│   ├── __init__.py
│   └── orm_engine.py         # Motor de modelos y sesiones ORM
├── tests/
│   ├── __init__.py
│   └── test_orm_engine.py    # Suite de pruebas unitarias pytest
├── mkdocs.yml                # Configuración de MkDocs
├── requirements.txt          # Dependencias del entorno
└── README.md                 # Documentación técnica corporativa