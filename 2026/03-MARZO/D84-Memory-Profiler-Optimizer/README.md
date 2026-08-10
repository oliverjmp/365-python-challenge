# Módulo D84: Memory Profiler Optimizer (`tracemalloc + Python`)

## Descripción General
Este módulo implementa una herramienta de diagnóstico profundo utilizando la librería nativa `tracemalloc` de Python. Su propósito es perfilar, rastrear y comparar el uso de memoria en scripts analíticos de larga duración para detectar fugas (*memory leaks*) de forma precisa.

---

## Características Principales
* **Captura de Instantáneas**: Registro del estado de asignación de bloques de memoria en puntos críticos del código.
* **Análisis Diferencial**: Comparación directa entre dos instantáneas para aislar las líneas exactas que incrementan el consumo.
* **Pruebas Automatizadas**: Validación completa de métricas y detección de fugas simuladas.

---

## Estructura del Proyecto
```text
D84-Memory-Profiler-Optimizer/
├── src/
│   ├── __init__.py
│   ├── profiler.py  # Lógica principal de tracemalloc y comparación de snapshots
│   └── service.py   # Servicio analítico simulado con procesos de acumulación
├── tests/
│   ├── __init__.py
│   └── test_profiler.py # Pruebas unitarias de diagnóstico de memoria
├── requirements.txt # Dependencias del proyecto
└── README.md        # Documentación técnica del módulo