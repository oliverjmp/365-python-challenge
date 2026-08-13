# D119 - Code Coverage Enforcer

Este hito implementa un **validador estricto de cobertura de código (`Coverage.py`) para garantizar calidad antes de despliegue**, automatizando la integración de puertas de calidad (*Quality Gates*).

## Características Principales
- **Automatización de Umbrales:** Bloquea despliegues o pipelines de integración continua si el porcentaje de pruebas cae por debajo de la meta establecida (ej. 100%).
- **Integración con Subprocesos:** Ejecuta comandos de diagnóstico directamente sobre el entorno de pruebas de Python.
- **Resiliencia en CI/CD:** Asegura que ningún cambio suba a producción sin estar respaldado por pruebas unitarias rigurosas.

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
En entornos de ingeniería de software profesional, las puertas de calidad evitan que código sin probar llegue a ramas principales.

### Ejemplos de Uso:
1. **Validación Automática en Pipelines de GitHub Actions / GitLab CI:**
   * *Caso:* Forzar que el sistema falle automáticamente si un desarrollador introduce código nuevo sin sus respectivas pruebas unitarias.
2. **Auditoría Interna de Calidad:**
   * *Caso:* Generar reportes automatizados de métricas de cobertura previos a una auditoría de código o release oficial.

## 📂 Estructura del Proyecto
```text
D119-Code-Coverage-Enforcer/
│
├── src/
│   ├── __init__.py
│   └── quality_gate.py
├── tests/
│   └── test_quality_gate.py
├── run_quality.py
├── requirements.txt
└── README.md