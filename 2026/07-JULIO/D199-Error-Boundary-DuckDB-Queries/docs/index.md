# D199 - Error Boundary & Custom Exceptions for DuckDB Queries

Sistema centralizado de **captura y gestión de errores de sintaxis y fallos de ejecución** en consultas SQL utilizando **DuckDB** y patrones de excepciones personalizadas en Python.

## 🏛️ Arquitectura Implementada
1. **Jerarquía de Excepciones (`src/exceptions.py`):** Clases tipadas (`SQLSyntaxError`, `QueryExecutionError`) que heredan de una excepción base (`DataLakeError`) para aislar los fallos del motor de datos.
2. **Patrón Error Boundary (`src/query_runner.py`):** Envoltorio seguro para la ejecución de sentencias SQL que traduce errores de bajo nivel del motor analítico en excepciones de negocio limpias y auditables.

## 💼 Casos de Uso Empresariales
- **Robustez en Pipelines de Datos:** Evita caídas abruptas de procesos ETL ante errores tipográficos o consultas malformadas en fuentes dinámicas.
- **Auditoría y Logging Limpio:** Facilita el registro estructurado de qué consulta exacta falló y por qué motivo técnico lo hizo.

## 🚀 Valor Añadido
- **Pruebas Unitarias al 100%:** Cobertura estricta con `pytest` y `pytest-cov`.
- **Interfaz Interactiva:** Dashboard en **Streamlit** para experimentación en tiempo real.

## ⚙️ Ejecución
- **Pruebas:** `python -m pytest --cov=src --cov-report=term-missing --cache-clear`
- **CLI:** `python main.py`
- **Dashboard:** `streamlit run app.py`