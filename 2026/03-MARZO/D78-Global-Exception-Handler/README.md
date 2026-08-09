# Módulo D78: Global Exception Handler (`Python Exception Handling`)

## Descripción General
Este proyecto implementa un **sistema centralizado de captura y manejo global de excepciones** en FastAPI. Su propósito principal es interceptar tanto las excepciones de negocio controladas como los errores de servidor no controlados, transformándolos de manera uniforme en respuestas HTTP estandarizadas, limpias y con códigos de estado coherentes.

---

## Características Principales
* **Manejo Centralizado**: Evita la duplicación de bloques `try-except` en los endpoints de la API.
* **Respuestas Estandarizadas**: Devuelve un formato JSON consistente (`status` y `message`) para todos los errores de la aplicación.
* **Separación de Responsabilidades**: 
  * Captura de reglas de negocio personalizadas (`BusinessException`) devolviendo un código HTTP `404 Not Found`.
  * Captura global de fallos imprevistos del sistema (`Exception`) devolviendo un código HTTP `500 Internal Server Error`.
* **Pruebas Unitarias Robustas**: Cobertura de código al 100% validando cada flujo de excepción.

---

## Estructura del Proyecto
```text
D78-Global-Exception-Handler/
├── src/
│   ├── __init__.py
│   └── main.py          # Lógica de la API y manejadores globales de excepciones
├── tests/
│   ├── __init__.py
│   └── test_handler.py  # Pruebas unitarias para validar las respuestas HTTP y excepciones
├── requirements.txt     # Dependencias del proyecto
└── README.md            # Documentación técnica del módulo