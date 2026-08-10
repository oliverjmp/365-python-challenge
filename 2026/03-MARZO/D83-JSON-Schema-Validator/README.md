# Módulo D83: JSON Schema Validator (`jsonschema + Python`)

## Descripción General
Este proyecto implementa un sistema de **validación estricta de contratos de datos** utilizando la librería `jsonschema` en Python. Su propósito es garantizar que los datos entrantes (*payloads*) cumplan rigurosamente con un esquema formal antes de ser procesados por los sistemas analíticos o de backend.

---

## Características Principales
* **Contratos Estrictos**: Definición clara de tipos, restricciones numéricas, longitudes y campos requeridos.
* **Control de Atributos Extra**: Bloqueo automático de propiedades no permitidas (`additionalProperties: False`).
* **Manejo de Errores Explicativo**: Captura de excepciones detalladas para auditoría y depuración.

---

## Estructura del Proyecto
```text
D83-JSON-Schema-Validator/
├── src/
│   ├── __init__.py
│   ├── schemas.py   # Definición de esquemas formales en formato JSON Schema
│   └── validator.py # Clase lógica encargada de aplicar las validaciones
├── tests/
│   ├── __init__.py
│   └── test_validator.py # Pruebas unitarias de casos válidos y erróneos
├── requirements.txt # Dependencias del proyecto
└── README.md        # Documentación técnica del módulo