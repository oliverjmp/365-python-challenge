# Módulo D92: JSON Structured Logger (`Python Logging + JSON`)

## Descripción General
Este módulo implementa un **sistema de logging estructurado corporativo** en Python. Su propósito es estandarizar la salida de los registros en formato JSON e incorporar trazabilidad de contexto mediante `Correlation IDs` para auditorías en arquitecturas modernas y pipelines de datos.

---

## Características Principales
* **Salida JSON Nativa**: Conversión automática de cada evento de log en un objeto JSON estructurado.
* **Trazabilidad Contextual**: Uso de `contextvars` para propagar de forma segura identificadores de correlación (`Correlation IDs`).
* **Metadatos Extensibles**: Capacidad de inyectar datos adicionales personalizados en cada evento de registro.

---

## Estructura del Proyecto
```text
D92-JSON-Structured-Logger/
├── src/
│   ├── __init__.py
│   └── structured_logger.py # Implementación del logger JSON y contexto
├── tests/
│   ├── __init__.py
│   └── test_structured_logger.py # Pruebas unitarias de formato y trazabilidad
├── requirements.txt # Dependencias del proyecto
└── README.md        # Documentación técnica del módulo