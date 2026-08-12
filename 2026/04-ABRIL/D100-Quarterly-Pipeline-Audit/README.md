# D100 - Quarterly Pipeline Audit

Este proyecto marca el hito 100 de nuestro desafío de desarrollo en Python. Su objetivo principal es realizar una **auditoría integral del estado de salud de los pipelines desarrollados en el primer trimestre** mediante procesamiento de datos estructurados en JSON y análisis con Python Core.

## Características Principales
- **Análisis de Métricas JSON:** Lectura segura y robusta de archivos de configuración y telemetría de pipelines.
- **Auditoría de Salud Global:** Cálculo automático de tasas de éxito, conteo de errores y clasificación de estado del trimestre (`HEALTHY` o `CRITICAL`).
- **Pruebas Unitarias Rigurosas:** Cobertura de código validada al 100% con `pytest` y validación de excepciones (archivos inexistentes o JSON malformados).

## Requisitos del Entorno
- Python 3.11 o superior.
- Librerías especificadas en `requirements.txt`:
  ```text
  pytest==8.1.1
  pytest-cov==4.1.0