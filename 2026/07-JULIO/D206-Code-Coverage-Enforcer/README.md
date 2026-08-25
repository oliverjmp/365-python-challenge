# D206 - Code Coverage Enforcer & Quality Suite

[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/pytest-8.0%2B-orange.svg)](https://docs.pytest.org/)
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📋 Resumen Ejecutivo
El hito **D206** implementa un sistema automatizado de auditoría y cumplimiento estricto de cobertura de código mediante **Coverage.py** para motores analíticos impulsados por **DuckDB**. Este componente elimina la deuda técnica al hacer cumplir un umbral de cobertura del 100% tanto en líneas como en ramas lógicas, asegurando la máxima fiabilidad en pipelines de ingeniería de datos de nivel empresarial.

---

## 🏛️ Arquitectura del Repositorio

La estructura del proyecto mantiene una estricta separación de responsabilidades entre la capa analítica, los componentes de prueba y el sistema de políticas de calidad:

```text
D206-Code-Coverage-Enforcer/
├── .coveragerc                        # Configuración estricta de políticas de Coverage.py
├── data/
│   └── mock_audit.csv                 # Dataset sintético corporativo para auditoría
├── docs/
│   ├── index.md                       # Portal técnico ejecutivo y de gobierno de calidad
│   └── architecture.md                # Guía de arquitectura de enforcers y topología de pruebas
├── src/
│   ├── __init__.py
│   └── analytics_engine.py            # Motor analítico corporativo a auditar con DuckDB
├── tests/
│   ├── __init__.py
│   ├── conftest.py                    # Fixtures de Pytest para DuckDB in-memory
│   └── test_analytics.py              # Suite de pruebas unitarias exhaustivas (100% cobertura)
├── app.py                             # Dashboard interactivo de auditoría y cobertura en Streamlit
├── mkdocs.yml                         # Configuración formal del portal de documentación corporativa
├── requirements.txt                   # Definición de dependencias técnicas del proyecto
└── README.md                          # Documentación raíz corporativa del hito