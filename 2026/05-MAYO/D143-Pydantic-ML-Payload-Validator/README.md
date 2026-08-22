# D143 - Pydantic ML Payload Validator

Este hito implementa un **validador estricto de esquemas de entrada para payloads de peticiones de inferencia** utilizando `Pydantic v2`.

## Características Principales
- **Validadores de Campo Personalizados (`@field_validator`):** Controlan límites físicos de tamaño de vectores y formatos normalizados de cadenas de texto (como versiones de modelos).
- **Validadores a Nivel de Modelo (`@model_validator`):** Aplican reglas de negocio complejas e interdependientes entre múltiples atributos del payload.
- **Tipado Estricto y Coerción Segura:** Asegura que los datos entrantes a la API de Machine Learning cumplan con los contratos esperados antes de consumir recursos de cómputo.

## 📂 Estructura del Proyecto
```text
D143-Pydantic-ML-Payload-Validator/
│
├── src/
│   ├── __init__.py
│   └── validators.py
├── tests/
│   ├── __init__.py
│   └── test_validators.py
├── run_validator.py
├── requirements.txt
└── README.md