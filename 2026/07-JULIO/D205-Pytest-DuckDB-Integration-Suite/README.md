# D205 - Pytest DuckDB Integration Suite

[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/pytest-8.0%2B-orange.svg)](https://docs.pytest.org/)
[![DuckDB](https://img.shields.io/badge/duckdb-0.10%2B-yellow.svg)](https://duckdb.org/)
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📋 Resumen Ejecutivo
El hito **D205** implementa una arquitectura avanzada de pruebas unitarias y de integración orientada a validar la corrección lógica, la consistencia transaccional y el rendimiento de consultas SQL vectorizadas ejecutadas sobre **DuckDB**. Mediante el uso estricto de **Pytest Fixtures**, este módulo aísla los entornos de ejecución en memoria (`:memory:`), permitiendo simular escenarios analíticos complejos de manera determinista, reproducible y con una cobertura de código estricta del 100%.

---

## 🏛️ Arquitectura del Repositorio

La estructura del proyecto sigue un diseño modular y desacoplado, separando la lógica analítica, la infraestructura de pruebas y las interfaces de auditoría interactiva:

```text
D205-Pytest-DuckDB-Integration-Suite/
├── data/
│   └── mock_transactions.csv          # Dataset sintético corporativo para control
├── docs/
│   ├── index.md                       # Portal técnico ejecutivo y especificaciones
│   └── architecture.md                # Guía detallada de la topología de pruebas y fixtures
├── src/
│   ├── __init__.py
│   └── query_validator.py             # Capa de lógica de negocio y consultas SQL validadas
├── tests/
│   ├── __init__.py
│   ├── conftest.py                    # Fixtures globales de Pytest para DuckDB in-memory
│   └── test_queries.py                # Suite de pruebas unitarias avanzadas (100% cobertura)
├── app.py                             # Dashboard interactivo de auditoría y visualización en Streamlit
├── mkdocs.yml                         # Configuración del portal de documentación corporativa
├── requirements.txt                   # Definición formal de dependencias técnicas
└── README.md                          # Documentación raíz del hito