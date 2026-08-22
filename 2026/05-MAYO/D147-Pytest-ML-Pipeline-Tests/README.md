# D147 - Pytest ML Pipeline Tests

Este hito implementa una **suite robusta de pruebas unitarias automatizadas utilizando Pytest y Fixtures** para validar la integridad, preprocesamiento y estabilidad de artefactos en un pipeline de Machine Learning.

## Características Principales
- **Uso Avanzado de Fixtures:** Separación limpia de datos sintéticos y estados de modelos ajustados para reutilización en múltiples pruebas.
- **Validación de Contratos de Entrada:** Comprobación estricta de excepciones ante estructuras vacías o dimensiones incongruentes entre características ($X$) y etiquetas ($y$).
- **Pruebas de Artefactos de ML:** Asegura que los pipelines encapsulados mantengan consistencia predictiva y probabilística antes de pasar a entornos de producción.

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
En entornos de MLOps, garantizar que los pipelines de preprocesamiento y estimación no fallen silenciosamente ante cambios de esquema es vital.

### Ejemplos de Uso:
1. **Validación Continua en CI/CD:**
   * *Caso:* Integrar esta suite de pruebas en GitHub Actions para verificar que cualquier cambio en el código del modelo no rompa los contratos de inferencia.
2. **Pruebas de Integridad de Modelos Serializados:**
   * *Caso:* Validar que los objetos exportados mediante `joblib` o `pickle` respondan correctamente a los contratos definidos en las fixtures.

## 📂 Estructura del Proyecto
```text
D147-Pytest-ML-Pipeline-Tests/
│
├── src/
│   ├── __init__.py
│   └── pipeline_model.py
├── tests/
│   ├── __init__.py
│   └── test_pipeline_model.py
├── run_pipeline_test.py
├── requirements.txt
└── README.md