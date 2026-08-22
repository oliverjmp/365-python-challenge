# D145 - Model Drift Detection Script

Este hito implementa un **script analítico para la detección temprana de deriva de datos (*data drift*) en producción**, utilizando NumPy y pruebas estadísticas robustas (Kolmogorov-Smirnov).

## Características Principales
- **Pruebas Estadísticas No Paramétricas:** Emplea la prueba de dos muestras de Kolmogorov-Smirnov (`ks_2samp`) para comparar distribuciones continuas sin asumir normalidad estricta en los datos.
- **Control Parametrizable de Significancia:** Permite ajustar umbrales de confianza estadísticos (`p-value` frente a `alpha`).
- **Validación Robusta de Entradas:** Previene fallos por datasets vacíos o nulos mediante excepciones controladas.

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
En sistemas de Machine Learning en producción, los datos del mundo real cambian con el tiempo (estacionalidad, cambios de comportamiento de usuarios, factores económicos), degradando la precisión del modelo (*model decay*).

### Ejemplos de Uso:
1. **Monitoreo Automatizado de Modelos (MLOps):**
   * *Caso:* Ejecutar pipelines diarios que comparen las características de las peticiones de inferencia de la última semana contra el dataset de entrenamiento original para disparar alertas de re-entrenamiento.
2. **Auditoría de Calidad de Datos en Pipelines:**
   * *Caso:* Detectar anomalías estructurales o cambios de escala en fuentes de datos externas antes de alimentar modelos analíticos críticos.

## 📂 Estructura del Proyecto
```text
D145-Model-Drift-Detection-Script/
│
├── src/
│   ├── __init__.py
│   └── drift_detector.py
├── tests/
│   ├── __init__.py
│   └── test_drift_detector.py
├── run_drift_detection.py
├── requirements.txt
└── README.md