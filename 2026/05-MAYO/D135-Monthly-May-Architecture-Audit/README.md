# D135 - Monthly May Architecture Audit

Este hito implementa un **motor de auditoría integral en Python Core y JSON** para validar el rendimiento, la consistencia estructural y la disponibilidad de los artefactos de Machine Learning desarrollados a lo largo del mes de mayo.

## Características Principales
- **Verificación de Integridad Estructural:** Comprueba de forma automatizada la existencia de archivos críticos, modelos entrenados y dependencias en el sistema de archivos.
- **Reportes Automatizados en JSON:** Estructura y exporta métricas de cumplimiento arquitectónico en formatos normalizados para trazabilidad.
- **Control de Excepciones y Resiliencia:** Valida tipos de datos de entrada para garantizar que los reportes de auditoría sean consistentes.

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
En entornos de ingeniería de Machine Learning y MLOps, auditar de manera periódica los pipelines y artefactos asegura que los sistemas en producción mantengan la trazabilidad y cumplan con los estándares de calidad antes del despliegue.

### Ejemplos de Uso:
1. **Validación de Pipelines de CI/CD:**
   * *Caso:* Comprobar que todos los modelos serializados (`.pkl`, `.onnx`), scripts de preprocesamiento y pruebas unitarias existan antes de empaquetar un contenedor Docker.
2. **Gobierno de Datos y Modelos:**
   * *Caso:* Generar reportes automáticos de cumplimiento para auditorías corporativas sobre qué modelos y datasets están activos en el repositorio.

## 📂 Estructura del Proyecto
```text
D135-Monthly-May-Architecture-Audit/
│
├── src/
│   ├── __init__.py
│   └── auditor.py
├── tests/
│   └── test_auditor.py
├── run_audit.py
├── requirements.txt
└── README.md