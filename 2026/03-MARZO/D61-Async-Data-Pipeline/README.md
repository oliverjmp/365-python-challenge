# Día 61 — Async Data Pipeline 🚀

## 📋 Descripción del Proyecto
El **Día 61** profundiza en la **Fase 3** del reto, enfocándose en la ingeniería orientada al rendimiento mediante concurrencia asíncrona. Este módulo implementa un pipeline capaz de consumir múltiples fuentes de datos externas en paralelo utilizando `asyncio` y `httpx`, reduciendo drásticamente el tiempo total de espera comparado con enfoques síncronos secuenciales.

---

## 🛠️ Tecnologías y Librerías Utilizadas
* **Python 3.x** (Tipado y control de concurrencia)
* **Asyncio** (Gestión del bucle de eventos y tareas concurrentes)
* **Httpx** (Cliente HTTP asíncrono de alto rendimiento con soporte HTTP/2)

---

## 📂 Arquitectura de Archivos
```text
D61-Async-Data-Pipeline/
├── D61.py                 # Código fuente principal del pipeline asíncrono
├── pipeline_metrics.json  # Artefacto de métricas y rendimiento exportado
└── README.md              # Documentación técnica del módulo