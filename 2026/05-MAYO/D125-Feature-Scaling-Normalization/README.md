# D125 - Feature Scaling and Normalization

Este hito implementa un **motor avanzado de estandarización robusta y normalización de distribuciones sesgadas** utilizando `Scikit-learn Preprocessing` para preparar datos óptimos destinados a modelos analíticos y de Machine Learning.

## Características Principales
- **RobustScaler:** Escala las características utilizando estadísticas que son robustas frente a valores atípicos (outliers), basándose en el rango intercuartílico (IQR).
- **PowerTransformer (Yeo-Johnson):** Transforma datos sesgados hacia una distribución normal gaussiana, mejorando el rendimiento de algoritmos sensibles a la asimetría.
- **Pipelines Reutilizables:** Ajuste seguro en datos de entrenamiento (`fit_transform`) y aplicación coherente en producción (`transform`).

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
Muchos algoritmos de Machine Learning (como regresión logística, redes neuronales o SVMs) asumen que las características están centradas y tienen varianzas similares.

### Ejemplos de Uso:
1. **Modelos de Predicción de Precios Inmobiliarios:**
   * *Caso:* Normalizar variables altamente sesgadas como los metros cuadrados o los precios de venta que contienen mansiones (outliers).
2. **Scoring Crediticio:**
   * *Caso:* Estandarizar ingresos anuales y deudas sin que los valores extremos distorsionen el entrenamiento del modelo.

## 📂 Estructura del Proyecto
```text
D125-Feature-Scaling-Normalization/
│
├── src/
│   ├── __init__.py
│   └── scaler_engine.py
├── tests/
│   └── test_scaler.py
├── run_scaler.py
├── requirements.txt
└── README.md