# D217 - Automated Data Quality with DuckDB

Validación estricta de restricciones de calidad de datos y reglas de negocio mediante aserciones y restricciones SQL nativas en **DuckDB**.

## 🏛️ Estructura del Proyecto

D217-Automated-Data-Quality-DuckDB/
├── .coveragerc            # Cobertura estricta obligatoria (fail_under = 100)
├── docs/
│   ├── index.md           # Portal técnico ejecutivo del hito
│   └── architecture.md    # Arquitectura del pipeline de calidad y constraints
├── src/
│   ├── __init__.py
│   └── data_validator.py  # Motor de validación y reglas SQL en DuckDB
├── tests/
│   ├── __init__.py
│   └── test_validator.py  # Pruebas unitarias con pytest (100% Cobertura)
├── app.py                 # Dashboard interactivo en Streamlit
├── main.py                # Script CLI de validación automatizada
├── mkdocs.yml             # Configuración del portal MkDocs
├── requirements.txt       # Dependencias del entorno
└── README.md              # Documentación principal

## 🚀 Comandos de Ejecución

- **Instalar dependencias:**
  `pip install -r requirements.txt`

- **Ejecutar pruebas unitarias (Garantizando el 100% de cobertura exacta):**
  `python -m pytest --cov=src --cov-fail-under=100 --cov-report=term-missing --cache-clear`

- **Ejecutar script CLI de validación:**
  `python main.py`

- **Lanzar Dashboard Interactivo (Streamlit):**
  `streamlit run app.py`

- **Servir documentación técnica:**
  `mkdocs serve`

## 💼 Casos Prácticos de Uso

1. **Gobierno y Calidad de Datos en Ingestas (Ingest Data Quality):**
   - Garantiza la estricta conformidad de esquemas y dominios antes de persistir datos operativos en almacenes analíticos.
2. **Prevención de Corrupción Financiera o Transaccional:**
   - Bloquea importaciones con importes negativos, claves duplicadas o nulos en campos obligatorios mediante `PRIMARY KEY` y `CHECK` constraints.
3. **Auditorías Automatizadas en Pipelines CI/CD:**
   - Ejecuta aserciones programáticas sobre datasets críticos para asegurar que las métricas de negocio cumplan con los umbrales esperados.