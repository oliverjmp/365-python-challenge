# Módulo D90: Quarterly Code Refactoring (`Refactoring Toolkit`)

## Descripción General
Este módulo implementa un **Refactoring Toolkit** basado en el análisis de Árboles de Sintaxis Abstracta (`ast`) en Python. Su propósito es consolidar el cierre del trimestre auditando la deuda técnica y detectando automáticamente funciones excesivamente largas que requieran refactorización.

---

## Características Principales
* **Análisis Estático**: Inspección profunda del código fuente sin necesidad de ejecutarlo.
* **Control de Métricas**: Detección configurable de funciones que superan el umbral de líneas permitidas.
* **Pruebas Automatizadas**: Verificación de robustez ante código limpio o con excesos de complejidad.

---

## Estructura del Proyecto
```text
D90-Quarterly-Code-Refactoring/
├── src/
│   ├── __init__.py
│   └── code_refactor_tool.py # Herramienta de análisis estático basada en AST
├── tests/
│   ├── __init__.py
│   └── test_refactor_tool.py # Pruebas unitarias para validar detección de deuda técnica
├── requirements.txt # Dependencias del proyecto
└── README.md        # Documentación técnica del módulo