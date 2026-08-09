# Módulo D71: System Metrics Collector (`psutil + Logger`)

Este módulo implementa un script de monitoreo de infraestructura en Python que recopila métricas en tiempo real del sistema operativo (CPU, Memoria y Disco) y utiliza un sistema de registros (`logging`) para emitir advertencias automáticas cuando los recursos superan los umbrales de seguridad establecidos.

## Características Principales
- **Monitoreo de Recursos:** Extracción de porcentajes de uso de CPU, memoria RAM y almacenamiento en disco mediante la librería `psutil`.
- **Sistema de Alertas:** Evaluación automática de umbrales críticos para notificar incidencias a través de consola con marcas de tiempo (`INFO`, `WARNING`).
- **Pruebas Automatizadas:** Cobertura de código y validación mediante `pytest`.

## Estructura del Proyecto
```text
D71-System-Metrics-Collector/
├── src/
│   └── monitor.py
├── tests/
│   └── test_monitor.py
├── requirements.txt
└── README.md