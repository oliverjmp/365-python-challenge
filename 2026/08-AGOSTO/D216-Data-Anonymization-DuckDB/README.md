# D216 - Data Anonymization with DuckDB

Pipeline de enmascaramiento y anonimización de PII (*Personally Identifiable Information*) directamente en el motor SQL de **DuckDB**.

## 🏛️ Estructura del Proyecto

D216-Data-Anonymization-DuckDB/
├── .coveragerc            # Configuración de cobertura estricta (fail_under = 100)
├── docs/
│   ├── index.md           # Documentación técnica del hito
│   └── architecture.md    # Diagrama de arquitectura del pipeline SQL
├── src/
│   ├── __init__.py
│   └── anonymizer.py      # Lógica del motor SQL de anonimización
├── tests/
│   ├── __init__.py
│   └── test_anonymizer.py # Pruebas unitarias con pytest (100% Cobertura)
├── main.py                # Script CLI de validación y demostración
├── mkdocs.yml             # Configuración del portal web corporativo
├── requirements.txt       # Dependencias del proyecto
└── README.md              # Documentación principal

## 🚀 Comandos de Ejecución

- **Instalar dependencias:**
  `pip install -r requirements.txt`

- **Ejecutar pruebas unitarias (con cobertura al 100%):**
  `python -m pytest --cov=src --cov-fail-under=100 --cov-report=term-missing --cache-clear`

- **Ejecutar script CLI de validación:**
  `python main.py`

- **Servir documentación técnica:**
  `mkdocs serve`

## 💼 Casos Prácticos de Uso

1. **Cumplimiento Normativo (GDPR / CCPA):**
   - Facilita la sanitización de bases de datos de clientes antes de compartirlas con equipos de analítica o ciencia de datos que no requieren acceso a PII directa.
2. **Entornos de Pruebas y Staging Seguros:**
   - Permite generar subconjuntos de datos de producción completamente anonimizados para alimentar entornos de desarrollo y testing sin riesgos de fugas de información sensible.
3. **Anonimización en Pipelines de Datos Analíticos (ETL):**
   - Agiliza la transformación y enmascaramiento directamente a nivel de motor SQL columnar (DuckDB) antes de persistir la información en almacenes o Data Lakes.