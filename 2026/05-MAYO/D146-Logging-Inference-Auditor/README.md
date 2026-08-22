# D146 - Logging Inference Auditor

Este hito implementa un **auditor de peticiones de inferencia para sistemas de Machine Learning**, utilizando el módulo de logging estándar de Python configurado con un formateador personalizado para emitir trazas estructuradas en formato JSON.

## Características Principales
- **Logging Estructurado en JSON:** Convierte cada evento de log en un objeto JSON plano ideal para indexación en plataformas de observabilidad (ELK, Datadog, CloudWatch).
- **Medición Precisa de Latencia:** Captura el tiempo exacto de ejecución en milisegundos (`latency_ms`) de cada llamada al modelo.
- **Trazabilidad de Errores y Éxitos:** Registra metadatos completos incluyendo ID de petición, versión del modelo, conteo de características y mensajes de error en caso de fallos.

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
En producción, auditar los modelos de Machine Learning no solo requiere saber si la API respondió, sino entender *qué* se predijo, *cuánto* tardó y *qué datos* ingresaron para auditorías de cumplimiento y debugging.

### Ejemplos de Uso:
1. **Sistemas de Monitoreo de APIs de ML:**
   * *Caso:* Consumir los logs estructurados en JSON desde contenedores Docker para graficar latencias p99 y tasas de error en tiempo real.
2. **Auditoría Forense y Trazabilidad:**
   * *Caso:* Rastrear peticiones específicas de usuarios (`request_id`) para investigar discrepancias o comportamientos anómalos en predicciones pasadas.

## 📂 Estructura del Proyecto
```text
D146-Logging-Inference-Auditor/
│
├── src/
│   ├── __init__.py
│   └── auditor.py
├── tests/
│   ├── __init__.py
│   └── test_auditor.py
├── run_audit.py
├── requirements.txt
└── README.md