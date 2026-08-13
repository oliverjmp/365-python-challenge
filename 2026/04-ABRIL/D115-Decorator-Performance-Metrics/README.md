# D115 - Decorator Performance Metrics

Este hito implementa un **decorador de telemetría avanzada para la medición automática de latencias y rendimiento de funciones** en aplicaciones Python.

## Características Principales
- **Metprogramación con Decoradores:** Uso de `@functools.wraps` para preservar la metadata original de las funciones decoradas.
- **Monitoreo de Latencia en Milisegundos:** Medición precisa utilizando `time.perf_counter`.
- **Captura de Excepciones Resiliente:** Bloques `try...except...finally` que aseguran el registro de telemetría incluso si la función sufre fallos críticos.

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
En arquitecturas de microservicios y APIs de alto rendimiento, medir el tiempo de respuesta de los métodos internos es vital para la observabilidad.

### Ejemplos de Uso:
1. **Monitoreo de Consultas a Bases de Datos:**
   * *Caso:* Registrar automáticamente la latencia de queries pesadas para detectar cuellos de botella.
2. **Auditoría de Endpoints o Funciones ETL:**
   * *Caso:* Medir el tiempo exacto que toma transformar lotes de datos para optimizar los pipelines.

## 📂 Estructura del Proyecto
```text
D115-Decorator-Performance-Metrics/
│
├── src/
│   ├── __init__.py
│   └── telemetry.py
├── tests/
│   └── test_telemetry.py
├── run_telemetry.py
├── requirements.txt
└── README.md