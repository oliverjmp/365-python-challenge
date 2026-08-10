# Módulo D87: Custom Decorator Telemetry (`Python Decorators`)

## Descripción General
Este módulo implementa un **decorador avanzado de telemetría** en Python. Su propósito es envolver funciones para medir automáticamente sus tiempos de respuesta (`perf_counter`), registrar métricas de rendimiento y auditar estados de éxito o fallo sin alterar la lógica de negocio.

---

## Características Principales
* **Metadatos Preservados**: Uso de `functools.wraps` para mantener la identidad (`__name__` y docstrings) de las funciones originales.
* **Medición de Alta Precisión**: Cálculo de milisegundos transcurridos mediante `time.perf_counter`.
* **Auditoría de Excepciones**: Bloque `try-except-finally` para registrar fallos y propagar errores de forma segura.

---

## Estructura del Proyecto
```text
D87-Custom-Decorator-Telemetry/
├── src/
│   ├── __init__.py
│   └── telemetry.py # Implementación del decorador monitor_telemetry
├── tests/
│   ├── __init__.py
│   └── test_telemetry.py # Pruebas unitarias de éxito y manejo de excepciones
├── requirements.txt # Dependencias del proyecto
└── README.md        # Documentación técnica del módulo