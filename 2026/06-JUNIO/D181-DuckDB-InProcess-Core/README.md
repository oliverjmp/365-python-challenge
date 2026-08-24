# D181 - DuckDB In-Process Core

Inicialización de base de datos analítica *in-process* y ejecución de consultas SQL de alta velocidad utilizando DuckDB y Python.

## Características Principales
- **Motor Analítico Embebido:** Procesamiento de consultas pesadas directamente en memoria sin dependencias de servidores externos (como PostgreSQL o MySQL).
- **Integración Nativa con Python:** API sencilla para ejecutar sentencias SQL y retornar resultados en estructuras estándar.
- **Cobertura Total:** Validado mediante pruebas unitarias con `pytest` y `pytest-cov` asegurando un **100% de cobertura**.

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
DuckDB se ha convertido en la herramienta estándar para analítica local gracias a su capacidad de procesar grandes volúmenes de datos con velocidad columnar y cero fricción de infraestructura.

### Ejemplos de Uso:
1. **Pipelines de Datos Locales (ETL):**
   * *Caso:* Transformación rápida y filtrado avanzado de archivos grandes (como CSV o Parquet) utilizando SQL puro antes de pasarlos a modelos de Machine Learning.
   * *Uso:* Carga los archivos en tablas temporales en memoria y ejecuta uniones complejas en milisegundos.
2. **Analítica en Memoria para Aplicaciones de Escritorio / CLI:**
   * *Caso:* Herramientas internas o reportes automatizados que requieren hacer consultas agregadas sin levantar una base de datos pesada.
   * *Uso:* Permite inicializar una base de datos temporal con `":memory:"` y consultar métricas al instante.
3. **Pruebas Automatizadas Rápidas (Testing):**
   * *Caso:* Validar lógica de negocio basada en bases de datos relacionales sin depender de servicios externos en la nube o contenedores lentos.
   * *Uso:* Se crean tablas y datos de prueba limpios en cada ejecución de `pytest` de forma totalmente aislada.

## 📂 Estructura del Proyecto
```text
D181-DuckDB-InProcess-Core/
├── docs/
│   └── index.md
├── src/
│   ├── __init__.py
│   └── db_engine.py
├── tests/
│   ├── __init__.py
│   └── test_db.py
├── mkdocs.yml
├── requirements.txt
└── README.md