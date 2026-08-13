# D124 - Missing Data Imputation Engine

Este hito implementa un **pipeline inteligente de imputación de valores nulos utilizando algoritmos avanzados de Machine Learning como KNN Imputer e Iterative Imputer (MICE)** mediante `Scikit-learn`.

## Características Principales
- **Imputación Basada en Vecinos (KNN):** Rellena los valores faltantes encontrando las muestras más cercanas en el espacio de características.
- **Imputación Multivariada Iterativa (MICE):** Modela cada característica con valores faltantes en función de las demás características como una función de regresión de forma iterativa.
- **Pipelines Reutilizables:** Permite ajustar los modelos con datos históricos (`fit_transform`) y aplicarlos de forma idéntica en producción (`transform`).

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
En ciencia de datos e ingeniería de Machine Learning, eliminar filas enteras por tener valores nulos desperdicia información valiosa. La imputación inteligente preserva la distribución estadística del dataset.

### Ejemplos de Uso:
1. **Limpieza de Datos en Banca y Finanzas:**
   * *Caso:* Estimar ingresos o puntajes crediticios faltantes en solicitudes de crédito basándose en perfiles de clientes con características similares.
2. **Preprocesamiento en Sensores IoT:**
   * *Caso:* Rellenar huecos temporales de telemetría industrial utilizando patrones multivariados de sensores correlacionados.

## 📂 Estructura del Proyecto
```text
D124-Missing-Data-Imputation-Engine/
│
├── src/
│   ├── __init__.py
│   └── imputation_engine.py
├── tests/
│   └── test_imputation.py
├── run_imputation.py
├── requirements.txt
└── README.md